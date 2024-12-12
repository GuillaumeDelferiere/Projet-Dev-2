import sqlite3
import os

# Connexion à la base de données (ou création si elle n'existe pas)
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Création de la table "affaire"
cursor.execute('''
CREATE TABLE IF NOT EXISTS affaire (
    id_affaire INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_affaire TEXT NOT NULL,
    type_crime TEXT NOT NULL,
    lieu TEXT NOT NULL,
    etat TEXT NOT NULL,
    date_ouverture DATE NOT NULL,
    enqueteur_assigne TEXT
)
''')

# Création de la table "preuve"
cursor.execute('''
CREATE TABLE IF NOT EXISTS preuve (
    id_preuve INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_preuve TEXT NOT NULL, 
    type_preuve TEXT NOT NULL,
    description TEXT, 
    lien TEXT, 
    lieu_collecte TEXT, 
    date_heure_decouverte DATE NOT NULL,
    resultat_analyse TEXT, 
    etat_actuel TEXT,
    scientifique_en_charge TEXT
)
''')

# Création de la table "rapport"
cursor.execute('''
CREATE TABLE IF NOT EXISTS rapport (
    id_rapport INTEGER PRIMARY KEY AUTOINCREMENT,
    id_affaire INTEGER NOT NULL,
    contenu TEXT NOT NULL,
    date_creation DATE NOT NULL,
    FOREIGN KEY (id_affaire) REFERENCES affaire(id_affaire)
)
''')

# Validation des modifications et fermeture de la connexion
conn.commit()
conn.close()

print("Base de données et tables créées avec succès !")