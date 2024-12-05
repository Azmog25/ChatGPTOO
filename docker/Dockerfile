# Utiliser une image Python officielle
FROM python:3.12-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier requirements.txt depuis le contexte
COPY requirements.txt ./requirements.txt

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier tous les fichiers du projet dans le conteneur
COPY . .

# Exposer le port 8000 pour Django
EXPOSE 8000

# Commande par défaut pour démarrer le serveur
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
