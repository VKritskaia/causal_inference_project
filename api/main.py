from fastapi import FastAPI
import pickle
import numpy as np

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

@app.post("/predict")
def predict(temperature: float, rainfall: float):
    input_data = np.array([[temperature, rainfall]])
    prediction = model.predict(input_data)
    return {"predicted_sales": prediction[0]}

