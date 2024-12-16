import unittest
import sqlite3
import os
from ui.preuve_dialog import PreuveDialog
from ui.main_window import MainWindow
from ui.affaire_dialog import AffaireDialog
from utils.export_pdf import generer_pdf

class TestPreuveDialog(unittest.TestCase):
    def setUp(self):
        self.dialog = PreuveDialog([])
        self.db_path = self.dialog.get_database_path('test_database.db')
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS preuve (
                id_preuve INTEGER PRIMARY KEY AUTOINCREMENT,
                nom_preuve TEXT NOT NULL,
                type_preuve TEXT,
                description TEXT,
                lien TEXT,
                lieu_collecte TEXT,
                date_heure_decouverte DATE,
                resultat_analyse TEXT,
                etat_actuel TEXT,
                scientifique_en_charge TEXT
            )
        ''')
        self.conn.commit()

    def tearDown(self):
        self.conn.close()
        os.remove(self.db_path)

    def test_ajouter_preuve_db(self):
        self.dialog.ajouter_preuve_db('Empreinte digitale')
        self.cursor.execute('SELECT nom_preuve FROM preuve WHERE nom_preuve = ?', ('Empreinte digitale',))
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[0], 'Empreinte digitale')

class TestMainWindow(unittest.TestCase):
    def setUp(self):
        self.window = MainWindow()
        self.db_path = self.window.get_database_path('test_database.db')
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
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
        self.cursor.execute('''
            INSERT INTO affaire (nom_affaire, type_crime, lieu, etat, date_ouverture)
            VALUES ('Affaire 1', 'Vol', 'Paris', 'Ouverte', '2023-01-01')
        ''')
        self.conn.commit()

    def tearDown(self):
        self.conn.close()
        os.remove(self.db_path)

    def test_charger_affaires(self):
        self.window.charger_affaires()
        self.assertEqual(len(self.window.affaires), 1)
        self.assertEqual(self.window.affaires[0]['nom'], 'Affaire 1')

    def test_get_database_path(self):
        db_path = self.window.get_database_path('test_database.db')
        self.assertTrue(os.path.isabs(db_path))
        self.assertTrue(db_path.endswith('test_database.db'))

class TestAffaireDialog(unittest.TestCase):
    def setUp(self):
        self.dialog = AffaireDialog([])
        self.db_path = self.dialog.get_database_path('test_database.db')
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
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
        self.conn.commit()

    def tearDown(self):
        self.conn.close()
        os.remove(self.db_path)

    def test_ajouter_affaire_db(self):
        self.dialog.ajouter_affaire_db('Affaire 2', 'Meurtre', 'Lyon', 'En cours', '2023-02-01')
        self.cursor.execute('SELECT nom_affaire FROM affaire WHERE nom_affaire = ?', ('Affaire 2',))
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[0], 'Affaire 2')

class TestExportPDF(unittest.TestCase):
    def test_generer_pdf(self):
        affaires = [
            {"nom": "Affaire 1", "type_crime": "Vol", "lieu": "Paris", "statut": "Ouverte", "date_ouverture": "2023-01-01"},
            {"nom": "Affaire 2", "type_crime": "Meurtre", "lieu": "Lyon", "statut": "En cours", "date_ouverture": "2023-02-01"}
        ]
        generer_pdf(affaires)
        self.assertTrue(os.path.exists("rapport_affaires.pdf"))
        os.remove("rapport_affaires.pdf")

if __name__ == '__main__':
    unittest.main()