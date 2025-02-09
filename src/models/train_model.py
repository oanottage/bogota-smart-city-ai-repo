# src/train.py
import pandas as pd
import hydra
from omegaconf import DictConfig
import mlflow
import mlflow.sklearn  # Import the appropriate flavor based on your model framework
from mlflow.models.signature import infer_signature  # Import infer_signature
from codecarbon import EmissionsTracker
from pprint import pprint
import os
from dotenv import load_dotenv
from datetime import datetime



# Load environment variables
load_dotenv()  # Loads from .env by default

## Define base path (adjust if notebook is in different location)
BASE_PATH = os.getenv('BASE_PATH')

# Verify base path exists
if not BASE_PATH or not os.path.exists(BASE_PATH):
    raise ValueError(f"Invalid BASE_PATH: {BASE_PATH}. Check your .env file and directory structure")

@hydra.main(version_base=None, config_path=os.path.join(BASE_PATH,"conf"), config_name="config")
def main(cfg: DictConfig):
    # Initialize Code Carbon Emissions Tracker
    tracker = EmissionsTracker(
        output_dir= os.path.join(BASE_PATH, cfg.codecarbon.save_dir),
        output_file="emissions.csv",
        measure_power_secs=1  # Measure power consumption every second
    )
    tracker.start()

    # Start an MLflow experiment run and set the experiment name
    mlflow.set_experiment("Bogota_Smart_City_Models")
    
    run_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    with mlflow.start_run(run_name=f"{cfg.model.name}_{run_timestamp}_run"):
        # Log key configuration parameters using MLflow
        mlflow.log_param("model_name", cfg.model.name)
        for key, value in cfg.model.params.items():
            mlflow.log_param(f"model_params_{key}", value)

        mlflow.log_param("data_processed_dir", cfg.data.processed_dir)
        
    
        # Print the complete configuration for debugging purposes
        print("Current configuration:")
        pprint(cfg)
        
        # Construct the full data path from configuration
        data_path = os.path.join(BASE_PATH, cfg.data.processed_dir)
        print(f"Loading data from: {data_path}")
    
        # Load the data (assuming a parquet file)
        df = pd.read_parquet(data_path)
        print("Data sample:")
        print(df.head())

        # get the data sample ratio from the configuration and adjust the data sample size
        environment = cfg.env
        
        if environment == "dev":
            sample_ratio = cfg.env.dev.data_sample_ratio
            mlflow.log_param("data_sample_ratio", sample_ratio)
            df = df.sample(frac=sample_ratio)
            print(f"Data sample size adjusted to {sample_ratio}. New sample size: {len(df)}")
        
        else:
            mlflow.log_param("data_sample_ratio", 1.0)

        
        # 3. Determine the model to use and its parameters
        model_name = cfg.model.name
        params = cfg.model.params
        print(f"Preparing to run model: {model_name} with parameters: {params}")

        # For clustering models, we assume the features for clustering are numeric.
        # You might need to adjust this selection to match your data schema.
        X = df.select_dtypes(include=["number"]).values
        
        # 5. Instantiate the selected model
        if model_name == "kmeans":
            from sklearn.cluster import KMeans
            model = KMeans(**params)
            # Fit the KMeans model on the numeric features
            model.fit(X)
            print("KMeans clustering complete.")
            print("Cluster centers:")
            print(model.cluster_centers_)
            print("Cluster labels:")
            print(model.labels_)

            # Get the unique amount of clusters in the model
            unique_clusters = len(set(model.labels_))
            print("Unique cluster labels:")
            print(unique_clusters)

            # Prepare an input example (e.g., first 5 rows of X)
            input_example = X[:5]
            # Infer the model signature based on inputs and predictions
            signature = infer_signature(X, model.predict(X))
            
            # Log a metric: number of clusters detected
            mlflow.log_metric("num_clusters", unique_clusters)
            # Log the model (only once) with signature and input example

            # Stop the emissions tracker and log emissions
            emissions = tracker.stop()
            mlflow.log_metric("CO2_kg", emissions)
            
            mlflow.sklearn.log_model(
                model, 
                artifact_path="models/kmeans", 
                signature=signature, 
                input_example=input_example
            )
            
            
        elif model_name == "dbscan":
            from sklearn.cluster import DBSCAN
            model = DBSCAN(**params)
            # Fit the DBSCAN model on the numeric features
            model.fit(X)
            print("DBSCAN clustering complete.")
            # In DBSCAN, noise points are labeled as -1
            print("Cluster labels (with noise points as -1):")
            print(model.labels_)
            # Calculate and log the number of clusters (ignoring noise labeled as -1)
            labels = model.labels_
            num_clusters = len(set(labels)) - (1 if -1 in labels else 0)
            
            # For DBSCAN, there's no predict method. However, you can still log an input_example.
            input_example = X[:5]
            
            mlflow.log_metric("num_clusters", num_clusters)
            
            # Stop the emissions tracker and log emissions
            emissions = tracker.stop()
            mlflow.log_metric("CO2_kg", emissions)

            mlflow.sklearn.log_model(
                model, 
                artifact_path="models/dbscan", 
                input_example=input_example  # signature is omitted here since DBSCAN doesn't have predict
            )
            
        else:
            print(f"Model {model_name} is not supported.")
        
        print("Model instantiation complete. Proceed with training or evaluation as required.")

    print("MLflow run completed!")
    
if __name__ == "__main__":
    main()