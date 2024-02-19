# Usa una imagen base con Python y herramientas básicas
FROM python:3.8

# Configura la variable de entorno PYTHONUNBUFFERED
ENV PYTHONUNBUFFERED=1

# Instala las dependencias necesarias
RUN apt-get update && apt-get install -y \
    openslide-tools \
    && rm -rf /var/lib/apt/lists/*

# Instala una biblioteca de Python para trabajar con imágenes openslide
RUN pip install openslide-python

# Instala una biblioteca de Python para mostrar barras de progreso
RUN pip install tqdm

# Configura el directorio de trabajo
WORKDIR /app

# Copia el script de conversión
COPY convert.py /app/
COPY get_metadata.py /app/

# Define el comando por defecto al ejecutar el contenedor
CMD ["python", "convert.py"]

### Correr estos dos comandos para hacer funcionar el contenedor
# docker build -t svs-to-png-converter .
# docker run -v C:/Users/achav/Documents/OA:/app/data svs-to-png-converter
