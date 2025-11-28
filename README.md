# 🧠 Detección de Alzheimer con Deep Learning y Django

Este proyecto es una aplicación web diseñada para asistir en el diagnóstico temprano del Alzheimer mediante el análisis de imágenes de resonancia magnética (MRI). Utiliza un modelo de **Redes Neuronales Convolucionales (CNN)** entrenado con Deep Learning para clasificar imágenes entre pacientes sanos y pacientes con Alzheimer.

## 🚀 Características

*   **Interfaz Web Moderna:** Desarrollada con **Django** y **Bootstrap 5**, ofreciendo una experiencia de usuario limpia y responsiva.
*   **Análisis en Tiempo Real:** Carga una imagen MRI y obtén una predicción instantánea.
*   **Modelo de Deep Learning:** Implementado con **Keras Core** (backend Torch), capaz de identificar patrones visuales asociados a la enfermedad.
*   **Resultados Claros:** Muestra la clasificación ("Sano" o "Alzheimer") junto con el porcentaje de confianza del modelo.

## 🛠️ Tecnologías Utilizadas

*   **Backend:** Python, Django
*   **Inteligencia Artificial:** Keras Core, PyTorch, NumPy
*   **Procesamiento de Imágenes:** OpenCV
*   **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript

## 📋 Requisitos Previos

Asegúrate de tener instalado **Python 3.10+** en tu sistema.

## 🔧 Instalación y Uso

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/yisusrgg/Deteccion-Alzheimer.git
    cd Deteccion-Alzheimer
    ```

2.  **Crear y activar un entorno virtual (Opcional pero recomendado):**
    ```bash
    python -m venv venv
    # En Windows:
    .\venv\Scripts\activate
    # En Mac/Linux:
    source venv/bin/activate
    ```

3.  **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Entrenar el modelo (Si no tienes el archivo `.keras`):**
    *   Abre el notebook `entrenamiento.ipynb`.
    *   Ejecuta las celdas para entrenar la red neuronal.
    *   Al finalizar, se generará el archivo `alzheimer_model.keras`.

5.  **Ejecutar el servidor:**
    Asegúrate de estar en la carpeta donde se encuentra `manage.py` (dentro de la carpeta `alzheimer`):
    ```bash
    cd alzheimer
    python manage.py runserver
    ```

6.  **Usar la aplicación:**
    Abre tu navegador y visita: `http://127.0.0.1:8000/`

---
**Desarrollado por Jesus Rosiles González, Lizet Guadalupe López Medina, America Citlalli López Lemus, Paola Montserrat Ruiz Carmen**