from ultralytics import YOLO

# Definir el modelo y los datos
model_path = 'yolo11n.pt'
data_path = 'coco8.yaml'

# Cargar el modelo
model = YOLO(model_path)

# Entrenar el modelo
model.train(data=data_path)  # Entrenamiento del modelo con los datos especificados
