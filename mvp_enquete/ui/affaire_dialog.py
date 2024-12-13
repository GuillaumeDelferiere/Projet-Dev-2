from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QLineEdit, QListWidget, QMessageBox, QComboBox, QDateEdit
from PyQt5.QtCore import QDate
import sqlite3
import os
import os.path


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
        date_ouverture = self.input_date.date().toString("yyyy-MM-dd")  # Format SQL compatible

        if nom_affaire and type_crime and lieu:
            # Ajouter dans la liste interne et l'interface
            affaire = {
                "nom": nom_affaire,
                "type_crime": type_crime,
                "lieu": lieu,
                "statut": statut,
                "date_ouverture": date_ouverture
            }
            self.affaires.append(affaire)
            self.affaire_list.addItem(nom_affaire)

            # Réinitialiser les champs d'entrée
            self.input_nom.clear()
            self.input_type.clear()
            self.input_lieu.clear()

            # Ajouter l'affaire dans la base de données
            self.ajouter_affaire_db(nom_affaire, type_crime, lieu, statut, date_ouverture)
        else:
            QMessageBox.warning(self, "Erreur", "Tous les champs doivent être remplis.")

    def modifier_affaire(self):
        selected_item = self.affaire_list.currentItem()
        if selected_item:
            nom_affair = self.input_nom.text()
            type_crime = self.input_type.text()
            lieu = self.input_lieu.text()
            statut = self.input_statut.currentText()
            date_ouverture = self.input_date.date().toString("dd/MM/yyyy")

            if nom_affair and type_crime and lieu:
                index = self.affaire_list.row(selected_item)
                self.affaires[index] = {
                    "nom": nom_affair,
                    "type_crime": type_crime,
                    "lieu": lieu,
                    "statut": statut,
                    "date_ouverture": date_ouverture
                }
                selected_item.setText(nom_affair)
                self.input_nom.clear()
                self.input_type.clear()
                self.input_lieu.clear()
                print(f"Affaire modifiée en '{nom_affair}' !")
            else:
                QMessageBox.warning(self, "Erreur", "Tous les champs doivent être remplis.")
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner une affaire à modifier.")

    def supprimer_affaire(self):
        selected_item = self.affaire_list.currentItem()
        print(selected_item)
        print(self)
        if selected_item:
            index = self.affaire_list.row(selected_item)
            del self.affaires[index]
            self.affaire_list.takeItem(index)
            print(f"Affaire '{selected_item.text()}' supprimée !")
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner une affaire à supprimer.")


    def ajouter_affaire_db(self, nom, type_crime, lieu, statut, date_ouverture):
        try:
            print(f"Ajout de l'affaire dans la base de données : {nom}, {type_crime}, {lieu}, {statut}, {date_ouverture}")
            conn = sqlite3.connect(self.get_database_path())
            cursor = conn.cursor()

            # Insérer les données dans la table affaire
            cursor.execute('''
                INSERT INTO affaire (nom_affaire, type_crime, lieu, etat, date_ouverture)
                VALUES (?, ?, ?, ?, ?)
            ''', (nom, type_crime, lieu, statut, date_ouverture))

            conn.commit()  # Valider les modifications
            print(f"Affaire '{nom}' ajoutée dans la base de données.")
            conn.close()
        except sqlite3.Error as e:
            print(f"Erreur lors de l'ajout dans la base de données : {e}")
            QMessageBox.critical(self, "Erreur", f"Erreur lors de l'ajout dans la base de données : {e}")
        
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
        print(f"Chemin de la base de données : {db_path}")
        return db_path
