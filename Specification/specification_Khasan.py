#Specification Aktamirov Khasan

def ajouter_affaire(self, nom_affaire, type_affaire, lieu, statut, date_ouverture):
    """
    Cette fonction permet d'ajouter une nouvelle affaire à la base de données en récupérant les informations saisies dans l'interface graphique.

    :param Aucun (les données sont récupérées depuis les champs d'entrée de l'interface graphique)
    :return bool:

    PRE : Les champs de saisie doivent contenir des données valides et non vides.
          Une connexion active à la base de données doit être disponible.
          La table "affaire" doit exister dans la base de données avec les colonnes nécessaires.
    POST : Retourne un booléen. True si l'affaire a été ajoutée avec succès, sinon False.
    """
    pass


def afficher_resultats(self):
    """
    Cette fonction permet d'afficher une liste de résultats de recherche dans une fenêtre de dialogue et de gérer la sélection d'un élément pour afficher ses détails.

    :param Aucun (les données sont récupérées depuis l'attribut self.resultats qui contient une liste de chaînes de caractères)
    :return Aucun

    PRE : L'attribut self.resultats doit contenir une liste non vide de chaînes de caractères représentant les résultats de la recherche.
    POST : Ouvre une fenêtre de dialogue affichant les résultats sous forme de liste cliquable.
           Si un élément est cliqué, la méthode afficher_details est appelée avec cet élément en paramètre.
    """
    pass


def gerer_preuves(self):
    """
    Cette fonction permet à l'utilisateur de gérer les preuves associées à une affaire sélectionnée via une interface de sélection.

    :param Aucun (les données sont récupérées à partir des attributs self.affaires et self.preuves)
    :return Aucun

    PRE : L'attribut self.affaires doit contenir une liste de dictionnaires avec une clé "nom" pour chaque affaire.
          L'attribut self.preuves doit être un dictionnaire où chaque clé est le nom d'une affaire, et chaque valeur est une liste de preuves associées.
    POST : Affiche une boîte de dialogue permettant à l'utilisateur de sélectionner une affaire.
           Si l'affaire est sélectionnée, ouvre un dialogue pour afficher et gérer les preuves associées.
           Si aucune liste de preuves n'existe pour l'affaire sélectionnée, une liste vide est initialisée pour cette affaire.
    """
    pass



def creer_pdf(self):
    """
    Cette fonction génère un rapport PDF contenant les informations sur toutes les affaires et leurs preuves associées, puis sauvegarde le fichier localement.

    :param Aucun (les données sont récupérées à partir des attributs self.affaires et self.preuves)
    :return Aucun

    PRE :
        - L'attribut self.affaires doit contenir une liste de dictionnaires représentant les affaires avec les clés suivantes :
          "nom", "type_crime", "lieu", "statut", "date_ouverture".
        - L'attribut self.preuves doit être un dictionnaire où chaque clé est le nom d'une affaire, et chaque valeur est une liste de preuves associées.
        - Le module FPDF doit être importé et disponible.
        - Le chemin d'écriture ("rapport_affaires_criminelles.pdf") doit être accessible pour la sauvegarde du fichier.

    POST :
        - Crée un fichier PDF nommé "rapport_affaires_criminelles.pdf" contenant les informations des affaires et leurs preuves.
        - Affiche un message d'information indiquant le succès de la génération du rapport.
    """
    pass

def rechercher(self):
    """
    Cette méthode effectue une recherche dans les affaires et les preuves en fonction de la requête entrée par l'utilisateur dans un champ de recherche.

    :param Aucun (les données nécessaires, comme `self.affaires` et `self.preuves`, sont disponibles dans l'objet).

    PRE :
        - `self.search_input` doit contenir un champ de texte valide pour l'entrée de la requête.
        - `self.affaires` doit être une liste de dictionnaires contenant au moins les clés "nom", "type_crime", "lieu", et "statut".
        - `self.preuves` doit être un dictionnaire où les clés sont les noms des affaires et les valeurs sont des listes de preuves.
        - La méthode `afficher_resultats` doit être implémentée dans la classe pour afficher les résultats.

    POST :
        - Si une requête valide est fournie et des résultats correspondants sont trouvés, ceux-ci sont stockés dans `self.resultats` et affichés via `afficher_resultats`.
        - Si aucune correspondance n'est trouvée, un message d'information est affiché à l'utilisateur.
        - Si la requête est vide, un message d'avertissement est affiché, et la recherche est interrompue.
    """
    pass