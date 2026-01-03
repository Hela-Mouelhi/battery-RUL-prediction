# battery-RUL-prediction
## 📌 Project Objectives
- Predict the total battery lifetime (cycle life)
- Estimate the Remaining Useful Life (RUL) of a battery
- Compute the failure probability using Weibull distribution
- Provide an interactive web interface for real-time estimation
- Bridge data science models with engineering reliability concepts

## 📂 Dataset
**Source:** MathWorks Battery Degradation Dataset  
**Platform:** MathWorks (MATLAB / Simulink battery data)

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
