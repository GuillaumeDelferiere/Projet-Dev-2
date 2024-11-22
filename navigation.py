import tkinter as tk
from tkinter import ttk
import sqlite3


def afficher_preuves():
    # Efface le contenu du body
    for widget in body_frame.winfo_children():
        widget.destroy()

    # Ajouter les colonnes (en-têtes)
    colonnes = ["id", "enquete_id", "nom", "description", "type", "lien", "lieu collecte", "scientifique en charge"]
    for i, col in enumerate(colonnes):
        tk.Label(body_frame, text=col, font=("Arial", 12, "bold"), bg="lightblue").grid(row=0, column=i, padx=20, pady=10)

    # Se connecter à la base de données
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Récupérer les preuves depuis la table correspondante
        cursor.execute("SELECT id, enquete_id, nom, description, type, lien, lieu_collecte  FROM preuves")
        preuves = cursor.fetchall()

        # Ajouter les preuves dans le tableau (interface graphique)
        for i, preuve in enumerate(preuves):
            for j, valeur in enumerate(preuve):
                tk.Label(body_frame, text=valeur, font=("Arial", 10), bg="white").grid(row=i+1, column=j, padx=20, pady=5)

    except sqlite3.Error as e:
        print(f"Erreur lors de la récupération des preuves : {e}")

    finally:
        conn.close()

def afficher_suspects():
    # Efface le contenu du body
    for widget in body_frame.winfo_children():
        widget.destroy()

    # Ajouter les colonnes (en-têtes)
    colonnes = ["id", "enquete_id", "nom", "prenom", "age", "date de naissance", "lieu de naissance"]
    for i, col in enumerate(colonnes):
        tk.Label(body_frame, text=col, font=("Arial", 12, "bold"), bg="lightblue").grid(row=0, column=i, padx=20, pady=10)

    # Se connecter à la base de données
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Récupérer les suspects depuis la table correspondante
        cursor.execute("SELECT id, enquete_id, nom, prenom, age, date_naissance, lieu_naissance FROM suspects")
        suspects = cursor.fetchall()

        # Ajouter les suspects dans le tableau (interface graphique)
        for i, suspect in enumerate(suspects):
            for j, valeur in enumerate(suspect):
                tk.Label(body_frame, text=valeur, font=("Arial", 10), bg="white").grid(row=i+1, column=j, padx=20, pady=5)

    except sqlite3.Error as e:
        print(f"Erreur lors de la récupération des suspects : {e}")

    finally:
        conn.close()

def quitter_application():
    root.destroy()

# Fenêtre principale
root = tk.Tk()
root.title("Gestion des enquêtes - Inspecteur Scott")
root.geometry("750x400")
root.configure(bg="darkblue")

# Texte en haut de la page
label_titre = tk.Label(root, text="Enquête Criminelle", font=("Arial", 16, "bold"), bg="darkblue", fg="white")
label_titre.pack(pady=20)

# Conteneur pour le "body" central
body_frame = tk.Frame(root, bg="lightblue", relief=tk.SUNKEN, borderwidth=2)
body_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)

# Conteneur pour le pied de page
bottom_frame = tk.Frame(root, bg="darkgray")
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)


def charger_enquetes():
    """Charge les noms des enquêtes depuis la base de données et les ajoute au menu déroulant."""
    try:
        # Connexion à la base de données
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Récupérer les noms des enquêtes
        cursor.execute("SELECT id, type_crime FROM enquetes")
        enquetes_bd = cursor.fetchall()

        # Mettre à jour le menu déroulant avec les noms des enquêtes
        enquetes.clear()
        for enquete in enquetes_bd:
            enquetes.append(f"ID: {enquete[0]} - {enquete[1]}")

        # Actualiser les valeurs du Combobox
        enquete_combo['values'] = enquetes

    except sqlite3.Error as e:
        print(f"Erreur lors du chargement des enquêtes : {e}")
    finally:
        conn.close()


# Menu déroulant
label = tk.Label(bottom_frame, text="Sélectionnez une enquête :", font=("Arial", 10), bg="darkgray", fg="white")
label.pack(side=tk.LEFT, padx=5)

enquetes = []  # Liste pour stocker les enquêtes récupérées
enquete_combo = ttk.Combobox(bottom_frame, values=enquetes, state="readonly", width=30)
enquete_combo.pack(side=tk.LEFT, padx=5)

# Charger les enquêtes lors de l'ouverture de l'application
charger_enquetes()
# Boutons alignés horizontalement
btn_preuves = tk.Button(bottom_frame, text="Afficher les preuves", command=afficher_preuves)
btn_preuves.pack(side=tk.LEFT, padx=5)

btn_suspects = tk.Button(bottom_frame, text="Afficher les suspects", command=afficher_suspects)
btn_suspects.pack(side=tk.LEFT, padx=5)

btn_quitter = tk.Button(bottom_frame, text="Quitter", command=quitter_application)
btn_quitter.pack(side=tk.LEFT, padx=5)

# Lancement de la fenêtre principale
root.mainloop()
