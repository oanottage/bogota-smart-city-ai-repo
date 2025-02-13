import os

from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
import mlflow
import pandas as pd
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import MinMaxScaler
from dotenv import load_dotenv

import pickle
import joblib



load_dotenv()

BASE_PATH = os.getenv('BASE_PATH')

if not BASE_PATH or not os.path.exists(BASE_PATH):
    raise ValueError(f"Invalid BASE_PATH: {BASE_PATH}. Check your .env file")

# Initialize FastAPI app
app = FastAPI(
    title="Bogotá Smart City Clustering API",
    description="API to serve ML clustering models for urban mobility insights.",
    version="1.0.0"
)

# Pydantic model for request payload
class PredictionRequest(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    feature4: float
    feature5: float
    feature6: float
    feature7: float
    feature8: float
    # Add fields as needed based on your model's input requirements

@app.get("/")
def root():
    return {"message": "Welcome to the Bogotá Smart City Clustering API!"}

@app.post("/predict")
def predict(data: PredictionRequest):
    # Load the trained model (KMeans or DBSCAN)
    load_dotenv()
    BASE_PATH = os.getenv('BASE_PATH')
    model_name = "kmeans"  # Example, this could come from your config
    model_path = f"{BASE_PATH}/mlruns/252850428605173686/892ccda8802545239b930715b8c2c1af/artifacts/models/{model_name}/model.pkl"
    try:
        # Load the pickled parameters
        with open(model_path, "rb") as f:
            model = pickle.load(f)

    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Model not found")
    

    # Convert input data to appropriate format
    data = [[data.feature1, data.feature2, data.feature3, data.feature4, data.feature5, data.feature6, data.feature7, data.feature8]]  # Adjust based on model's input features

    #load the scaler
    scaler_path = f"{BASE_PATH}/models/incidences_scaler.pkl"
    scaler = joblib.load(scaler_path)
    data = scaler.transform(data)

    # map the cluster number to the cluster name
    cluster_mapping = {4: 'A', 1: 'B', 5: 'C', 3: 'D', 2: 'E'}

    # Make prediction
    prediction = model.predict(data) + 1

    # Map the cluster number to the cluster name
    prediction = [cluster_mapping[pred] for pred in prediction]
    
    print("Prediction: ", prediction)
    return {"prediction": prediction}