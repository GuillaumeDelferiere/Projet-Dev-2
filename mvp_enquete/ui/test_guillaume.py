import unittest
from unittest.mock import MagicMock
from PyQt5.QtWidgets import QApplication
from preuve_dialog_gui import PreuveDialog

class TestPreuveDialog(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])  # Nécessaire pour initialiser l'application Qt
        self.preuves = ["Preuve 1", "Preuve 2"]
        self.dialog = PreuveDialog(self.preuves)
        self.dialog.manager.add_preuve = MagicMock()  # Simuler le PreuveManager

    def tearDown(self):
        self.app.quit()

# Test sur la fonction ajouter_preuve(self)
    def test_ajouter_preuve_valide(self):
        self.dialog.input_preuve.setText("Preuve 3")
        self.dialog.ajouter_preuve()
        self.assertIn("Preuve 3", self.dialog.preuves)
        self.assertEqual(self.dialog.preuve_list.count(), 3)
        self.assertEqual(self.dialog.preuve_list.item(2).text(), "Preuve 3")
        self.assertEqual(self.dialog.input_preuve.text(), "")
    # Résultat attendu : Preuve 3 est ajouté à self.preuves, la liste contient 3 éléments
    # Le dernier élément est "Preuve 3" et le champ de saisie est vide

    def test_ajouter_preuve_vide(self):
        self.dialog.input_preuve.setText("")
        with self.assertRaises(Exception):
            self.dialog.ajouter_preuve()
        self.assertEqual(self.dialog.preuve_list.count(), 2)
        # Résutat attendu : Exception donc la validation a échouée
        # Le nombre d'éléments de la liste reste 2

    def test_ajouter_preuve_duplicate(self):
        self.dialog.input_preuve.setText("Preuve 1")
        self.dialog.ajouter_preuve()
        self.assertEqual(self.dialog.preuve_list.count(), 3)
        self.assertEqual(self.dialog.preuves.count("Preuve 1"), 2)
        # Résultat attendu : la preuve est ajoutée, la liste contient 3 éléments
        # Preuve 1 apparait 2 fois dans self.preuves

# Test sur la fonction modifier_preuve(self)
    def test_modifier_preuve_valide(self):
        self.dialog.preuve_list.setCurrentRow(1)
        self.dialog.input_preuve.setText("Preuve Modifiée")
        self.dialog.modifier_preuve()
        self.assertEqual(self.dialog.preuves[1], "Preuve Modifiée")
        self.assertEqual(self.dialog.preuve_list.item(1).text(), "Preuve Modifiée")
        self.assertEqual(self.dialog.input_preuve.text(), "")
    # Résultat attendu : la preuve à l'index = 1 devient "Preuve modifiée"
    # Le champ de saisie est vide

    def test_modifier_preuve_vide(self):
        self.dialog.preuve_list.setCurrentRow(0)
        self.dialog.input_preuve.setText("")
        with self.assertRaises(Exception):
            self.dialog.modifier_preuve()
        self.assertEqual(self.dialog.preuves[0], "Preuve 1")
        self.assertEqual(self.dialog.preuve_list.item(0).text(), "Preuve 1")
    # Résultat attendu : il y a une exception donc la validation échoue
    # La liste reste inchangée

    def test_modifier_preuve_non_selectionnee(self):
        self.dialog.preuve_list.setCurrentRow(-1)
        self.dialog.input_preuve.setText("Preuve Modifiée")
        with self.assertRaises(Exception):
            self.dialog.modifier_preuve()
    # Résultat attendu : exception car aucun preuve n'est sélectionnée

# Test sur la fonction supprimer_preuves(self)
    def test_supprimer_preuve_valide(self):
        self.dialog.preuve_list.setCurrentRow(0)
        self.dialog.supprimer_preuve()
        self.assertNotIn("Preuve 1", self.dialog.preuves)
        self.assertEqual(self.dialog.preuve_list.count(), 1)
        self.assertEqual(self.dialog.preuve_list.item(0).text(), "Preuve 2")
    # Résultat attendu : "Preuve 1" est supprimée de self.preuves
    # La liste contient désormais un seul élément

    def test_supprimer_preuve_non_selectionnee(self):
        self.dialog.preuve_list.setCurrentRow(-1)
        with self.assertRaises(Exception):
            self.dialog.supprimer_preuve()
        self.assertEqual(self.dialog.preuve_list.count(), 2)
    # Résultat attendu : une exception est levée car pas de sélection
    # La liste reste inchangée

    def test_supprimer_derniere_preuve(self):
        self.dialog.preuve_list.setCurrentRow(1)
        self.dialog.supprimer_preuve()
        self.dialog.preuve_list.setCurrentRow(0)
        self.dialog.supprimer_preuve()
        self.assertEqual(len(self.dialog.preuves), 0)
        self.assertEqual(self.dialog.preuve_list.count(), 0)
    # Résultat attendu : Supprime toutes les preuves, la liste est = à 0
if __name__ == "__main__":
    unittest.main()
