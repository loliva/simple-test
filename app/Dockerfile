# Usa la imagen base de Python
FROM python:3.9

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos necesarios
COPY app.py .

# Instala las dependencias
RUN pip install flask

# Expone el puerto donde se ejecuta la API
EXPOSE 5050

# Comando para iniciar el servidor
CMD ["python", "app.py"]
