# Usa la imagen base de Python
FROM python:3.9

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos necesarios
COPY locustfile.py .

# Instala las dependencias
RUN pip install locust

# Comando para iniciar la prueba con Locust
CMD ["locust", "-f", "locustfile.py"]
