/*
* UE - Projet BD/Réseau
* Tavail réalisé par VAYSSE Matthieu & VOLQUARDSEN Alex, L3-I 2022-2023
*/


-- on enleve les tables avant de rajouter les nouvelles --
DROP TABLE IF EXISTS casier CASCADE;
DROP TABLE IF EXISTS etudiant CASCADE;
DROP TABLE IF EXISTS enseignant CASCADE;
DROP TABLE IF EXISTS periode_cours CASCADE;
DROP TABLE IF EXISTS carte CASCADE;
DROP TABLE IF EXISTS utilisateur CASCADE;
DROP TABLE IF EXISTS departement CASCADE;
DROP TABLE IF EXISTS est_dans CASCADE;
DROP TABLE IF EXISTS reserve CASCADE;
DROP TABLE IF EXISTS est_en_cours CASCADE;


-- différents sites possible pour un département --
CREATE TYPE lieu AS ENUM('Saint-Martin', 'Les Chênes', 'Neuville');

-- Département utilisé pour regrouper les utilisateurs/ les periodes cours / les casiers / ...
CREATE TABLE departement
(
    id_departement CHAR(4),
    nom_departement VARCHAR(20),
    sites lieu,
    filieres VARCHAR(200), -- toutes les filières possible sont regroupé dedans 
    CONSTRAINT departement_pk PRIMARY KEY (id_departement)
);


-- carte d'utilisateur relié à ce dernier dans la table utilisateur
CREATE TABLE carte
(
    id_carte CHAR(8),
    num CHAR(14),
    code CHAR(4),
    date_creation DATE,
    date_validite DATE,
    CONSTRAINT carte_pk PRIMARY KEY (id_carte),
    CONSTRAINT id_carte_check CHECK (id_carte ~ '^[0-9 ]*$'),
    CONSTRAINT num_check CHECK (num ~ '([0-9]{4}){2}[0-9]{4}'), -- '123456781212 '
    CONSTRAINT code_check CHECK (code ~ '^[0-9]*$'),
    CONSTRAINT date_creation_check CHECK (date_creation between cast('2010-01-01' as DATE) AND cast('2022-11-25' as DATE)),
    CONSTRAINT date_validite_check CHECK (date_validite > cast('2022-11-25' as DATE))
);


-- table contenant tout les utilisateur quelque soit leur statut --
CREATE TABLE utilisateur
(
    id_uti CHAR(8),
    mdp_uti VARCHAR(110) NULL,
    nom_uti VARCHAR(25),
    prenom_uti VARCHAR(25),
    anniversaire_uti DATE,
    mail_uti VARCHAR(50),
    telephone_uti CHAR(10),
    departement CHAR(4),
    id_carte CHAR(8),
    penalite BOOLEAN DEFAULT false,
    temps_penalite CHAR(8) NULL,
    handicap BOOLEAN DEFAULT false,
    CONSTRAINT utilisateur_pk PRIMARY KEY (id_uti),
    CONSTRAINT id_carte_fk FOREIGN KEY (id_carte) REFERENCES carte (id_carte), -- la carte de l'utilisateur est une carte présente dans la table carte --
    CONSTRAINT id_departement_fk FOREIGN KEY (departement) REFERENCES departement (id_departement),
    CONSTRAINT anniversaire_uti_check CHECK (anniversaire_uti between cast('1920-01-01' as DATE) AND cast('2006-01-01' as DATE)), -- L'anniversaire doit être avant 2014 pour que l'utilisateur ai au moins 17 ans 
    CONSTRAINT telephone_check CHECK (LEFT(telephone_uti,2) LIKE '06' OR LEFT(telephone_uti,2) LIKE '07'), -- on vérifie que le numéro de téléphone commence par soit 06 soit 07
    CONSTRAINT mail_uti_check CHECK (mail_uti LIKE '%@cyu.fr%') -- l'email de l'utilisateur est similaire au mail de la fac (globalmeent le même)-- 
);

-- table de ralation entre département et utilisateur --
CREATE TABLE est_dans
(
    id_utilisateur CHAR(10) NOT NULL, -- id de l'utilisateur --
    id_departement CHAR(4) NOT NULL, -- id du département auquel il appartient --
    CONSTRAINT est_dans_pk PRIMARY KEY (id_utilisateur, id_departement),
    CONSTRAINT id_utilisateur_fk FOREIGN KEY (id_utilisateur) REFERENCES utilisateur (id_uti),
    CONSTRAINT id_departement_fk FOREIGN KEY (id_departement) REFERENCES departement (id_departement) 
);

