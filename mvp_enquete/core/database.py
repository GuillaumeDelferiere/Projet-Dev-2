import sqlite3
import os

def get_database_path(db_name='database.db'):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, db_name)

def create_tables():
    db_path = get_database_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

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

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS rapport (
        id_rapport INTEGER PRIMARY KEY AUTOINCREMENT,
        id_affaire INTEGER NOT NULL,
        contenu TEXT NOT NULL,
        date_creation DATE NOT NULL,
        FOREIGN KEY (id_affaire) REFERENCES affaire(id_affaire)
    )
    ''')

    conn.commit()
    conn.close()