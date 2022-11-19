<?php

/**
 * Fonction permettant de se connecter à la base de données
 * @return object connect la connection à la base de données
 */
function connect():?string
{
    
    $host = $_ENV["HOST"];
    $dbname = $_ENV["DB"];
    $username = $_ENV["USER"];
    $password = $_ENV["PASSWORD"];

    $dsn = "host=$host port=5432 dbname=$dbname user=$username password=$password";
    return $dsn;
}

/**
 * Fonction permettant de se déconnecter de la base de données.
 */
function disconnect():?bool
{
    return null;
}


/**
 * Fonction permettant d'ajouter un nouvel utilisateur à la base de données
 * @param string id : id de l'utilisateur
 * @param string nom : nom de l'utilisateur
 * @param string prenom : prenom de l'utilisateur
 * @param string birthday : date de naissance
 * @param string mail : sont email
 * @param integer phone : sont numéro de téléphone
 * @param boolean handicap : s'il est handicapé
 */
function add_uti(string $id,string $nom, string $prenom,string $birthday,
                            string $mail,int $phone,bool $handicap,string $dep):string
{
    $dsn = connect();
    $connexion = pg_connect($dsn) or die("Could not connect:" .pg_last_error()); 
    $sql = "INSERT INTO utilisateur (id_utilisateur, nom, prenom, birthday, mail, telephone, departement, utilisation_en_cours, penality, penality_time, handicap) VALUES ('$id','$nom','$prenom','$birthday','$mail',$phone,'$dep',0,'false',NULL,'$handicap');";
    $send = pg_query($connexion,$sql);
    if($send)
    {
        $connexion = disconnect();
        return "Utilisateur créer";
    }
    else{
        $connexion = disconnect();
        return "Problème lors de la création";
    }

}
?>