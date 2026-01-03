from flask import Flask, render_template, request
import joblib
import numpy as np
import math

app = Flask(__name__)

# Load trained models
lifetime_model = joblib.load("battery_lifetime_model.pkl")  # trained on 6 features
weibull_params = joblib.load("weibull_params.pkl")
BETA = weibull_params["beta"]
ETA = weibull_params["eta"]

# Weibull failure probability
def weibull_failure_probability(cycles, beta, eta):
    return 1 - math.exp(-(cycles / eta) ** beta)

@app.route("/", methods=["GET", "POST"])
def index():
    predicted_life = None
    rul = None
    failure_prob = None
    error_message = None

    if request.method == "POST":
        try:

            temperature = float(request.form["temperature"].replace(",", "."))
            mean_dQdV = float(request.form["mean_dQdV"].replace(",", "."))
            max_dQdV = float(request.form["max_dQdV"].replace(",", "."))
            voltage = float(request.form["voltage"].replace(",", "."))
            current = float(request.form["current"].replace(",", "."))
            Qd = float(request.form["Qd"].replace(",", "."))


            # Validation based on dataset ranges
            if not (30 <= temperature <= 37):
                raise ValueError("Temperature must be between 30 and 37 °C")
            
            if not (-0.77 <= mean_dQdV <= -0.72):
                raise ValueError("Mean dQ/dV must be between -0.77 and -0.72")
            
            if not (-0.02 <= max_dQdV <= 0):
                raise ValueError("Max dQ/dV must be between -0.02 and 0")
            
            if not (3.10 <= voltage <= 3.13):
                raise ValueError("Voltage must be between 3.10 and 3.13 V")
            
            if not (-0.15 <= current <= 0.03):
                raise ValueError("Current must be between -0.15 and 0.03 A")
            
            if not (0.28 <= Qd <= 0.31):
                raise ValueError("Qd must be between 0.28 and 0.31")

            # Prediction
            X = np.array([[mean_dQdV, max_dQdV, temperature, voltage, current, Qd]])
            predicted_life = lifetime_model.predict(X)[0]

            # RUL
            current_cycles = float(request.form.get("current_cycles", 0))
            rul = max(predicted_life - current_cycles, 0)

            # Weibull
            failure_prob = weibull_failure_probability(current_cycles, BETA, ETA) * 100

        except Exception as e:
            error_message = str(e)

    return render_template(
        "index.html",
        predicted_life=predicted_life,
        rul=rul,
        failure_prob=failure_prob,
        error_message=error_message
    )

if __name__ == "__main__":
    app.run(debug=True)
