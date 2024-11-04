from ultralytics import YOLO
import os
import cv2
from PIL import Image
import numpy as np

# Cargar el modelo de segmentación YOLO
model = YOLO('yolov8x-seg.pt')  # Cargar un modelo de segmentación YOLO preentrenado

# Especificar la ruta a la carpeta de imágenes
ruta_imagenes = 'imagenesMio'  # Cambia esto por la ruta de tu carpeta de imágenes

# Generar la lista de imágenes del 1 al 40, asegurando que sean solo .jpg
image_paths = []
for i in range(1, 20):
    image_path = os.path.join(ruta_imagenes, f'{i}.jpg')
    if os.path.isfile(image_path):  # Verificar si el archivo existe
        image_paths.append(image_path)  # Añadir la ruta a la lista si el archivo existe

# Predecir en cada imagen
for image_path in image_paths:
    # Cargar la imagen original
    original_image = cv2.imread(image_path)
    original_height, original_width = original_image.shape[:2]
    
    # Realizar la predicción
    results = model.predict(source=image_path, save=False, conf=0.5)  # Ajusta el nivel de confianza si es necesario
    
    for result in results:
        # Verificar si existen máscaras en el resultado
        if result.masks is not None and len(result.masks.data) > 0:
            # Obtener la máscara de segmentación como un array binario
            mask = result.masks.data[0].cpu().numpy()  # Asumimos una sola máscara por simplicidad
            mask = (mask * 255).astype(np.uint8)  # Convertir a escala de 0-255
            
            # Redimensionar la máscara para que coincida con el tamaño de la imagen original
            mask_resized = cv2.resize(mask, (original_width, original_height), interpolation=cv2.INTER_NEAREST)
            
            # Dibujar el cuadro de color alrededor del área segmentada (asumiendo detección de bus)
            x, y, w, h = cv2.boundingRect(mask_resized)  # Calcular el cuadro delimitador de la máscara
            color = (0, 255, 0)  # Color del cuadro (verde, en este caso)
            thickness = 3  # Grosor del cuadro
            original_with_box = original_image.copy()
            cv2.rectangle(original_with_box, (x, y), (x + w, y + h), color, thickness)
            
            # Convertir el área segmentada a escala de grises
            grayscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
            grayscale_image = cv2.cvtColor(grayscale_image, cv2.COLOR_GRAY2BGR)  # Convertir a BGR para fusionar

            # Crear una imagen de salida donde el área segmentada está en escala de grises
            output_image = np.where(mask_resized[..., None] == 255, grayscale_image, original_with_box)

            # Mostrar o guardar la imagen de salida
            output_pil = Image.fromarray(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
            output_pil.show()
        else:
            print(f"No se detectaron objetos en la imagen {image_path}")
