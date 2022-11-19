/*
* UE - Projet BD/Réseau
* Tavail réalisé par VAYSSE Matthieu & VOLQUARDSEN Alex, L3-I 2022-2023
*/

DROP TABLE IF EXISTS casier CASCADE;
DROP TABLE IF EXISTS etudiant CASCADE;
DROP TABLE IF EXISTS enseignant CASCADE;
DROP TABLE IF EXISTS periode_cours CASCADE;
DROP TABLE IF EXISTS carte CASCADE;
DROP TABLE IF EXISTS utilisateur CASCADE;
DROP TABLE IF EXISTS departement CASCADE;
DROP TABLE IF EXISTS est_dans CASCADE;
DROP TABLE IF EXISTS reserve CASCADE;



CREATE TABLE departement
(
    id_departement CHAR(4),
    nom_departement VARCHAR(20),
    lieu VARCHAR(20),
    filieres VARCHAR(200),
    CONSTRAINT departement_pk PRIMARY KEY (id_departement)
);

/* 
    Voir pour l'emploi du temps 
*/
CREATE TABLE utilisateur
(
    id_utilisateur CHAR(10) NOT NULL,
    nom VARCHAR(25) NOT NULL,
    prenom VARCHAR(25) NOT NULL,
    birthday DATE NOT NULL,
    mail VARCHAR(50) NOT NULL,
    telephone INTEGER NULL,
    departement CHAR(4) NOT NULL,
    utilisation_en_cours INTEGER NULL,
    penality BOOLEAN DEFAULT false,
    penality_time CHAR(8) NULL,
    handicap BOOLEAN DEFAULT false,
    CONSTRAINT utilisateur_pk PRIMARY KEY (id_utilisateur),
    CONSTRAINT id_departement_fk FOREIGN KEY (departement) REFERENCES departement (id_departement)
);

CREATE TABLE est_dans
(
    id_utilisateur CHAR(10) NOT NULL,
    id_departement CHAR(4) NOT NULL,
    CONSTRAINT est_dans_pk PRIMARY KEY (id_utilisateur, id_departement),
    CONSTRAINT id_utilisateur_fk FOREIGN KEY (id_utilisateur) REFERENCES utilisateur (id_utilisateur),
    CONSTRAINT id_departement_fk FOREIGN KEY (id_departement) REFERENCES departement (id_departement) 
);

CREATE TABLE casier
(
    id_casier CHAR(9),
    id_dep CHAR(4) NULL REFERENCES departement(id_departement),
    occupe BOOLEAN DEFAULT false,
    reserve BOOLEAN DEFAULT false,
    partage VARCHAR(200) NULL,
    heure_restant TIME NULL,
    heure_reservation TIME NULL,
    heure_fermeture TIME NULL,
    id_uti CHAR(10) NULL REFERENCES utilisateur (id_utilisateur),
    CONSTRAINT casier_pk PRIMARY KEY (id_casier)
);

CREATE TABLE etudiant
(
    id_etudiant CHAR(10),
    annee_etude VARCHAR(9),
    filiere VARCHAR(20),
    groupe_CM VARCHAR(12),
    groupe_TD VARCHAR(9),
    utilisation_etudiant INTEGER,
    tuteur BOOLEAN DEFAULT false,
    CONSTRAINT etudiant_pk PRIMARY KEY (id_etudiant),
    CONSTRAINT etudiant_fk FOREIGN KEY (id_etudiant) REFERENCES utilisateur (id_utilisateur)
);

CREATE TABLE enseignant
(
    id_enseignant CHAR(10),
    utilisation_prof INTEGER,
    CONSTRAINT enseignant_pk PRIMARY KEY (id_enseignant),
    CONSTRAINT enseignant_fk FOREIGN KEY (id_enseignant) REFERENCES utilisateur (id_utilisateur)
);

CREATE TABLE periode_cours
(
    id_cours CHAR(5),
    nom VARCHAR(25),
    departement CHAR(4),
    effectif INTEGER,
    debut TIME,
    fin TIME,
    CONSTRAINT periode_cours_pk PRIMARY KEY (id_cours),
    CONSTRAINT departement_fk FOREIGN KEY (departement) REFERENCES departement (id_departement)
);

CREATE TABLE carte
(
    id_carte CHAR(8),
    id_utilisateur CHAR(10) REFERENCES utilisateur (id_utilisateur),
    num CHAR(14),
    code CHAR(4),
    date_creation DATE,
    date_validite DATE,
    CONSTRAINT carte_pk PRIMARY KEY (id_carte)
);

CREATE TABLE reserve
(
    id_carte CHAR(8) NOT NULL,
    id_casier CHAR(9) NOT NULL,
    CONSTRAINT reserve_pk PRIMARY KEY (id_carte, id_casier),
    CONSTRAINT casier_fk FOREIGN KEY (id_casier) REFERENCES casier (id_casier),
    CONSTRAINT carte_fk FOREIGN KEY (id_carte) REFERENCES carte (id_carte)
);
