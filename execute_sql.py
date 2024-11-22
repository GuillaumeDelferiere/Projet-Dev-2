import sqlite3

def charger_et_executer_sql(chemin_sql, nom_bdd):
    # Connexion à la base de données SQLite (fichier local)
    conn = sqlite3.connect(nom_bdd)
    cursor = conn.cursor()

    # Charger le contenu du fichier .sql
    with open(chemin_sql, 'r') as f:
        script_sql = f.read()

    # Exécuter le script SQL
    cursor.executescript(script_sql)

    # Sauvegarder et fermer la connexion
    conn.commit()
    conn.close()

    print(f"Base de données '{nom_bdd}' configurée avec succès à partir de '{chemin_sql}'.")

# Exécuter la fonction avec le fichier SQL
if __name__ == "__main__":
    charger_et_executer_sql(r'C:\Users\Win\PycharmProjects\DevIIProjet\database.sql', 'database.db')
