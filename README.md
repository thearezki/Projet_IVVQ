# System Log Auditor

Un outil d'automatisation Python conçu pour surveiller, analyser et archiver les journaux systèmes (logs) d'un serveur Linux.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat)
![Status](https://img.shields.io/badge/Status-Stable-green)

## Fonctionnalités

Ce script automatise les tâches quotidiennes d'un Administrateur Système :

* **Analyse Intelligente :** Lecture fichier ligne par ligne pour détecter les mots-clés `[ERROR]` et `[CRITICAL]`.
* **Robustesse :** Gestion des exceptions (fichiers manquants) via des blocs `try/except` pour éviter les crashs.
* **Archivage Automatique :** Déplacement automatique des logs traités vers un dossier `/archives` pour garder la racine propre (module `shutil`).
* **Qualité Code (IVVQ) :** Validé par des tests unitaires automatisés avec `pytest`.

## Installation & Utilisation

### 1. Installation
```bash
git clone git@github.com:thearezki/Projet_IVVQ.git
cd Projet_IVVQ
```
2. Simuler des logs (Génération de données)
Si vous n'avez pas de fichier log sous la main, créez-en un avec cette commande :

```Bash
echo "2024-10-01 [INFO] Service started" > server.log
echo "2024-10-01 [ERROR] Database connection failed" >> server.log
echo "2024-10-01 [CRITICAL] System Overheat" >> server.log
```
3. Lancer l'analyseur
```Bash
python3 auditor.py
```
Le script affichera le nombre d'erreurs détectées et déplacera le fichier dans le dossier archives/.

Tests Unitaires
Pour vérifier la fiabilité du code (IVVQ), lancez la suite de tests :

```Bash
pytest
```
Auteur
Arezki - Projet Portfolio DevOps / Python





