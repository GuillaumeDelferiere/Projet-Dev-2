import unittest
from unittest.mock import MagicMock, patch

class TestApplication(unittest.TestCase):

    def setUp(self):
        self.app = MagicMock()  # Instanciation simulée de ton application
        self.app.search_input = MagicMock()  # Mock de l'objet de saisie
        self.app.resultats = []  # Initialisation d'une liste pour les résultats
        self.app.afficher_resultats = MagicMock()  # Mock de la méthode afficher_resultats
        self.app.affaires = [
            {"nom": "Affaire 1", "type_crime": "Vol", "lieu": "Paris", "statut": "Ouvert"}
        ]
        self.app.preuves = {"Affaire 1": ["Preuve 1"]}

    # Test pour ajouter_affaire
    def test_ajouter_affaire(self):
        self.app.ajouter_affaire = MagicMock(return_value=True)
        result = self.app.ajouter_affaire("Affaire 2", "Fraude", "Lyon", "Ouvert", "2024-02-01")
        self.assertTrue(result)
        self.app.ajouter_affaire.assert_called_once_with("Affaire 2", "Fraude", "Lyon", "Ouvert", "2024-02-01")

    # Test pour afficher_resultats
    def test_afficher_resultats(self):
        self.app.resultats = ["Affaire: Affaire 1", "Preuve: Preuve 1 (Affaire: Affaire 1)"]
        self.app.afficher_details = MagicMock()
        self.app.afficher_resultats()

        self.assertEqual(len(self.app.resultats), 2)
        self.app.afficher_details.assert_not_called()  # Vérifier si afficher_details n'est pas appelé par erreur ici

    # Test pour gerer_preuves
    def test_gerer_preuves(self):
        with patch("PyQt5.QtWidgets.QMessageBox.information") as mock_message:
            self.app.gerer_preuves()
            mock_message.assert_not_called()
            self.assertIn("Affaire 1", self.app.preuves)
            self.assertEqual(len(self.app.preuves["Affaire 1"]), 2)

    # Test pour creer_pdf
    @patch("fpdf.FPDF.output")
    def test_creer_pdf(self, mock_output):
        self.app.creer_pdf()
        mock_output.assert_called_once_with("rapport_affaires_criminelles.pdf")

    # Test pour rechercher
    def test_rechercher(self):
        # Cas normal avec "vol"
        self.app.search_input.text.return_value = "vol"
        self.app.rechercher()
        self.assertIn("Affaire: Affaire 1", self.app.resultats)

        # Cas normal avec "Preuve 1"
        self.app.search_input.text.return_value = "Preuve 1"
        self.app.rechercher()
        self.assertIn("Preuve: Preuve 1 (Affaire: Affaire 1)", self.app.resultats)

        # Cas où la requête est vide
        self.app.search_input.text.return_value = ""
        with patch("PyQt5.QtWidgets.QMessageBox.warning") as mock_warning:
            self.app.rechercher()
            mock_warning.assert_called_once_with(self.app, "Erreur", "Veuillez entrer un terme de recherche.")


if __name__ == "__main__":
    unittest.main()
