def analyze_logs(filepath):
    print(f"--- Analyse du fichier : {filepath} ---")
    
    count = 0

    with open(filepath, 'r') as f:
        for line in f:
            if "ERROR" in line or "CRITICAL" in line:
                count = count + 1
                print(f"Alerte détectée : {line.strip()}")

    return count

if __name__ == "__main__":

    nombre_erreurs = analyze_logs("server.log")

    print(f"Analyse terminée. Nombre d'erreurs trouvées : {nombre_erreurs}")
