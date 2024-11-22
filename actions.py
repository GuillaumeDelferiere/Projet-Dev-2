import sqlite3

def ajouter_enquete(type_crime, lieu, statut, date_ouv, date_clot, enqueteur):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(""" 
            INSERT INTO enquetes (type_crime, lieu_crime, statut, date_ouverture, date_cloture, enqueteur_assigne)
            VALUES (?,?,?,?,?,?)
            """, (type_crime, lieu, statut, date_ouv, date_clot, enqueteur))
        conn.commit()
        print(f"Enquete '{type_crime}' ajoutée avec succès.")
    except sqlite3.Error as e:
        print(f"Erreur lors de l'ajout de l'enquete : {e}")
    finally:
        conn.close()


# Ajouter une enquête
ajouter_enquete("Vol de bijoux", 'Esplanade', "En cours", "2024-11-22", "2024-11-30", 'Hergé')

def ajouter_suspect(enquete_id, nom, prenom, age, date_naissance, lieu_naissance):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("""
                   SELECT COUNT(*) FROM suspects
                   WHERE enquete_id = ? AND nom = ? AND prenom = ?
               """, (enquete_id, nom, prenom))

        resultat = cursor.fetchone()
        if resultat[0] > 0:
            print(f"Le suspect '{nom} {prenom}' est déjà associé à l'enquête {enquete_id}.")
            return


        cursor.execute("""
            insert into suspects (enquete_id, nom, prenom, age, date_naissance, lieu_naissance)
            values (?,?,?,?,?,?)
            """, (enquete_id, nom, prenom, age, date_naissance, lieu_naissance))
        conn.commit()
        print(f"Suspect '{nom}' ajoutée avec succès.")
    except sqlite3.Error as e:
        print(f"Erreur lors de l'ajout du suspect : {e}")
    finally:
        conn.close()

ajouter_suspect(1,'sasuke', 'uchiha', 16, '01/01/2008', 'konoha')


def ajouter_preuves(enquete_id, nom, description, type_preuve, lien, lieu):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("""
            insert into preuves (enquete_id, nom, description, type, lien, lieu_collecte)
            values (?,?,?,?,?,?)
            """, (enquete_id, nom, description, type_preuve, lien, lieu))
        conn.commit()
        print(f"Preuve '{nom}' ajoutée avec succès.")
    except sqlite3.Error as e:
        print(f"Erreur lors de l'ajout du preuve : {e}")
    finally:
        conn.close()

ajouter_preuves(1, "couteau", "manche en bois", "arme blanche", "outil de pression", "foot locker")
