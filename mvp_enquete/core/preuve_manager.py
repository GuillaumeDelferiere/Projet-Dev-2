import sqlite3
from .database import get_database_path

class PreuveManager:
    def __init__(self, db_name='database.db'):
        self.db_path = get_database_path(db_name)

    def add_preuve(self, nom, type_preuve, description, lien, lieu_collecte, date_heure_decouverte, resultat_analyse, etat_actuel, scientifique_en_charge):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO preuve (nom_preuve, type_preuve, description, lien, lieu_collecte, date_heure_decouverte, resultat_analyse, etat_actuel, scientifique_en_charge)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (nom, type_preuve, description, lien, lieu_collecte, date_heure_decouverte, resultat_analyse, etat_actuel, scientifique_en_charge))
        conn.commit()
        conn.close()

    def get_all_preuves(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT nom_preuve, type_preuve, description, lien, lieu_collecte, date_heure_decouverte, resultat_analyse, etat_actuel, scientifique_en_charge FROM preuve')
        preuves = [
            {
                "nom": row[0],
                "type_preuve": row[1],
                "description": row[2],
                "lien": row[3],
                "lieu_collecte": row[4],
                "date_heure_decouverte": row[5],
                "resultat_analyse": row[6],
                "etat_actuel": row[7],
                "scientifique_en_charge": row[8]
            }
            for row in cursor.fetchall()
        ]
        conn.close()
        return preuves

    def update_preuve(self, index, nom, type_preuve, description, lien, lieu_collecte, date_heure_decouverte, resultat_analyse, etat_actuel, scientifique_en_charge):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE preuve
            SET nom_preuve = ?, type_preuve = ?, description = ?, lien = ?, lieu_collecte = ?, date_heure_decouverte = ?, resultat_analyse = ?, etat_actuel = ?, scientifique_en_charge = ?
            WHERE id_preuve = ?
        ''', (nom, type_preuve, description, lien, lieu_collecte, date_heure_decouverte, resultat_analyse, etat_actuel, scientifique_en_charge, index + 1))
        conn.commit()
        conn.close()

    def delete_preuve(self, index):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM preuve WHERE id_preuve = ?', (index + 1,))
        conn.commit()
        conn.close()

    def search(self, query):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT nom_preuve FROM preuve
            WHERE LOWER(nom_preuve) LIKE ? OR LOWER(type_preuve) LIKE ? OR LOWER(description) LIKE ?
        ''', (f'%{query}%', f'%{query}%', f'%{query}%'))
        resultats = [row[0] for row in cursor.fetchall()]
        conn.close()
        return resultats