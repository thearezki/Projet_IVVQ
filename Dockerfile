# 1. On part d'une version officielle de Python (légère : "slim")
FROM python:3.11-slim

# 2. On définit le dossier de travail dans le conteneur
WORKDIR /app

# 3. On copie tout mon dossier actuel (PC) vers le dossier /app (mon Conteneur)
COPY . .

# 4. La commande à lancer quand le conteneur démarre
CMD ["python", "auditor.py"]
