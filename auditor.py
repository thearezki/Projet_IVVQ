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
if __name__ == "__main__":
    analyze_logs("server.log")
