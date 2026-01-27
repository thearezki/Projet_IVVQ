def analyze_logs(filepath):
    print(f"--- Analyse du fichier : {filepath} ---")
    
    
    count = 0

    with open(filepath, 'r') as f:
        for line in f:
            if "ERROR" in line:

                count = count + 1
                print(f"Alerte détectée : {line.strip()}")
    
    print(f"Analyse terminée. Nombre d'erreurs trouvées : {count}")

if __name__ == "__main__":
    analyze_logs("server.log")
