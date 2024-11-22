from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QLineEdit, QListWidget, QMessageBox, QComboBox, QDateEdit
from PyQt5.QtCore import QDate

class AffaireDialog(QDialog):
    def __init__(self, affaires):
        super().__init__()

        self.affaires = affaires

        self.setWindowTitle("Gérer les Affaires")
        self.setGeometry(100, 100, 400, 400)

        layout = QVBoxLayout()

        self.label = QLabel("Gestion des Affaires")
        layout.addWidget(self.label)

        self.affaire_list = QListWidget()
        layout.addWidget(self.affaire_list)

        self.input_nom = QLineEdit()
        self.input_nom.setPlaceholderText("Nom de l'affaire")
        layout.addWidget(self.input_nom)

        self.input_type = QLineEdit()
        self.input_type.setPlaceholderText("Type de crime")
        layout.addWidget(self.input_type)

        self.input_lieu = QLineEdit()
        self.input_lieu.setPlaceholderText("Lieu")
        layout.addWidget(self.input_lieu)

        self.input_statut = QComboBox()
        self.input_statut.addItems(["Ouverte", "Fermée", "En cours"])
        layout.addWidget(self.input_statut)

        self.input_date = QDateEdit()
        self.input_date.setCalendarPopup(True)
        self.input_date.setDate(QDate.currentDate())
        layout.addWidget(self.input_date)

        self.btn_ajouter = QPushButton("Ajouter une Affaire")
        self.btn_modifier = QPushButton("Modifier une Affaire")
        self.btn_supprimer = QPushButton("Supprimer une Affaire")

        layout.addWidget(self.btn_ajouter)
        layout.addWidget(self.btn_modifier)
        layout.addWidget(self.btn_supprimer)

        self.setLayout(layout)

        # Connecter les boutons aux méthodes
        self.btn_ajouter.clicked.connect(self.ajouter_affaire)
        self.btn_modifier.clicked.connect(self.modifier_affaire)
        self.btn_supprimer.clicked.connect(self.supprimer_affaire)

        # Charger les affaires existantes dans la liste
        self.charger_affaires()

    def charger_affaires(self):
        self.affaire_list.clear()
        for affaire in self.affaires:
            self.affaire_list.addItem(affaire["nom"])

    def ajouter_affaire(self):
        nom_affaire = self.input_nom.text()
        type_crime = self.input_type.text()
        lieu = self.input_lieu.text()
        statut = self.input_statut.currentText()
        date_ouverture = self.input_date.date().toString("dd/MM/yyyy")

        if nom_affaire and type_crime and lieu:
            affaire = {
                "nom": nom_affaire,
                "type_crime": type_crime,
                "lieu": lieu,
                "statut": statut,
                "date_ouverture": date_ouverture
            }
            self.affaires.append(affaire)
            self.affaire_list.addItem(nom_affaire)
            self.input_nom.clear()
            self.input_type.clear()
            self.input_lieu.clear()
            print(f"Affaire '{nom_affaire}' ajoutée !")
        else:
            QMessageBox.warning(self, "Erreur", "Tous les champs doivent être remplis.")

    def modifier_affaire(self):
        selected_item = self.affaire_list.currentItem()
        if selected_item:
            nom_affaire = self.input_nom.text()
            type_crime = self.input_type.text()
            lieu = self.input_lieu.text()
            statut = self.input_statut.currentText()
            date_ouverture = self.input_date.date().toString("dd/MM/yyyy")

            if nom_affaire and type_crime and lieu:
                index = self.affaire_list.row(selected_item)
                self.affaires[index] = {
                    "nom": nom_affaire,
                    "type_crime": type_crime,
                    "lieu": lieu,
                    "statut": statut,
                    "date_ouverture": date_ouverture
                }
                selected_item.setText(nom_affaire)
                self.input_nom.clear()
                self.input_type.clear()
                self.input_lieu.clear()
                print(f"Affaire modifiée en '{nom_affaire}' !")
            else:
                QMessageBox.warning(self, "Erreur", "Tous les champs doivent être remplis.")
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner une affaire à modifier.")

    def supprimer_affaire(self):
        selected_item = self.affaire_list.currentItem()
        if selected_item:
            index = self.affaire_list.row(selected_item)
            del self.affaires[index]
            self.affaire_list.takeItem(index)
            print(f"Affaire '{selected_item.text()}' supprimée !")
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner une affaire à supprimer.")