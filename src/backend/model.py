import joblib
import numpy as np
import pandas as pd

# Cargar modelo y encoder una sola vez al iniciar
model = joblib.load('./models/model.joblib')
oh_encoder = joblib.load('./models/onehot_encoder.joblib')

# Diccionario de clases
heart_disease_names = {0: 'normal', 1: 'heart disease'}

def predict(features: list) -> str:
    # Transformar las variables categóricas según el criterio dado
    features[1] = 0 if features[1] == 'F' else 1  # F -> 0, M -> 1
    features[8] = 0 if features[8] == 'N' else 1  # N -> 0, Y -> 1
    features[10] = {'Down': 0, 'Flat': 1, 'Up': 2}.get(features[10], -1)  # Down -> 0, Flat -> 1, Up -> 2

    # Separar numéricas y categóricas
    numeric = [features[0], features[1], features[3], features[4], 
               features[5], features[7], features[8], features[9], features[10]]
    categorical = [features[2], features[6]]  # depende de tu entrenamiento

    # Convertir a arrays 2D
    numeric_array = np.array(numeric).reshape(1, -1)              # (1, 9)
    
    # Si usas pandas, ajusta la entrada para one hot encoding
    categorical_df = pd.DataFrame([categorical], columns=['ChestPainType', 'RestingECG'])
    categorical_encoded = oh_encoder.transform(categorical_df).toarray()

    # Concatenar horizontalmente → (1, 9+k)
    final_features = np.hstack([numeric_array, categorical_encoded])

    # Predicción
    prediction = model.predict(final_features)

    return heart_disease_names[prediction[0]]
