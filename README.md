# Weather-Driven Sales Forecasting API

1️⃣ **Introduction**

This project analyzes the causal impact of weather on product sales using **causal inference** techniques. If a causal relationship is found, we train a **regression model** to predict sales based on weather conditions and deploy it via **FastAPI**.

2️⃣ **Data**

Sales data: Daily sales for specific products (e.g., beverages, winter clothing).
Weather data: Temperature, humidity, rainfall from historical sources.


3️⃣ **Causal Analysis Approach**

Tool: DoWhy
Method: Backdoor adjustment / Propensity Score Matching
Key Question: Does temperature significantly impact product sales?


4️⃣ **Model & API**
If causality is established, a Linear Regression model is trained.
FastAPI endpoint for sales prediction based on input weather data.


5️⃣ How to Run

1. Run Causal Analysis

``
cd notebooks jupyter notebook 2_causal_analysis.ipynb
``

2. Train Model (if applicable)

``
cd notebooks jupyter notebook 3_model_training.ipynb
``

3. Run API Locally

``
cd api uvicorn main:app --reload
``

4. Test API Request

``
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"temperature": 30, "rainfall": 2}'
``
