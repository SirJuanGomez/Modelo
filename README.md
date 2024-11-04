# Segmentación de Imágenes del Sistema MIO utilizando YOLOv8x

## Descripción del Proyecto

Este proyecto se centra en la segmentación de imágenes de los vehículos articulados del sistema de transporte masivo MIO en la ciudad de Cali. Usando el modelo de segmentación YOLOv8x, se detecta el vehículo en cada imagen y se aplica un filtro visual que convierte el articulado a escala de grises, mientras que se genera un recuadro verde alrededor de él para destacarlo.

Este proyecto es ideal para:
- Investigadores y desarrolladores interesados en técnicas de visión por computadora aplicadas a sistemas de transporte urbano.
- Aquellos que buscan mejorar la identificación visual de vehículos en entornos urbanos.
## Agradecimientos

- [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
- [Awesome README](https://github.com/matiassingers/awesome-readme)
- [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)

## Apéndice

### Información Adicional

- **Datos de Entrenamiento:** Este modelo fue entrenado utilizando un conjunto de datos específico de imágenes del sistema MIO. Se recomienda usar imágenes con buena iluminación y ángulos variados para mejorar la precisión del modelo.

- **Implementación Técnica:** El modelo YOLOv8x se ha implementado utilizando la biblioteca [Ultralytics YOLO](https://github.com/ultralytics/yolov5) y se basa en un marco de trabajo de aprendizaje profundo. Asegúrate de tener las dependencias necesarias instaladas.

- **Posibles Mejoras Futuras:**
  - Integrar un sistema de retroalimentación para mejorar la precisión del modelo basado en imágenes no detectadas correctamente.
  - Implementar un sistema en tiempo real que permita la segmentación de imágenes de video en directo.

- **Notas de Uso:** Asegúrate de seguir las instrucciones de instalación y uso proporcionadas en la sección correspondiente del README para evitar errores durante la ejecución del modelo.

## Autores

- [Juan Gomez](https://github.com/SirJuanGomez) - Desarrollador principal y creador del proyecto.
- [@octokatherine](https://www.github.com/octokatherine) - Contribuciones y soporte en la documentación.
## Badges

Agrega insignias de algún lugar como: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Status](https://img.shields.io/badge/status-active-brightgreen.svg)](https://github.com/SirJuanGomez/Modelo)
## Color Reference

| Color          | Hex                                                                |
| -------------- | ------------------------------------------------------------------ |
| Gris           | ![#808080](https://via.placeholder.com/10/808080?text=+) #808080    |
| Verde          | ![#00b48a](https://via.placeholder.com/10/00b48a?text=+) #00b48a    |
| Blanco         | ![#ffffff](https://via.placeholder.com/10/ffffff?text=+) #ffffff    |
| Negro          | ![#000000](https://via.placeholder.com/10/000000?text=+) #000000    |
## Contributing

¡Las contribuciones son siempre bienvenidas!

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. **Forkea el repositorio:** Haz un fork del proyecto en tu propia cuenta de GitHub.
2. **Crea una rama:** Crea una nueva rama para tu característica o corrección de errores.
   ```bash
   git checkout -b nombre-de-tu-rama
## Documentación

Este proyecto utiliza varias bibliotecas y herramientas para la segmentación de imágenes. A continuación, se presentan detalles sobre las principales tecnologías utilizadas:

### Tecnologías y Bibliotecas

- **Python:** El lenguaje de programación utilizado para el desarrollo del proyecto.
- **YOLOv8x:** Modelo de machine learning para la segmentación de imágenes, utilizado para identificar y segmentar el articulado gris del sistema MIO en Cali. Más información en [YOLO](https://github.com/ultralytics/yolov8).
- **Pillow:** Biblioteca de Python para la manipulación de imágenes, utilizada para procesar las imágenes y aplicar filtros.
- **OpenCV:** Biblioteca de visión por computadora que se utiliza para la carga de imágenes, procesamiento y visualización de resultados.
- **NumPy:** Biblioteca para el cálculo numérico en Python, utilizada para manejar arrays y realizar operaciones matemáticas en matrices de imágenes.

### Uso

Para obtener más información sobre cómo utilizar este proyecto y sus funcionalidades, consulta el archivo README del repositorio.
## Características


- **Segmentación en Tiempo Real:** Utiliza un   modelo de segmentación YOLOv8x para identificar y segmentar el articulado gris del sistema MIO en imágenes de la ciudad de Cali.

- **Filtro de Escala de Grises:** Aplica un filtro que convierte el área segmentada a escala de grises mientras mantiene el resto de la imagen en color.

- **Cuadro de Detección:** Dibuja un recuadro verde alrededor del área segmentada para facilitar la visualización.

- **Compatibilidad Multiplataforma:** Funciona en cualquier sistema operativo que soporte Python y las bibliotecas requeridas.
## 🚀 Sobre Mí

Soy estudiante de ingeniería en electrónica y un entusiasta de todo lo relacionado con la tecnología. Desde los circuitos hasta la electricidad ⚡, disfruto explorando cómo funcionan las cosas y creando proyectos innovadores. Además, soy un apasionado de los videojuegos, lo que me motiva a combinar mi amor por el juego con mi formación técnica.

Formo parte de un capítulo de IEEE, donde tengo la oportunidad de conectar con otros aficionados y profesionales, participar en eventos interesantes y aprender sobre las últimas tendencias en ingeniería. Siempre estoy buscando nuevas formas de expandir mis habilidades y contribuir a proyectos que marquen la diferencia.

¡Sigue mi viaje mientras sigo aprendiendo y creando!
## Instalación

Para instalar este proyecto, sigue los siguientes pasos:

1. Clona el repositorio en tu máquina local:
   ```bash
   git clone https://github.com/SirJuanGomez/Modelo.git
## FAQ

#### ¿Qué es YOLO y cómo se utiliza en este proyecto?
YOLO (You Only Look Once) es un modelo de detección de objetos en tiempo real que permite segmentar y clasificar diferentes objetos dentro de una imagen. En este proyecto, utilizamos YOLOv8x para segmentar el articulado del sistema MIO de la ciudad de Cali y resaltar áreas específicas.

#### ¿Qué bibliotecas son necesarias para ejecutar este proyecto?
Para ejecutar este proyecto, necesitas tener instaladas las siguientes bibliotecas:
- `ultralytics` para el modelo YOLO.
- `opencv-python` para la manipulación de imágenes.
- `Pillow` para trabajar con imágenes en Python.
- `numpy` para operaciones numéricas.

#### ¿Cómo puedo contribuir al proyecto?
Las contribuciones son bienvenidas. Puedes abrir un problema o enviar una solicitud de extracción (pull request) en GitHub. Asegúrate de seguir el código de conducta y proporcionar una descripción clara de tu contribución.
## Variables de Entorno

Para ejecutar este proyecto, necesitarás agregar las siguientes variables de entorno a tu archivo `.env`:

- `MODEL_PATH`: La ruta al modelo de YOLO que utilizarás para la segmentación. Por ejemplo, `yolov8x-seg.pt`.
- `DATA_PATH`: La ruta al archivo de configuración de datos que se necesita para entrenar el modelo. Por ejemplo, `coco8.yaml`.
