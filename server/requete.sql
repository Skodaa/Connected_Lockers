
-- Le casier est maintenant occupé --
UPDATE casier SET occupe = TRUE WHERE (id_casier LIKE '{locker}')

-- L'utilisateur qui utilise le casier est maintenant utilisateur --
UPDATE casier SET id_uti = '{utilisateur}' WHERE (id_casier LIKE '{locker}')

-- on récupere le nombre d'utilisation de l'utilisateur  --
SELECT utilisation_en_cours FROM utilisateur WHERE (id_utilisateur LIKE '{utilisateur}')

-- set le nombre d'utilisation de l'utilisateur  --
UPDATE utilisateur SET utilisation_en_cours = {value} WHERE (id_utilisateur LIKE '{utilisateur}')


-- Récupere l'id casier si ce dernier est selon rentrée en parametre et est libre --
SELECT id_casier FROM casier WHERE (id_casier LIKE '{locker}' AND occupe = FALSE AND reserve = FALSE)



SELECT id_utilisateur
FROM carte
JOIN utilisateur
    ON 
    carte.id_utilisateur = utilisateur.id_utilisateur
    WHERE  
        utilisateur.id_utilisateur = '22 100 517';

SELECT id_utilisateur
FROM carte
    WHERE id_utilisateur = '22 100 517';


-- Chercher à l'aide de l'id de la carte si l'utilisateur est un étudiant --
SELECT e.id_etudiant
FROM etudiant as e
JOIN utilisateur as u
    ON e.id_etudiant = u.id_utilisateur
    WHERE u.id_utilisateur = 
        (
            SELECT c.id_utilisateur
            FROM carte as c
                WHERE c.id_carte = '{utilisateur}'
        );

SELECT e.id_etudiant FROM etudiant as e JOIN utilisateur as u ON e.id_etudiant = u.id_utilisateur WHERE u.id_utilisateur = (SELECT c.id_utilisateur FROM carte as c WHERE c.id_carte = '{utilisateur}')

-- Cherche à l'aide de l'id de la carte si l'utilisateur est un enseignant -- 
SELECT e.id_enseignant
FROM enseignant as e
JOIN utilisateur as u
    ON e.id_enseignant = u.id_utilisateur
    WHERE u.id_utilisateur = 
        (
            SELECT c.id_utilisateur
            FROM carte as c
                WHERE c.id_carte = '{utilisateur}'
        );

-- Vérifie si l'utilisateur et le casier sont du même département --
SELECT c.id_casier
FROM casier AS c
JOIN utilisateur as u
    ON c.id_dep IS NULL OR c.id_dep = u.departement
    WHERE 
        u.id_utilisateur = '22 100 493'
        AND
        c.id_casier = 'locker_01';


-- Remet le casier en état 'libre' --
UPDATE casier 
SET 
    occupe = FALSE, 
    reserve = FALSE, 
    heure restant = NULL, 
    heure_reservation = NULL, 
    heure_fermeture = NULL, 
    id_uti = NULL
WHERE id casier LIKE {locker};

-- Vérifie si le casier est occupé ou réservé --
SELECT id_casier 
FROM casier 
    WHERE 
    (id_casier LIKE '{locker}' 
    AND 
    occupe = FALSE 
    AND 
    reserve = FALSE);

-- Modifie le nombre d'utilisation en cours --
UPDATE etudiant 
SET utilisation_etudiant = {res[0]} 
    WHERE 
    (id_etudiant LIKE '{utilisateur}');

-- Modifie le nombre d'utilisation en cours -- 
UPDATE enseignant 
SET utilisation_prof = {res[0]} 
    WHERE   
    (id_enseignant LIKE '{utilisateur}');

-- Ferme le casier --
UPDATE casier 
SET 
    occupe = TRUE,
    id_uti = '{utilisateur}'
    WHERE 
        (id_casier LIKE '{locker}');

-- Récupere le nombre d'utilisation d'un enseignant --
SELECT utilisation_enseignant
FROM enseignant 
    WHERE 
        (id_enseignant LIKE '{uti}');