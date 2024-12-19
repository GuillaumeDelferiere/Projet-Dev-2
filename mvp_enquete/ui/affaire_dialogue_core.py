# core.py
import sqlite3
import os
import os.path

class AffaireManager:
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
                CREATE TABLE IF NOT EXISTS affaire (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom_affaire TEXT,
                    type_crime TEXT,
                    lieu TEXT,
                    etat TEXT,
                    date_ouverture TEXT
                )
            ''')
            conn.commit()
            conn.close()

    def get_all_affaires(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT nom_affaire, type_crime, lieu, etat, date_ouverture FROM affaire')
        affaires = [
            {
                "nom": row[0],
                "type_crime": row[1],
                "lieu": row[2],
                "statut": row[3],
                "date_ouverture": row[4]
            }
            for row in cursor.fetchall()
        ]
        conn.close()
        return affaires

    def add_affaire(self, nom, type_crime, lieu, statut, date_ouverture):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO affaire (nom_affaire, type_crime, lieu, etat, date_ouverture)
            VALUES (?, ?, ?, ?, ?)
        ''', (nom, type_crime, lieu, statut, date_ouverture))
        conn.commit()
        conn.close()

    def update_affaire(self, index, nom, type_crime, lieu, statut, date_ouverture):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE affaire
            SET nom_affaire = ?, type_crime = ?, lieu = ?, etat = ?, date_ouverture = ?
            WHERE id = ?
        ''', (nom, type_crime, lieu, statut, date_ouverture, index + 1))
        conn.commit()
        conn.close()

    def delete_affaire(self, index):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM affaire WHERE id = ?', (index + 1,))
        conn.commit()
        conn.close()

