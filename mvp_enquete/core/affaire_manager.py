import sqlite3
from .database import get_database_path

class AffaireManager:
    def __init__(self, db_name='database.db'):
        self.db_path = get_database_path(db_name)

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
            WHERE id_affaire = ?
        ''', (nom, type_crime, lieu, statut, date_ouverture, index + 1))
        conn.commit()
        conn.close()

    def delete_affaire(self, index):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM affaire WHERE id_affaire = ?', (index + 1,))
        conn.commit()
        conn.close()

    def search(self, query):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT nom_affaire FROM affaire
            WHERE LOWER(nom_affaire) LIKE ? OR LOWER(type_crime) LIKE ? OR LOWER(lieu) LIKE ?
        ''', (f'%{query}%', f'%{query}%', f'%{query}%'))
        resultats = [row[0] for row in cursor.fetchall()]
        conn.close()
        return resultats