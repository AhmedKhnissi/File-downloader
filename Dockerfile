#image officielle de Python
FROM python:3.12-slim
#définition du répertoire de travail
WORKDIR /app
#copie les fichiers du projet
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
#exposition fdu port utilisé par Flask
EXPOSE 5000
#démarrage Flask
CMD ["python", "app.py"]