-- table contenant les casiers et les éléments pertinents associés --
CREATE TABLE casier
(
    id_casier CHAR(9),
    id_dep CHAR(4) NULL,
    occupe BOOLEAN DEFAULT false,
    reserve BOOLEAN DEFAULT false,
    heure_reservation TIME(0) NULL,
    heure_butoire TIME(0) NULL,
    id_uti CHAR(8) NULL,
    CONSTRAINT casier_fk FOREIGN KEY (id_uti) REFERENCES utilisateur (id_uti),
    CONSTRAINT casier_pk PRIMARY KEY (id_casier),
    CONSTRAINT id_casier_check CHECK (id_casier LIKE '%locker_%'), -- le nom du casier commence forcément par locker
    -- l'heure de réservation est compris dans une tranche d'utilisation correspondant aux horaires possible d'accès à l'université --
    CONSTRAINT heure_reservation_check CHECK (heure_reservation between cast('06:00:00' as TIME) AND cast('17:59:59' as TIME)) 
);


-- table heritant de utilisateur --
CREATE TABLE etudiant
(
    id_etudiant CHAR(8),
    annee_etude VARCHAR(9),
    filiere VARCHAR(20),
    groupe_CM CHAR(12),
    groupe_TD CHAR(8),
    utilisation_etudiant INTEGER,
    tuteur BOOLEAN DEFAULT false,
    CONSTRAINT etudiant_pk PRIMARY KEY (id_etudiant),
    -- un étudiant est forcément déjà dans la table des utilisateurs --
    CONSTRAINT etudiant_fk FOREIGN KEY (id_etudiant) REFERENCES utilisateur (id_uti),
    -- un utilisateur n'as le droit qu'à une utilisation au maximum --
    CONSTRAINT utilisation_etudiant_check CHECK (utilisation_etudiant between 0 AND 1) 
);

-- table heritant de utilisateur --
CREATE TABLE enseignant
(
    id_enseignant CHAR(8),
    utilisation_prof INTEGER,
    filieres VARCHAR(150),
    CONSTRAINT enseignant_pk PRIMARY KEY (id_enseignant),
    -- un enseignant est forcément déjà enregistré dans la table utilisateur --
    CONSTRAINT enseignant_fk FOREIGN KEY (id_enseignant) REFERENCES utilisateur (id_uti),
    -- un enseignant a le droit à au plus 3 utilisations simultané --
    CONSTRAINT utilisation_prof_check CHECK (utilisation_prof between 0 AND 3)
);

-- table contenant les différents cours et pour quel filières ils seront --
CREATE TABLE periode_cours
(
    id_cours CHAR(5),
    nom VARCHAR(25),
    departement CHAR(4),
    effectif INTEGER,
    debut TIME,
    fin TIME,
    CONSTRAINT periode_cours_pk PRIMARY KEY (id_cours),
    CONSTRAINT departement_fk FOREIGN KEY (departement) REFERENCES departement (id_departement),
    -- une periode de cours commence dans un certain delais et se finisse dans forcément dans une certaines fourchette donné
    CONSTRAINT debut_check CHECK (debut between cast('08:30:00' as TIME) and cast('16:30:00' as TIME)),
    CONSTRAINT fin_check CHECK (fin between cast('10:00:00' as TIME) and cast('18:00:00' as TIME))
);

-- table de relation entre periode_cours et etudiant --
CREATE TABLE est_en_cours
(
    id_uti CHAR(10) NOT NULL,
    id_cours CHAR(5) NOT NULL,
    CONSTRAINT est_en_cours_pk PRIMARY KEY (id_uti, id_cours),
    -- id de l'utilisateur et du cours auquel il assiste --
    CONSTRAINT id_uti_fk FOREIGN KEY (id_uti) REFERENCES utilisateur (id_uti),
    CONSTRAINT id_cours_fk FOREIGN KEY (id_cours) REFERENCES periode_cours (id_cours)

);

-- table de relation entre casier et utilisateur --
CREATE TABLE reserve
(
    id_carte CHAR(8) NOT NULL,
    id_casier CHAR(9) NOT NULL,
    CONSTRAINT reserve_pk PRIMARY KEY (id_carte, id_casier),
    CONSTRAINT casier_fk FOREIGN KEY (id_casier) REFERENCES casier (id_casier),
    CONSTRAINT carte_fk FOREIGN KEY (id_carte) REFERENCES carte (id_carte)
);
