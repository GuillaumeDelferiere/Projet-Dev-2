from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox, QInputDialog, QLineEdit, QListWidget, QDialog, QVBoxLayout, QLabel
import sys
from PyQt5.QtWidgets import QApplication
from fpdf import FPDF
from ui.affaire_dialog import AffaireDialog  # Importer la fenêtre de dialogue pour les affaires
from ui.preuve_dialog import PreuveDialog  # Importer la nouvelle fenêtre de dialogue pour les preuves
import sqlite3
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestion des Affaires Criminelles")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.btn_affaires = QPushButton("Gérer les Affaires")
        self.btn_preuves = QPushButton("Gérer les Preuves")
        self.btn_rapport = QPushButton("Générer un Rapport")

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Rechercher une affaire ou une preuve")
        self.search_button = QPushButton("Rechercher")

        layout.addWidget(self.search_input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.btn_affaires)
        layout.addWidget(self.btn_preuves)
        layout.addWidget(self.btn_rapport)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Listes pour stocker les affaires et les preuves
        self.affaires = []
        self.preuves = {}  # Dictionnaire pour stocker les preuves par affaire

        # Charger les affaires et les preuves depuis la base de données
        self.charger_affaires()
        self.charger_preuves()

        # Connecter les boutons aux méthodes
        self.btn_affaires.clicked.connect(self.gerer_affaires)
        self.btn_preuves.clicked.connect(self.gerer_preuves)
        self.btn_rapport.clicked.connect(self.generer_rapport)
        self.search_button.clicked.connect(self.rechercher)

    def charger_affaires(self):
        try:
            conn = sqlite3.connect(self.get_database_path())
            cursor = conn.cursor()
            cursor.execute('SELECT nom_affaire, type_crime, lieu, etat, date_ouverture FROM affaire')
            rows = cursor.fetchall()
            for row in rows:
                affaire = {
                    "nom": row[0],
                    "type_crime": row[1],
                    "lieu": row[2],
                    "statut": row[3],
                    "date_ouverture": row[4]
                }
                self.affaires.append(affaire)
            conn.close()
        except sqlite3.Error as e:
            print(f"Erreur lors du chargement des affaires depuis la base de données : {e}")

    def charger_preuves(self):
        try:
            conn = sqlite3.connect(self.get_database_path())
            cursor = conn.cursor()
            cursor.execute('SELECT nom_preuve, nom_affaire FROM preuve')
            rows = cursor.fetchall()
            for row in rows:
                nom_preuve = row[0]
                affaire_nom = row[1]
                if affaire_nom not in self.preuves:
                    self.preuves[affaire_nom] = []
                self.preuves[affaire_nom].append(nom_preuve)
            conn.close()
        except sqlite3.Error as e:
            print(f"Erreur lors du chargement des preuves depuis la base de données : {e}")

    def gerer_affaires(self):
        print("Bouton Gérer les Affaires cliqué !")
        self.dialog = AffaireDialog(self.affaires)
        self.dialog.exec_()

    def gerer_preuves(self):
        print("Bouton Gérer les Preuves cliqué !")
        noms_affaires = [affaire["nom"] for affaire in self.affaires]
        affaire, ok = QInputDialog.getItem(self, "Sélectionner une Affaire", "Affaires disponibles:", noms_affaires, 0, False)
        if ok and affaire:
            if affaire not in self.preuves:
                self.preuves[affaire] = []
            self.dialog = PreuveDialog(self.preuves[affaire])
            self.dialog.exec_()

    def generer_rapport(self):
        print("Bouton Générer un Rapport cliqué !")
        self.creer_pdf()

    def creer_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Ajouter un titre
        pdf.cell(200, 10, txt="Rapport des Affaires Criminelles", ln=True, align='C')

        # Ajouter les affaires et leurs preuves au PDF
        for affaire in self.affaires:
            pdf.cell(200, 10, txt=f"Affaire: {affaire['nom']}", ln=True, align='L')
            pdf.cell(200, 10, txt=f"  Type de crime: {affaire['type_crime']}", ln=True, align='L')
            pdf.cell(200, 10, txt=f"  Lieu: {affaire['lieu']}", ln=True, align='L')
            pdf.cell(200, 10, txt=f"  Statut: {affaire['statut']}", ln=True, align='L')
            pdf.cell(200, 10, txt=f"  Date d'ouverture: {affaire['date_ouverture']}", ln=True, align='L')
            if affaire['nom'] in self.preuves:
                for preuve in self.preuves[affaire['nom']]:
                    pdf.cell(200, 10, txt=f"    Preuve: {preuve}", ln=True, align='L')

        # Sauvegarder le PDF
        pdf.output("rapport_affaires_criminelles.pdf")
        QMessageBox.information(self, "Succès", "Le rapport a été généré avec succès !")

    def rechercher(self):
        query = self.search_input.text().lower()
        if not query:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer un terme de recherche.")
            return

        self.resultats = []

        # Rechercher dans les affaires
        for affaire in self.affaires:
            if query in affaire["nom"].lower() or query in affaire["type_crime"].lower() or query in affaire["lieu"].lower() or query in affaire["statut"].lower():
                self.resultats.append(f"Affaire: {affaire['nom']}")

        # Rechercher dans les preuves
        for affaire, preuves in self.preuves.items():
            for preuve in preuves:
                if query in preuve.lower():
                    self.resultats.append(f"Preuve: {preuve} (Affaire: {affaire})")

        if self.resultats:
            self.afficher_resultats()
        else:
            QMessageBox.information(self, "Résultats de la recherche", "Aucun résultat trouvé.")

    def afficher_resultats(self):
        self.resultats_dialog = QDialog(self)
        self.resultats_dialog.setWindowTitle("Résultats de la recherche")
        layout = QVBoxLayout()

        self.resultats_list = QListWidget()
        self.resultats_list.addItems(self.resultats)
        self.resultats_list.itemClicked.connect(self.afficher_details)

        layout.addWidget(self.resultats_list)
        self.resultats_dialog.setLayout(layout)
        self.resultats_dialog.exec_()

    def afficher_details(self, item):
        texte = item.text()
        if texte.startswith("Affaire:"):
            nom_affaire = texte.split(": ")[1]
            affaire = next((a for a in self.affaires if a["nom"] == nom_affaire), None)
            if affaire:
                details = (
                    f"Nom: {affaire['nom']}\n"
                    f"Type de crime: {affaire['type_crime']}\n"
                    f"Lieu: {affaire['lieu']}\n"
                    f"Statut: {affaire['statut']}\n"
                    f"Date d'ouverture: {affaire['date_ouverture']}"
                )
                QMessageBox.information(self, "Détails de l'affaire", details)
        elif texte.startswith("Preuve:"):
            nom_preuve = texte.split(": ")[1].split(" (Affaire: ")[0]
            nom_affaire = texte.split(" (Affaire: ")[1][:-1]
            affaire = next((a for a in self.affaires if a["nom"] == nom_affaire), None)
            if affaire:
                details = (
                    f"Affaire: {affaire['nom']}\n"
                    f"Preuve: {nom_preuve}"
                )
                QMessageBox.information(self, "Détails de la preuve", details)

    def get_database_path(self, db_name: str = 'database.db') -> str:
        """
        Get the absolute path to a database file.

        Args:
            db_name (str): The name of the database file (e.g., "database.db").

        Returns:
            str: The absolute path to the database file.
        """
        # Get the directory where the script is running
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the full path to the database file
        db_path = os.path.join(script_dir, db_name)
        return db_path

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())