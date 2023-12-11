# Usa una imagen base con Python y herramientas básicas
FROM python:3.8

# Instala las dependencias necesarias
RUN apt-get update && apt-get install -y \
    openslide-tools \
    && rm -rf /var/lib/apt/lists/*

# Instala una biblioteca de Python para trabajar con imágenes openslide
RUN pip install openslide-python

# Configura el directorio de trabajo
WORKDIR /app

# Copia el script de conversión
COPY convert.py /app/
COPY get_metadata.py /app/

# Define el comando por defecto al ejecutar el contenedor
CMD ["python", "get_metadata.py"]