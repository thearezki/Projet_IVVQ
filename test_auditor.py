import os
from auditor import analyze_logs

def test_detection_erreurs():
  
    fichier_test = "test_temp.log"
    # création d' un fichier avec exactement 2 erreurs
    with open(fichier_test, "w") as f:
        f.write("[INFO] Tout va bien\n")
        f.write("[ERROR] Une erreur ici\n")  
        f.write("[WARNING] Attention...\n")
        f.write("[CRITICAL] Gros problème !\n") 
    
    #  2. ACTION (Exécution)

    nb_erreurs = analyze_logs(fichier_test)
    
    #  3. Nettoyage

    os.remove(fichier_test)

    # 4. ASSERT (Validation) 
    assert nb_erreurs == 2
