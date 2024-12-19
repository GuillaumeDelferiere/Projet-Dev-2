import sqlite3
import os

class PreuveManager:
    def __init__(self, db_name='database.db'):
        self.db_path = self.get_database_path(db_name)
        self.ensure_database_exists()

    def get_database_path(self, db_name):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(script_dir, db_name)

    def ensure_database_exists(self):
        if not os.path.exists(self.db_path):
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS preuve (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom_preuve TEXT,
                    type_preuve TEXT,
                    description TEXT,
                    lien TEXT,
                    lieu_collecte TEXT,
                    date_heure_decouverte TEXT,
                    resultat_analyse TEXT,
                    etat_actuel TEXT,
                    scientifique_en_charge TEXT
                )
            ''')
            conn.commit()
            conn.close()

    def add_preuve(self, nom):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO preuve (nom_preuve, type_preuve, description, lien, lieu_collecte, date_heure_decouverte, resultat_analyse, etat_actuel, scientifique_en_charge)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (nom, '', '', '', '', '2023-01-01', '', '', ''))
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            raise Exception(f"Erreur lors de l'ajout dans la base de données : {e}")