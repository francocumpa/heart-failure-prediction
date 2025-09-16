from fastapi import FastAPI, Request
from model import predict

app = FastAPI()

@app.get("/")
def root():
    return {"ok": 1}

@app.post("/predict")
async def predict_route(request: Request):
    # Obtener los datos de la solicitud como JSON
    data = await request.json()
    features = data["features"]

    # Realizar la predicción
    prediction_name = predict(features)

    # Devolver el resultado
    return {"prediction": prediction_name}
