import sqlite3
print('1er')
# Connexion à la base de données (ou création si elle n'existe pas)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
print('2eme')
# Création de la table "affaire"
cursor.execute('''
CREATE TABLE IF NOT EXISTS affaire (
    id_affaire INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_affaire TEXT NOT NULL,
    type_crime TEXT NOT NULL,
    lieu TEXT NOT NULL,
    etat TEXT NOT NULL,
    date_ouverture DATE NOT NULL
)
''')

# Création de la table "preuve"
cursor.execute('''
CREATE TABLE IF NOT EXISTS preuve (
    id_preuve INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_preuve TEXT NOT NULL
)
''')

# Création de la table "rapport"
cursor.execute('''
CREATE TABLE IF NOT EXISTS rapport (
    id_rapport INTEGER PRIMARY KEY AUTOINCREMENT,
    contenu TEXT NOT NULL
)
''')

# Validation des modifications et fermeture de la connexion
conn.commit()
conn.close()

print("Base de données et tables créées avec succès !")