# Utilise une image officielle de Python
FROM python:3.12-slim

# Définit le répertoire de travail
WORKDIR /app

# Copie les fichiers de ton projet
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose le port utilisé par Flask
EXPOSE 5000

# Commande pour démarrer Flask
CMD ["python", "app.py"]
