# Clasificador de Estilos Artísticos con Deep Learning

Este repositorio contiene el código fuente y los recursos para el proyecto semestral de la asignatura **Introducción a Machine Learning y Deep Learning**. El objetivo del software es clasificar automáticamente obras de arte en 6 estilos distintos utilizando Redes Neuronales Convolucionales (CNN) y técnicas de *Transfer Learning*.

## Descripción del Proyecto

El sistema utiliza la arquitectura **ResNet50V2** pre-entrenada en ImageNet para extraer características visuales complejas y clasificar imágenes en los siguientes movimientos artísticos:
* Cubismo
* Expresionismo
* Impresionismo
* Realismo
* Pop_art
* Ukiyo-e

El proyecto implementa un flujo completo de Deep Learning, incluyendo preprocesamiento, *data augmentation*, entrenamiento con validación cruzada e inferencia.

## Instalación y Ejecución (Método Docker)

Este proyecto está encapsulado con Docker para garantizar su ejecución en cualquier entorno sin problemas de dependencias, cumpliendo con los estándares de reproducibilidad.

### Requisitos previos
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado y ejecutándose.
* Git.

### Pasos para ejecutar

1. **Clonar el repositorio:**
   Abre tu terminal y ejecuta:
   ```bash
   git clone https://github.com/AshCrow13/clasificador-arte-cnn.git
   cd clasificador-arte-cnn
   ```

2. **Configuración del Modelo Pre-entrenado:**
   * Si el archivo `.keras` (pesos del modelo) **NO** aparece en la lista de archivos (debido a limitaciones de tamaño de GitHub), descárgalo desde el enlace de Drive y colócalo en la carpeta raíz de este proyecto.
   * Nombre esperado del archivo: `temp_resnet50_finetuned.keras`.
   ```bash
   https://drive.google.com/drive/folders/1sGTRPdyV3Zd_NfSsiPML_idFO7p0NP1J?usp=sharing
   ```

3. **Construir la imagen de Docker:**
   En la terminal, dentro de la carpeta del proyecto:
   ```bash
   docker build -t clasificador-arte .
   ```

4. **Ejecutar el contenedor:**
   ```bash
   docker run -p 8888:8888 clasificador-arte
   ```

5. **Acceder al entorno:**
   Una vez que el contenedor arranque, verás en la terminal un enlace similar a:
   `http://127.0.0.1:8888/lab?token=...`
   
   Copia y pega ese enlace en tu navegador web. Se abrirá Jupyter Lab con todos los archivos del proyecto listos para usar.

## Estructura del Repositorio

### Archivos Principales (Solución Final)
* **`01proyecto_trata_datos.ipynb`**: Script de limpieza inicial del dataset WikiArt, selección de clases y balanceo de datos.
* **`02data_generators.ipynb`**: Configuración de los generadores de datos, partición estratificada (Train/Val/Test) y configuración de *Data Augmentation*.
* **`06Proyecto_Final_Ordenado.ipynb`**: **SCRIPT PRINCIPAL (FINAL)**. Contiene la implementación limpia y modular (patrón *Factory*) que compara arquitecturas y entrena el modelo ganador (ResNet50V2).
* **`07Script_inferencia.ipynb`**: Interfaz de uso para cargar el modelo entrenado y predecir el estilo de nuevas imágenes.

### Archivos de Experimentación e Investigación (Historial)
* **`03entrenamiento_modelo.ipynb`**: **Línea Base (Baseline)**. Implementación de una CNN personalizada (Custom CNN) entrenada desde cero. Sirvió para demostrar la dificultad de entrenar sin *Transfer Learning*.
* **`04Proyecto_Final.ipynb`**: **Iteración 1 (VGG19)**. Primera implementación exitosa utilizando *Transfer Learning* con la arquitectura VGG19.
* **`05Proyecto_Final_investigativo.ipynb`**: **Iteración 2 (ResNet50)**. Fase de investigación profunda con ResNet50. Los resultados superiores obtenidos aquí motivaron la refactorización del código hacia la versión final (`06`).

### Otros Archivos
* **`imagenes_prueba/`**: Imágenes de ejemplo para validación.
* **`Dockerfile`**: Configuración para la creación del contenedor.
* **`requirements.txt`**: Dependencias del proyecto.

## Cómo probar el modelo (Inferencia)

1. Abre el entorno Jupyter a través del enlace generado por Docker.
2. Abre el archivo `07Script_inferencia.ipynb`.
3. Ejecuta las celdas de carga de librerías y del modelo.
4. Utiliza la función de predicción con una imagen de la carpeta de pruebas:
   ```python
   # Ejemplo de uso dentro del notebook
   predecir_estilo('./imagenes_prueba/ejemplo_cubismo.jpg')
   ```

## Tecnologías Utilizadas
* **Lenguaje:** Python 3.10
* **Framework Deep Learning:** TensorFlow / Keras
* **Arquitectura Base:** ResNet50V2 (Transfer Learning)
* **Contenerización:** Docker

## Autor
**Omar Ignacio Castro González** Universidad del Bío-Bío  
Asignatura: Introducción a Machine Learning y Deep Learning
