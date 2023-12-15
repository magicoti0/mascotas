# Usa una imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo requirements.txt y luego instala las dependencias
RUN pip3 install pandas
RUN pip install Django

# Copia el resto de la aplicación al contenedor
COPY . .

# Comando para ejecutar la aplicación cuando el contenedor se inicia
CMD ["python", "manage.py", "runserver", "0.0.0.0:8090"]