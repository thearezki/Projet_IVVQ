def analyze_logs(filepath):
    print(f"--- Analyse du fichier : {filepath} ---")
    
    with open(filepath, 'r') as f:
        
        for line in f: 
            print(line.strip())

if __name__ == "__main__":
    analyze_logs("server.log")
