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
    contenu TEXT NOT NULL
)
''')

# Création de la table Suspects
cursor.execute('''
CREATE TABLE IF NOT EXISTS suspects (
    id_suspects INTEGER PRIMARY KEY AUTOINCREMENT,
    enquete_id INTEGER NOT NULL,
    nom_suspects TEXT, 
    prenom_suspects TEXT,
    surnom TEXT,
    age INTEGER,
    date_naissance DATE,
    lieu_naissance TEXT,
    adresse TEXT,
    taille INTEGER,
    poids INTEGER,
    signes_particuliers TEXT,
    role TEXT,
    alibi_declare TEXT,
    FOREIGN KEY (enquete_id) REFERENCES enquete(id)
)
''')

# Création de la table Témoin
cursor.execute('''
CREATE TABLE IF NOT EXISTS temoin (
    id_temoin INTEGER PRIMARY KEY AUTOINCREMENT,
    enquete_id INTEGER NOT NULL,
    nom_temoin TEXT,
    prenom_temoin TEXT,
    age INTEGER, 
    date_temoignage DATE,
    temoignage TEXT,
    adresse TEXT,
    numero_telephone TEXT
)
''')

# Validation des modifications et fermeture de la connexion
conn.commit()
conn.close()

print("Base de données et tables créées avec succès !")