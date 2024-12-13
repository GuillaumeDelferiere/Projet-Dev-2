# Spécification personnelle de Guillaume Delferiere sur base du diagramme UML
def ajouter_preuve(self, id_preuve, description_preuve, type_preuve, id_enquete):
    """
    Cette fonction permet d'ajouter une nouvelle preuve à une enquête
    :param id_preuve, description_preuve, type_preuve, id_enquete:

    PRE : L'enquête associée doit exister et être active
    POST : Retourne un booléen. True si l'ajout a réussi sinon False
    """
    pass

def consulter_preuves(id_enquete):
    """
    Cette fonction permet à un utilisateur de consulter la liste des preuves associées à une enquête
    :param id_enquete:
    :return list[Preuve]

    PRE: L'utilisateur doit avoir un niveau d'accès suffisant pour accèder aux preuves
         L'enquête doit exister et être active
    POST:Retourne une liste contenant les preuves
    """
    pass

def clore_enquete(id_enquete):
    """
    Cette fonction permet de clôturer une enquête une fois qu'elle est résolue ou abandonnée
    :param id_enquete:
    :return:

    PRE : L'enquête doit exister et être active
    POST : retourne un booléen. True si le statut de l'enquête passe à "cloture" sinon False
    """
    pass

def ajouter_suspect(id_suspect, nom_prenom, description, alibi, lien_enquete):
    """

    :param id_suspect:
    :param nom_prenom:
    :param description:
    :param alibi:
    :param lien_enquete:
    :return:

    PRE: L'enquête doit exister et être active
    POST: retourne un booléen. True si le suspect a été ajouté à la liste de suspects associés à l'enquête
    """
    pass

def generer_rapport(id_enquete):
    """

    :param id_enquete:
    :return:

    PRE : L'enquête doit être cloturée pour permettre la génération du rapport
    POST : Retourne un rapport généré dans un format texte.
    """
    pass