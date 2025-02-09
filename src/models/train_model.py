# src/train.py
import pandas as pd
import hydra
from omegaconf import DictConfig
from pprint import pprint
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()  # Loads from .env by default

## Define base path (adjust if notebook is in different location)
BASE_PATH = os.getenv('BASE_PATH')

# Verify base path exists
if not BASE_PATH or not os.path.exists(BASE_PATH):
    raise ValueError(f"Invalid BASE_PATH: {BASE_PATH}. Check your .env file and directory structure")

@hydra.main(version_base=None, config_path=os.path.join(BASE_PATH,"conf"), config_name="config")
def main(cfg: DictConfig):
    # 1. Print the complete configuration
    print("Current configuration:")
    pprint(cfg)
    
    # 2. Access data paths
    # Construct the full data path from configuration
    data_path = os.path.join(BASE_PATH, cfg.data.processed_dir)
    print(f"Loading data from: {data_path}")
    
    # Load the data using pandas (assuming a parquet file)
    df = pd.read_parquet(data_path)
    print("Data sample:")
    print(df.head())

    # get the data sample ratio from the configuration and adjust the data sample size
    data_sample_ratio = cfg.data.data_sample_ratio
    if data_sample_ratio < 1:
        df = df.sample(frac=data_sample_ratio)
        print(f"Data sample size adjusted to {data_sample_ratio} of the original size.")

    
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
        
    elif model_name == "dbscan":
        from sklearn.cluster import DBSCAN
        model = DBSCAN(**params)
        # Fit the DBSCAN model on the numeric features
        model.fit(X)
        print("DBSCAN clustering complete.")
        # In DBSCAN, noise points are labeled as -1
        print("Cluster labels (with noise points as -1):")
        print(model.labels_)
        
    else:
        print(f"Model {model_name} is not supported.")
    
    print("Model instantiation complete. Proceed with training or evaluation as required.")
    
if __name__ == "__main__":
    main()