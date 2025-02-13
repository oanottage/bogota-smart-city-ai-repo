# tests/test_api.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)
def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Bogotá Smart City Clustering API!"}

def test_predict_endpoint():
    payload = {"feature1": 754, "feature2": 564, "feature3": 456, "feature4": 323, "feature5":295, "feature6": 290, "feature7": 687, "feature8": 760}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()