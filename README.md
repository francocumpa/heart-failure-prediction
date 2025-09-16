# Heart Failure Prediction Project

## Descripción

Este proyecto es una aplicación web para predecir enfermedades cardíacas en un paciente basándose en una serie de atributos médicos. La aplicación cuenta con un backend de Machine Learning que expone una API y un frontend interactivo para realizar las predicciones.

## Demo en Vivo (Hugging Face Spaces 🤗)

Puedes probar la aplicación directamente en el siguiente enlace:

[Probar la demo en vivo](https://franco3030-heart-failure-prediction.hf.space/?__theme=system&deep_link=ipxpizTHR54)

## Tecnologías Utilizadas

- **Backend:** Python, FastAPI, Pandas, Scikit-learn, Joblib, Uvicorn
- **Frontend:** Gradio, Requests
- **Contenerización:** Docker

## Estructura del Proyecto

```
├── notebooks/
│   └── analysis.ipynb        # Entrenamiento y evaluacion del modelo
└── src/
    ├── backend/              # Lógica del modelo y la API
    |   ├── Dockerfile        # Define el entorno para ejecutar el backend
    │   ├── api.py            # Endpoint de la API (FastAPI)
    │   ├── model.py          # Carga del modelo y lógica de predicción
    │   ├── requirements.txt  # Dependencias del backend
    │   └── models/           # Modelos pre-entrenados
    └── frontend/
        └── app.py            # Interfaz de usuario (Gradio)
```

## Instalación y Uso

Existen dos formas de ejecutar este proyecto: utilizando Docker (recomendado) o de forma local.

### Opción 1: Ejecución con Docker (Recomendado)

Esta opción ejecuta el backend en un contenedor Docker.

1.  **Cambiamos de directorio al backend:**
    ```bash
    cd src/backend
    ```

2.  **Construir la imagen de Docker:**
    ```bash
    docker build -t heart-failure-predictor .
    ```

3.  **Ejecutar el contenedor:**
    ```bash
    docker run -p 8000:8000 heart-failure-predictor
    ```
    El backend estará disponible en `http://localhost:8000`.

### Opción 2: Ejecución Local

1.  **Clonar el repositorio (si aplica).**

2.  **Instalar dependencias del backend:**
    ```bash
    pip install -r src/backend/requirements.txt
    ```

3.  **Instalar dependencias del frontend:**
    ```bash
    pip install gradio requests
    ```

4.  **Ejecutar el backend:**
    Navega al directorio `src/backend` y ejecuta:
    ```bash
    uvicorn api:app --host 0.0.0.0 --port 8000
    ```

5.  **Ejecutar el frontend:**
    En una nueva terminal, ejecuta:
    ```bash
    python src/frontend/app.py
    ```
    La interfaz de Gradio se abrirá en tu navegador.

# Monitoreo y Versionado de Modelos

## 1. Monitoreo
El monitoreo debe realizarse en tres niveles:

1. **Modelo de Machine Learning**  
   - Seguimiento del rendimiento.  
   - Control de métricas y posibles sesgos.  

2. **Infraestructura**  
   - Estado de los servicios.  
   - Consumo de recursos y disponibilidad.  

3. **Valor para el negocio**  
   - Evaluar si los resultados generan impacto real.  
   - Usar los hallazgos para tomar decisiones estratégicas.  

## 2. Versionado
Para un control eficiente de versiones de modelos se recomienda utilizar herramientas de MLOps como:

- **MLflow**  
- **Databricks**  
- Otros sistemas de gestión de experimentos  

Estas plataformas permiten:  
- Registrar cada versión del modelo.  
- Comparar métricas entre iteraciones.  
- Reproducir experimentos y despliegues de manera confiable.


