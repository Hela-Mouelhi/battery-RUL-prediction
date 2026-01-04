# battery-RUL-prediction
## 📌 Project Objectives
- Predict the total battery lifetime (cycle life)
- Estimate the Remaining Useful Life (RUL) of a battery
- Compute the failure probability using Weibull distribution
- Provide an interactive web interface for real-time estimation
- Bridge data science models with engineering reliability concepts

## 📂 Dataset
**Source:** MathWorks Battery Degradation Dataset  
**Platform:** [![Dataset]([https://img.shields.io/badge/📊-Dataset-blue](https://ssd.mathworks.com/supportfiles/predmaint/batterycyclelifeprediction/v2/batteryDischargeData.zip))]

### Description:
- Battery aging and discharge data
- Cycle-based degradation measurements

### Format:
- Originally `.mat` files
- Converted to `.csv` for machine learning and web deployment

### Key Features Used:
- `mean_dQdV` → Mean incremental capacity feature
- `max_dQdV` → Maximum incremental capacity feature
- `temperature` → Operating temperature
- `voltage` → Battery voltage
- `cycle_life` → Total battery lifetime (target variable)

## 🧠 Methods & Models Used

### 1️⃣ Exploratory Data Analysis (EDA)
- Statistical analysis of battery degradation features
- Correlation analysis between cycle life and dQ/dV features
- Visualization of degradation trends across cycles

**Techniques:**
- Histograms
- Scatter plots
- Correlation heatmaps

### 2️⃣ Machine Learning Model – Battery Lifetime Prediction
**Model Used:** Regression model (trained on degradation features)  
**Objective:** Predict total battery lifetime (in cycles)

**Inputs:**
- Mean dQ/dV
- Max dQ/dV
- Temperature
- Voltage

**Output:**
- Predicted total battery lifetime

**Why ML?**
- Captures non-linear relationships
- Handles multivariate degradation indicators
- More flexible than physics-only models

### 3️⃣ Remaining Useful Life (RUL) Estimation
RUL is computed as:
RUL = Predicted Cycle Life − Current Cycle
- Ensures RUL ≥ 0
- Gives an interpretable health indicator for users

### 4️⃣ Weibull Reliability Analysis (Failure Probability)
To estimate failure probability, a Weibull distribution is fitted on battery lifetime data.

**Weibull Parameters:**
- Shape (β) ≈ 3.35
- Scale (η) ≈ 1144.69

**Why Weibull?**
- Widely used in reliability engineering
- Models increasing failure rate due to aging
- Well-suited for battery degradation behavior

**Failure Probability Formula:**
P_f(t) = 1 − e^−(t/η)^β

Where:
- `t` = number of cycles
- `β` = shape parameter
- `η` = scale parameter

### 5️⃣ Visualization Techniques
The project includes rich and colorful visualizations, such as:
- Battery lifetime distribution
- Weibull probability density function (PDF)
- Weibull cumulative distribution function (CDF)
- RUL vs cycle number
- Failure probability vs cycles

**These plots help interpret:**
- Degradation trends
- Reliability evolution
- Risk of failure over time

## 🌐 Web Application (Flask)
**Features:**
- User inputs:
  - Mean dQ/dV
  - Max dQ/dV
  - Temperature
  - Voltage
  - Current cycle
- Outputs:
  - Predicted total lifetime
  - Remaining Useful Life (RUL)
  - Failure probability (%)

**Tech Stack:**
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS
- **Models:**
  - Saved ML model (`.pkl`)
  - Saved Weibull parameters (`.pkl`)

## 🗂️ Project Structure
battery-rul-prediction/


├── app.py # Flask application

├── battery_lifetime_model.pkl 
├── weibull_params.pkl 
├── templates/
    ── index.html 
├── static/
   ── style.css 


## 🎯 Key Outcomes
- Accurate battery lifetime prediction
- Clear estimation of Remaining Useful Life
- Probabilistic failure assessment
- User-friendly and interpretable web interface
- Strong combination of ML + reliability engineering

## 🚀 Future Improvements
- Add confidence intervals for predictions
- Support multiple battery chemistries
- Integrate real-time sensor data (IoT)
- Deploy the web app to cloud platforms (Render / Railway)

