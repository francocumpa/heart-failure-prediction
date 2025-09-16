import gradio as gr
import requests

# Definir la URL de la API
API_URL = "http://127.0.0.1:8000/predict"

# Función que interactúa con la API y realiza la predicción
def predict_heart_disease(age, sex, chest_pain_type, resting_bp, cholesterol, fasting_bs, resting_ecg, max_hr, exercise_angina, oldpeak, st_slope):
    # Ajustamos la lógica de fasting_bs
    fasting_bs = 1 if fasting_bs > 120 else 0

    # Crear el diccionario de datos para la API
    features = [age, sex, chest_pain_type, resting_bp, cholesterol, fasting_bs, resting_ecg, max_hr, exercise_angina, oldpeak, st_slope]
    
    # Hacer la solicitud POST a la API
    response = requests.post(API_URL, json={"features": features})
    
    # Obtener la predicción
    prediction = response.json().get("prediction")
    return f"Prediction: {prediction}"

# Crear la interfaz de usuario con Gradio
iface = gr.Interface(
    fn=predict_heart_disease,
    inputs=[
        gr.Slider(minimum=20, maximum=100, step=1, value=45, label="Age (years)"),  # Slider para Edad
        gr.Radio(["F", "M"], label="Sex", value="M"),  # Por defecto es "M"
        gr.Radio(["TA", "ATA", "NAP", "ASY"], label="Chest Pain Type", value="TA"),  # Por defecto es "TA"
        gr.Slider(minimum=80, maximum=200, step=1, value=120, label="Resting BP (mm Hg)"),  # Slider para BP
        gr.Slider(minimum=100, maximum=400, step=1, value=230, label="Cholesterol (mg/dl)"),  # Slider para colesterol
        gr.Slider(minimum=60, maximum=200, step=1, value=120, label="Fasting Blood Sugar (mg/dl)"),  # Slider para Fasting BS
        gr.Radio(["Normal", "ST", "LVH"], label="Resting ECG", value="Normal"),  # Por defecto "Normal"
        gr.Slider(minimum=60, maximum=202, step=1, value=150, label="Max HR"),  # Slider para max HR
        gr.Radio(["Y", "N"], label="Exercise Angina", value="N"),  # Por defecto "N"
        gr.Slider(minimum=0, maximum=6, step=0.1, value=1.2, label="Oldpeak (ST Depression)"),  # Slider para Oldpeak
        gr.Radio(["Up", "Flat", "Down"], label="ST Slope", value="Flat")  # Por defecto "Flat"
    ],
    outputs="text",
    live=True,
)

# Iniciar la interfaz de Gradio
iface.launch()
