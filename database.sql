-- Création de la table "enquetes"
CREATE TABLE IF NOT EXISTS enquetes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_crime TEXT NOT NULL,
    lieu_crime TEXT,
    statut TEXT,
    date_ouverture TEXT NOT NULL,
    date_cloture TEXT,
    enqueteur_assigne TEXT

);

-- Création de la table "suspects"
CREATE TABLE IF NOT EXISTS suspects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    enquete_id integer,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    surnom TEXT,
    age integer,
    date_naissance TEXT,
    lieu_naissance TEXT,
    adresse TEXT,

    taille integer,
    poids integer,
    signes_particuliers text,

    role text,
    alibi_declare text,
    statut_legal text,
    FOREIGN KEY (enquete_id) REFERENCES enquetes(id)
);

-- Création de la table "preuves"
CREATE TABLE IF NOT EXISTS preuves (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    enquete_id integer,
    nom TEXT NOT NULL,
    description TEXT,
    type text,
    lien text,

    lieu_collecte text,
    date_heure_decouverte text,
    qui_a_trouver text,

    resultat_analyse text,
    etat_actuel text,
    scientifique_en_charge text,
    FOREIGN KEY (enquete_id) REFERENCES enquetes(id)
);
