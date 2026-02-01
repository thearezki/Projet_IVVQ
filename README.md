# System Log Auditor

Un outil d'automatisation conçu pour surveiller, analyser et archiver les journaux systèmes (logs).
Le projet inclut une chaîne d'intégration continue (Tests Unitaires) et une conteneurisation complète.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?logo=docker&logoColor=white)
![Status](https://img.shields.io/badge/Status-Stable-green)

## Fonctionnalités

Ce projet démontre une approche DevOps appliquée à l'administration système :

* **Analyse Automatisée :** Détection des patterns critiques (`[ERROR]`, `[CRITICAL]`) via lecture de flux.
* **Conteneurisation (Docker) :** Exécution isolée et reproductible (Sandbox) via un `Dockerfile` optimisé.
* **Robustesse :** Gestion des exceptions (I/O, Permissions) et nettoyage automatique.
* **Archivage :** Rotation automatique des logs traités vers `/archives`.
* **Qualité Code (IVVQ) :** Validé par une suite de tests unitaires (`pytest`).

## Installation & Utilisation

### 1. Récupérer le projet
```bash
git clone git@github.com:thearezki/Projet_IVVQ.git
cd Projet_IVVQ
```
2. Générer des données de test
Créez un faux fichier log pour simuler l'activité du serveur :

```Bash
echo "2024-02-01 [INFO] Service started" > server.log
echo "2024-02-01 [ERROR] Database connection failed" >> server.log
echo "2024-02-01 [CRITICAL] System Overheat" >> server.log
```
Option A : Lancement via Docker (Recommandé)
Cette méthode ne nécessite pas d'installer Python sur votre machine.

1. Construire l'image

```Bash
docker build -t log-auditor .
```
2. Lancer l'analyseur

```Bash
docker run log-auditor
```
Le script s'exécutera dans un conteneur isolé.

Option B : Lancement classique (Python)
Pré-requis : Python 3.x installé.

```Bash
python3 auditor.py
```
Tests Unitaires
Pour valider le bon fonctionnement du code (IVVQ) :

```Bash
pip install pytest
pytest
```
Auteur
Arezki - Projet Portfolio DevOps
