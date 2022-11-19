-- Setting up the server --

SET datestyle = 'dmy';

-- Different useful types --

CREATE TYPE DEP as ENUM('Maths','Informatique','Physique','Droit','Langue','Lettre','Tech','IUT','Economie');


-- creating the differents tables --


CREATE TABLE departement(
    id_departement CHAR(4) NOT NULL PRIMARY KEY ,
    nom_departement DEP NOT NULL,
    filiere_departement CHAR(30) NOT NULL,
    site_departement CHAR(30) NOT NULL
);

CREATE TABLE casier(
    id_casier CHAR(20) NOT NULL PRIMARY KEY,
    occupe BOOLEAN NOT NULL,
    partage VARCHAR(200) NULL,
    reserve BOOLEAN NOT NULL,
    temps CHAR(30) NULL,
    heure_reservation TIME NULL,
    heure_fermeture TIME NULL
);

