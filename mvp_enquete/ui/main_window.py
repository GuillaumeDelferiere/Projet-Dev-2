from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QMessageBox, QInputDialog, QListWidget, QDialog, QLabel
from ui.affaire_dialog import AffaireDialog
from ui.preuve_dialog import PreuveDialog
from core.affaire_manager import AffaireManager
from core.preuve_manager import PreuveManager
from export_pdf import generer_pdf

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

        # Initialiser les gestionnaires
        self.affaire_manager = AffaireManager()
        self.preuve_manager = PreuveManager()

        # Connecter les boutons aux méthodes
        self.btn_affaires.clicked.connect(self.gerer_affaires)
        self.btn_preuves.clicked.connect(self.gerer_preuves)
        self.btn_rapport.clicked.connect(self.generer_rapport)
        self.search_button.clicked.connect(self.rechercher)

    def gerer_affaires(self):
        dialog = AffaireDialog(self.affaire_manager)
        dialog.exec_()

    def gerer_preuves(self):
        dialog = PreuveDialog(self.preuve_manager)
        dialog.exec_()

    def generer_rapport(self):
        affaires = self.affaire_manager.get_all_affaires()
        generer_pdf(affaires)
        QMessageBox.information(self, "Succès", "Le rapport a été généré avec succès!")

    def rechercher(self):
        query = self.search_input.text().lower()
        if not query:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer un terme de recherche.")
            return

        resultats = self.affaire_manager.search(query) + self.preuve_manager.search(query)
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