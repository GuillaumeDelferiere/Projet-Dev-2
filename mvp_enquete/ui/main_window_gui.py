from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox, QInputDialog, QLineEdit, QListWidget, QDialog, QVBoxLayout, QLabel
import sys
from PyQt5.QtWidgets import QApplication
from fpdf import FPDF
from main_window_core import AffaireManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestion des Affaires Criminelles")
        self.setGeometry(100, 100, 800, 600)

        # Initialiser le gestionnaire d'affaires
        self.manager = AffaireManager()

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

        # Connecter les boutons aux méthodes
        self.btn_affaires.clicked.connect(self.gerer_affaires)
        self.btn_preuves.clicked.connect(self.gerer_preuves)
        self.btn_rapport.clicked.connect(self.generer_rapport)
        self.search_button.clicked.connect(self.rechercher)

    def gerer_affaires(self):
        nom, ok = QInputDialog.getText(self, "Ajouter une Affaire", "Nom de l'affaire:")
        if ok and nom:
            self.manager.add_affaire(nom, "Type de crime", "Lieu", "Statut", "2024-01-01")
            QMessageBox.information(self, "Succès", "Affaire ajoutée avec succès!")

    def gerer_preuves(self):
        affaires = self.manager.get_all_affaires()
        noms_affaires = [affaire["nom"] for affaire in affaires]
        affaire, ok = QInputDialog.getItem(self, "Sélectionner une Affaire", "Affaires disponibles:", noms_affaires, 0, False)
        if ok and affaire:
            affaire_id = next(a["id"] for a in affaires if a["nom"] == affaire)
            preuve, ok = QInputDialog.getText(self, "Ajouter une Preuve", "Nom de la preuve:")
            if ok and preuve:
                self.manager.add_preuve(preuve, affaire_id)
                QMessageBox.information(self, "Succès", "Preuve ajoutée avec succès!")

    def generer_rapport(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Ajouter un titre
        pdf.cell(200, 10, txt="Rapport des Affaires Criminelles", ln=True, align='C')

        # Ajouter les affaires et leurs preuves au PDF
        affaires = self.manager.get_all_affaires()
        for affaire in affaires:
            pdf.cell(200, 10, txt=f"Affaire: {affaire['nom']}", ln=True, align='L')
            pdf.cell(200, 10, txt=f"  Type de crime: {affaire['type_crime']}", ln=True, align='L')
            pdf.cell(200, 10, txt=f"  Lieu: {affaire['lieu']}", ln=True, align='L')
            pdf.cell(200, 10, txt=f"  Statut: {affaire['statut']}", ln=True, align='L')
            pdf.cell(200, 10, txt=f"  Date d'ouverture: {affaire['date_ouverture']}", ln=True, align='L')
            preuves = self.manager.get_preuves_by_affaire(affaire['id'])
            for preuve in preuves:
                pdf.cell(200, 10, txt=f"    Preuve: {preuve}", ln=True, align='L')

        # Sauvegarder le PDF
        pdf.output("rapport_affaires_criminelles.pdf")
        QMessageBox.information(self, "Succès", "Le rapport a été généré avec succès!")

    def rechercher(self):
        query = self.search_input.text().lower()
        if not query:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer un terme de recherche.")
            return

        resultats = self.manager.search(query)
        if resultats:
            self.afficher_resultats(resultats)
        else:
            QMessageBox.information(self, "Résultats de la recherche", "Aucun résultat trouvé.")

    def afficher_resultats(self, resultats):
        self.resultats_dialog = QDialog(self)
        self.resultats_dialog.setWindowTitle("Résultats de la recherche")
        layout = QVBoxLayout()

        self.resultats_list = QListWidget()
        self.resultats_list.addItems(resultats)

        layout.addWidget(self.resultats_list)
        self.resultats_dialog.setLayout(layout)
        self.resultats_dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
