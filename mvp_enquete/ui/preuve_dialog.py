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

            conn = sqlite3.connect(self.get_database_path())
            cursor = conn.cursor()

            # Insérer les données dans la table preuve
            cursor.execute('''
                            INSERT INTO preuve (nom_preuve)
                            VALUES (?)
                        ''', (nom_preuve,))

            conn.commit()

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

    def get_database_path(self, db_name: str = 'poo.db') -> str:
        """
        Get the absolute path to a database file.

        Args:
            db_name (str): The name of the database file (e.g., "poo.db").

        Returns:
            str: The absolute path to the database file.
        """
        # Get the directory where the script is running
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the full path to the database file
        db_path = os.path.join(script_dir, db_name)
        return db_path