import json

def sauvegarder_donnees(fichier, donnees):
    with open(fichier, "w") as f:
        json.dump(donnees, f)

def charger_donnees(fichier):
    try:
        with open(fichier, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
