"""
This script trains a clustering model using the data
provided in the configuration file.

The model is then logged using MLflow and the
Code Carbon Emissions Tracker is used to measure the emissions.
"""

import os
from datetime import datetime
from pprint import pprint

import hydra
import mlflow
import mlflow.sklearn
import pandas as pd
from codecarbon import EmissionsTracker
from dotenv import load_dotenv
from mlflow.models.signature import infer_signature
from omegaconf import DictConfig
from sklearn.cluster import DBSCAN, KMeans
import joblib

load_dotenv()

BASE_PATH = os.getenv("BASE_PATH")


if not BASE_PATH or not os.path.exists(BASE_PATH):
    raise ValueError(f"Invalid BASE_PATH: {BASE_PATH}. Check .env file")


@hydra.main(
    version_base=None, config_path=os.path.join(BASE_PATH, "conf"), config_name="config"
)
def main(cfg: DictConfig):
    """
    This script trains a clustering model using the data
    provided in the configuration file.

    The model is then logged using MLflow and the
    Code Carbon Emissions Tracker is used to measure the emissions.

    Args:
        cfg (DictConfig): Configuration file for the model training process.

    Returns:
        None
    """

    # Initialize Code Carbon Emissions Tracker
    tracker = EmissionsTracker(
        output_dir=os.path.join(BASE_PATH, cfg.codecarbon.save_dir),
        output_file="emissions.csv",
        measure_power_secs=1,
    )
    tracker.start()

    # Start an MLflow experiment run and set the experiment name
    mlflow.set_experiment("Bogota_Smart_City_Models")

    run_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    with mlflow.start_run(run_name=f"{cfg.model.name}_{run_timestamp}_run"):
        mlflow.log_param("model_name", cfg.model.name)
        for key, value in cfg.model.params.items():
            mlflow.log_param(f"model_params_{key}", value)

        mlflow.log_param("data_processed_dir", cfg.data.processed_dir)

        print("Current configuration:")
        pprint(cfg)

        data_path = os.path.join(BASE_PATH, cfg.data.processed_dir)
        print(f"Loading data from: {data_path}")

        df = pd.read_parquet(data_path)
        print("Data sample:")
        print(df.head())

        environment = cfg.env

        if environment == "dev":
            sample_ratio = cfg.env.dev.data_sample_ratio
            mlflow.log_param("data_sample_ratio", sample_ratio)
            df = df.sample(frac=sample_ratio)
            print(
                f"Data sample size adjusted to {sample_ratio}. New sample size: {len(df)}"
            )

        else:
            mlflow.log_param("data_sample_ratio", 1.0)

        model_name = cfg.model.name
        params = cfg.model.params
        print(f"Preparing to run model: {model_name} with parameters: {params}")

        x = df.select_dtypes(include=["number"]).values

        if model_name == "kmeans":
            model = KMeans(**params)
            model.fit(x)
            print("KMeans clustering complete.")

            #use the model to predict the cluster labels for x

            df = pd.DataFrame(x)
            df["cluster"] = model.predict(x)

            df.to_parquet(os.path.join(BASE_PATH, "data/3_Gold/clustered_data.parquet"))


            print("Cluster centers:")
            print(model.cluster_centers_)
            print("Cluster labels:")
            print(model.labels_)
            print("Model parameters:")
            print(model.get_params())

            unique_clusters = len(set(model.labels_))
            print("Unique cluster labels:")
            print(unique_clusters)
            

            input_example = x[:5]

            signature = infer_signature(x, model.predict(x))

            mlflow.log_metric("num_clusters", unique_clusters)

            # Stop the emissions tracker and log emissions
            emissions = tracker.stop()
            mlflow.log_metric("CO2_kg", emissions)

            #Log the model parameters
            mlflow.sklearn.log_model(
                model,
                artifact_path="models/kmeans",
                signature=signature,
                input_example=input_example,
            )

        elif model_name == "dbscan":
            model = DBSCAN(**params)
            model.fit(x)
            print("DBSCAN clustering complete.")
            print("Cluster labels (with noise points as -1):")
            print(model.labels_)
            labels = model.labels_
            num_clusters = len(set(labels)) - (1 if -1 in labels else 0)

            input_example = x[:5]

            mlflow.log_metric("num_clusters", num_clusters)

            # Stop the emissions tracker and log emissions
            emissions = tracker.stop()
            mlflow.log_metric("CO2_kg", emissions)

            mlflow.sklearn.log_model(
                model,
                artifact_path="models/dbscan",
                input_example=input_example,  # signature is omitted
            )

        else:
            print(f"Model {model_name} is not supported.")

        print(
            "Model instantiation complete. \
            Proceed with training or evaluation as required."
        )

    print("MLflow run completed!")


if __name__ == "__main__":
    main()
