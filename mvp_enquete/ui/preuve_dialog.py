from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QLineEdit, QListWidget, QMessageBox
import sqlite3
import os
import os.path

class PreuveDialog(QDialog):
    def __init__(self, preuves):
        super().__init__()

        self.preuves = preuves

        self.setWindowTitle("Gérer les Preuves")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Gestion des Preuves")
        layout.addWidget(self.label)

        self.preuve_list = QListWidget()
        layout.addWidget(self.preuve_list)

        self.input_preuve = QLineEdit()
        self.input_preuve.setPlaceholderText("Nom de la preuve")
        layout.addWidget(self.input_preuve)

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

        # Charger les preuves existantes dans la liste
        self.charger_preuves()

    def charger_preuves(self):
        self.preuve_list.clear()
        for preuve in self.preuves:
            self.preuve_list.addItem(preuve)

    def ajouter_preuve(self):
        nom_preuve = self.input_preuve.text()
        if nom_preuve:
            self.preuves.append(nom_preuve)
            self.preuve_list.addItem(nom_preuve)
            self.input_preuve.clear()


            # Ajouter l'preuve dans la base de données
            self.ajouter_preuve_db(nom_preuve)
            print(f"Preuve '{nom_preuve}' ajoutée !")
        else:
            QMessageBox.warning(self, "Erreur", "Le nom de la preuve ne peut pas être vide.")

    def modifier_preuve(self):
        selected_item = self.preuve_list.currentItem()
        if selected_item:
            nom_preuve = self.input_preuve.text()
            if nom_preuve:
                index = self.preuve_list.row(selected_item)
                self.preuves[index] = nom_preuve
                selected_item.setText(nom_preuve)
                self.input_preuve.clear()
                print(f"Preuve modifiée en '{nom_preuve}' !")
            else:
                QMessageBox.warning(self, "Erreur", "Le nom de la preuve ne peut pas être vide.")
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner une preuve à modifier.")

    def supprimer_preuve(self):
        selected_item = self.preuve_list.currentItem()
        if selected_item:
            index = self.preuve_list.row(selected_item)
            del self.preuves[index]
            self.preuve_list.takeItem(index)
            print(f"Preuve '{selected_item.text()}' supprimée !")
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner une preuve à supprimer.")

    def ajouter_preuve_db(self, nom):
        try:
            conn = sqlite3.connect(self.get_database_path())
            cursor = conn.cursor()

            # Insérer les données dans la table preuve
            cursor.execute('''
                INSERT INTO preuve (nom_preuve, type_preuve, description, lien, lieu_collecte, date_heure_decouverte, resultat_analyse, etat_actuel, scientifique_en_charge)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (nom, '', '', '', '', '2023-01-01', '', '', ''))

            conn.commit()  # Valider les modifications
            print(f"Preuve '{nom}' ajoutée dans la base de données.")
            conn.close()
        except sqlite3.Error as e:
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
        return db_path
