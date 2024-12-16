def ajouter_preuve_db(self, nom):
    """
    Ajoute une preuve dans la base de données.

    Args:
        nom (str): Le nom de la preuve.

    Pre:
        - `nom` doit être une chaîne de caractères non vide.
        - La base de données doit être accessible.

    Post:
        - La preuve est ajoutée dans la table `preuve` de la base de données.
        - La transaction est validée et la connexion à la base de données est fermée.

    Raises:
        sqlite3.Error: Si une erreur se produit lors de l'insertion dans la base de données.
    """

def charger_affaires(self):
    """
    Charge les affaires depuis la base de données et les stocke dans `self.affaires`.

    Pre:
        - La base de données doit être accessible.

    Post:
        - `self.affaires` contient une liste de dictionnaires représentant les affaires chargées depuis la base de données.

    Raises:
        sqlite3.Error: Si une erreur se produit lors du chargement des affaires depuis la base de données.
    """

def ajouter_affaire_db(self, nom, type_crime, lieu, statut, date_ouverture):
    """
    Ajoute une affaire dans la base de données.

    Args:
        nom (str): Le nom de l'affaire.
        type_crime (str): Le type de crime.
        lieu (str): Le lieu de l'affaire.
        statut (str): Le statut de l'affaire.
        date_ouverture (str): La date d'ouverture de l'affaire au format "yyyy-MM-dd".

    Pre:
        - `nom`, `type_crime`, `lieu`, `statut`, et `date_ouverture` doivent être des chaînes de caractères non vides.
        - La base de données doit être accessible.

    Post:
        - L'affaire est ajoutée dans la table `affaire` de la base de données.
        - La transaction est validée et la connexion à la base de données est fermée.

    Raises:
        sqlite3.Error: Si une erreur se produit lors de l'insertion dans la base de données.
    """

def generer_pdf(affaires):
    """
    Génère un fichier PDF contenant les informations des affaires.

    Args:
        affaires (list): Liste de dictionnaires représentant les affaires.

    Pre:
        - `affaires` doit être une liste de dictionnaires contenant les informations des affaires.

    Post:
        - Un fichier PDF nommé "rapport_affaires.pdf" est généré dans le répertoire courant.

    Raises:
        IOError: Si une erreur se produit lors de la création ou de l'écriture du fichier PDF.
    """

def get_database_path(self, db_name: str = 'database.db') -> str:
    """
    Get the absolute path to a database file.

    Args:
        db_name (str): The name of the database file (e.g., "database.db").

    Returns:
        str: The absolute path to the database file.

    Pre:
        - `db_name` doit être une chaîne de caractères non vide.

    Post:
        - Retourne le chemin absolu vers le fichier de base de données.

    Raises:
        None
    """




