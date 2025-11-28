import os
os.environ["KERAS_BACKEND"] = "torch"
import keras_core as keras
import cv2
import numpy as np
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from pathlib import Path

MODEL_PATH = Path(settings.BASE_DIR).parent / 'alzheimer_model.keras'
model = None

def load_model():
    global model
    if model is None and MODEL_PATH.exists():
        try:
            model = keras.models.load_model(MODEL_PATH)
            print("Modelo cargado exitosamente")
        except Exception as e:
            print(f"Error al cargar modelo: {e}")

def home(request):
    return render(request, 'Examen/index.html')

def predict(request):
    if request.method == 'POST' and request.FILES.get('file'):
        load_model()
        if model is None:
            return JsonResponse({'error': 'Modelo no encontrado. Ejecuta el notebook primero.'})
        
        try:
            file = request.FILES['file']
            file_bytes = np.frombuffer(file.read(), np.uint8)
            img = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)
            
            # Preprocesamiento
            img = cv2.resize(img, (250, 250), cv2.INTER_AREA)
            img = img / 255.0
            img = np.expand_dims(img, axis=0)
            img = np.expand_dims(img, axis=-1)

            prediction = model.predict(img)
            score = prediction[0][0]
            
            result = "Sano" if score > 0.5 else "Alzheimer"
            confidence = score if score > 0.5 else 1 - score
            
            return JsonResponse({
                'prediction': result,
                'confidence': float(confidence)
            })
        except Exception as e:
            return JsonResponse({'error': str(e)})
            
    return JsonResponse({'error': 'Petición inválida'})