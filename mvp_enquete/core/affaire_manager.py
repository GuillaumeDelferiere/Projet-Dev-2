import sqlite3
from .database import get_database_path

class AffaireManager:
    def __init__(self, db_name='database.db'):
        self.db_path = get_database_path(db_name)

    def get_all_affaires(self):
        try:
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
        except sqlite3.Error as e:
            raise Exception(f"Erreur lors de la récupération des affaires: {e}")

    def add_affaire(self, nom, type_crime, lieu, statut, date_ouverture):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO affaire (nom_affaire, type_crime, lieu, etat, date_ouverture)
                VALUES (?, ?, ?, ?, ?)
            ''', (nom, type_crime, lieu, statut, date_ouverture))
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            raise Exception(f"Erreur lors de l'ajout de l'affaire: {e}")

    def update_affaire(self, index, nom, type_crime, lieu, statut, date_ouverture):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE affaire
                SET nom_affaire = ?, type_crime = ?, lieu = ?, etat = ?, date_ouverture = ?
                WHERE id_affaire = ?
            ''', (nom, type_crime, lieu, statut, date_ouverture, index + 1))
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            raise Exception(f"Erreur lors de la mise à jour de l'affaire: {e}")

    def delete_affaire(self, index):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('DELETE FROM affaire WHERE id_affaire = ?', (index + 1,))
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            raise Exception(f"Erreur lors de la suppression de l'affaire: {e}")

    def search(self, query):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                SELECT nom_affaire FROM affaire
                WHERE LOWER(nom_affaire) LIKE ? OR LOWER(type_crime) LIKE ? OR LOWER(lieu) LIKE ?
            ''', (f'%{query}%', f'%{query}%', f'%{query}%'))
            resultats = [row[0] for row in cursor.fetchall()]
            conn.close()
            return resultats
        except sqlite3.Error as e:
            raise Exception(f"Erreur lors de la recherche des affaires: {e}")