class Personnes:
    def __init__(self, nom, prenom, age):
        self.__nom = nom  # Encapsulation : attribut privé
        self.__prenom = prenom  # Encapsulation : attribut privé
        self.__age = age

    """
    Getter : permet de lire la valeur de l'attribut.
    Setter : permet de modifier la valeur.
    """

    def get_nom(self):
        return self.__nom


    def set_nom(self, nom):
        self.__nom = nom


    def get_prenom(self):
        return self.__prenom


    def set_prenom(self, prenom):
        self.__prenom = prenom


    def get_age(self):
        return self.__age


    def set_age(self, age):
        self.__age = age

# Classe fille : Temoin
class Temoin(Personnes):
    def __init__(self, nom, prenom, age, enquete):
        super().__init__(nom, prenom, age)
        self.__enquete = enquete


    def get_enquete(self):
        return self.__enquete


    def set_enquete(self, enquete):
        self.__enquete = enquete

# Classe fille : Suspect
class Suspect(Personnes):
    def __init__(self, nom, prenom, age, enquete):
        super().__init__(nom, prenom, age)
        self.__enquete = enquete

    # Getter pour enquete
    def get_enquete(self):
        return self.__enquete

    # Setter pour enquete
    def set_enquete(self, enquete):
        self.__enquete = enquete

#Exemple
if __name__ == "__main__":
    temoin = Temoin("Dupont", "Jean", 35, "Enquête 1")
    suspect = Suspect("Martin", "Paul", 40, "Enquête 2")

    print(f"Témoin : {temoin.get_nom()} {temoin.get_prenom()}, Âge : {temoin.get_age()}, Enquête : {temoin.get_enquete()}")
    print(f"Suspect : {suspect.get_nom()} {suspect.get_prenom()}, Âge : {suspect.get_age()}, Enquête : {suspect.get_enquete()}")
