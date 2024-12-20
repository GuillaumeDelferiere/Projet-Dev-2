from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QLineEdit, QListWidget, QComboBox, QDateTimeEdit
from PyQt5.QtCore import QDateTime

class PreuveDialog(QDialog):
    def __init__(self, preuve_manager):
        super().__init__()

        self.preuve_manager = preuve_manager

        self.setWindowTitle("Gérer les Preuves")
        self.setGeometry(100, 100, 400, 400)

        layout = QVBoxLayout()

        self.label = QLabel("Gestion des Preuves")
        layout.addWidget(self.label)

        self.preuve_list = QListWidget()
        layout.addWidget(self.preuve_list)

        self.input_nom = QLineEdit()
        self.input_nom.setPlaceholderText("Nom de la preuve")
        layout.addWidget(self.input_nom)

        self.input_type = QLineEdit()
        self.input_type.setPlaceholderText("Type de preuve")
        layout.addWidget(self.input_type)

        self.input_description = QLineEdit()
        self.input_description.setPlaceholderText("Description")
        layout.addWidget(self.input_description)

        self.input_lien = QLineEdit()
        self.input_lien.setPlaceholderText("Lien")
        layout.addWidget(self.input_lien)

        self.input_lieu_collecte = QLineEdit()
        self.input_lieu_collecte.setPlaceholderText("Lieu de collecte")
        layout.addWidget(self.input_lieu_collecte)

        self.input_date_heure = QDateTimeEdit()
        self.input_date_heure.setCalendarPopup(True)
        self.input_date_heure.setDateTime(QDateTime.currentDateTime())
        layout.addWidget(self.input_date_heure)

        self.input_resultat_analyse = QLineEdit()
        self.input_resultat_analyse.setPlaceholderText("Résultat de l'analyse")
        layout.addWidget(self.input_resultat_analyse)

        self.input_etat_actuel = QComboBox()
        self.input_etat_actuel.addItems(["En cours", "Terminé", "Archivé"])
        layout.addWidget(self.input_etat_actuel)

        self.input_scientifique = QLineEdit()
        self.input_scientifique.setPlaceholderText("Scientifique en charge")
        layout.addWidget(self.input_scientifique)

        self.btn_ajouter = QPushButton("Ajouter une Preuve")
        self.btn_modifier = QPushButton("Modifier une Preuve")
        self.btn_supprimer = QPushButton("Supprimer une Preuve")

        layout.addWidget(self.btn_ajouter)
        layout.addWidget(self.btn_modifier)
        layout.addWidget(self.btn_supprimer)

        self.setLayout(layout)

        # Connecter les boutons aux méthodes
        self.btn_ajouter.clicked.connect(self.ajouter_preuve)
        self.btn_modifier.clicked.connect(self.modifier_preuve)
        self.btn_supprimer.clicked.connect(self.supprimer_preuve)

        # Charger les preuves existantes
        self.charger_preuves()

    def charger_preuves(self):
        self.preuve_list.clear()
        preuves = self.preuve_manager.get_all_preuves()
        for preuve in preuves:
            self.preuve_list.addItem(preuve["nom"])

    def ajouter_preuve(self):
        nom = self.input_nom.text()
        type_preuve = self.input_type.text()
        description = self.input_description.text()
        lien = self.input_lien.text()
        lieu_collecte = self.input_lieu_collecte.text()
        date_heure_decouverte = self.input_date_heure.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        resultat_analyse = self.input_resultat_analyse.text()
        etat_actuel = self.input_etat_actuel.currentText()
        scientifique_en_charge = self.input_scientifique.text()

        self.preuve_manager.add_preuve(nom, type_preuve, description, lien, lieu_collecte, date_heure_decouverte, resultat_analyse, etat_actuel, scientifique_en_charge)
        self.charger_preuves()

    def modifier_preuve(self):
        selected_item = self.preuve_list.currentItem()
        if selected_item:
            nom = self.input_nom.text()
            type_preuve = self.input_type.text()
            description = self.input_description.text()
            lien = self.input_lien.text()
            lieu_collecte = self.input_lieu_collecte.text()
            date_heure_decouverte = self.input_date_heure.dateTime().toString("yyyy-MM-dd HH:mm:ss")
            resultat_analyse = self.input_resultat_analyse.text()
            etat_actuel = self.input_etat_actuel.currentText()
            scientifique_en_charge = self.input_scientifique.text()
            index = self.preuve_list.row(selected_item)

            self.preuve_manager.update_preuve(index, nom, type_preuve, description, lien, lieu_collecte, date_heure_decouverte, resultat_analyse, etat_actuel, scientifique_en_charge)
            self.charger_preuves()

    def supprimer_preuve(self):
        selected_item = self.preuve_list.currentItem()
        if selected_item:
            index = self.preuve_list.row(selected_item)
            self.preuve_manager.delete_preuve(index)
            self.charger_preuves()