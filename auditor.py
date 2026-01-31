import os
import shutil

def analyze_logs(filepath):
    print(f"--- Analyse du fichier : {filepath} ---")
    
    count = 0

    try:

        with open(filepath, 'r') as f:
            for line in f:
                if "ERROR" in line or "CRITICAL" in line:
                    count = count + 1
                    print(f"Alerte détectée : {line.strip()}")
                    
    except FileNotFoundError:
        
        print(f"ERREUR CRITIQUE : Le fichier '{filepath}' est introuvable !")
        return 0 

    return count


def move_to_archive(filepath):
    
    archive_dir = "archives"
    
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
    
    
    print(f" Déplacement de {filepath} vers {archive_dir}...")
    shutil.move(filepath, archive_dir)

if __name__ == "__main__":
    nombre_erreurs= analyze_logs("server.log")

    print(f"Analyse terminée. Nombre d'erreurs trouvées : {nombre_erreurs}")

    move_to_archive("server.log")
	
