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
 * @param string : le message indiquant si tout c'est bien passer ou non
 */
function activate_uti(string $id,string $password):string
{
    $dsn = connect();
    $connexion = pg_connect($dsn) or die("Could not connect:" .pg_last_error());
    $verif_uti = "SELECT id_uti FROM utilisateur WHERE ( id_uti LIKE '$id');";
    $verif = pg_query($connexion, $verif_uti);
    $ting = pg_fetch_result($verif,0);
    if($verif)
    {
        $password = password_hash($password, PASSWORD_BCRYPT);
        $sql = "SELECT mdp_uti FROM utilisateur WHERE (id_uti LIKE '$id')";
        $send = pg_query($connexion,$sql);
        $mdp = pg_fetch_result($send,0);
        if($mdp != NULL)
        {
            $connexion = disconnect();
            echo $send;
            return "Compte déjà activer";
        }
        else{
            $update = "UPDATE utilisateur SET mdp_uti = '$password' WHERE id_uti = '$id'";
            $updating = pg_query($connexion,$update);
            $connexion = disconnect();
            return "compte activer";
        }
    }
    else
    {
        $connexion = disconnect();
        return "Erreur : utilisateur introuvable";
    }


}
/**
 * Fonction permettant de vérifier si le mot de passe de l'utilisateur est le bon
 * @param string id : l'id de l'utikisateur dont on vérifie le mot de passe
 * @param string password : le mot de passe à vérifier
 */
function verif_mdp(string $id,string $password):int
{
    $dsn = connect();
    $connexion = pg_connect($dsn) or die("Could not connect:" .pg_last_error());
    $user = "SELECT id_uti FROM utilisateur WHERE (id_uti = '$id');";
    $tst_usr = pg_query($connexion, $user);
    if($tst_usr)
    {
        $sql = "SELECT mdp_uti FROM utilisateur WHERE (id_uti = '$id');";
        $tst_password = pg_query($connexion, $sql);
        $psw = pg_fetch_result($tst_password, 0);
        if($tst_password)
        {
            $verified = password_verify($password,$psw);
            if($verified == TRUE)
            {
                $connexion = disconnect();
                return 1;
            }
            else
            {
                $connexion = disconnect();
                return 0;
            }
        }
        else
        {
            $connexion = disconnect();
            return 0;
        }
    }
    else
    {
        $connexion = disconnect();
        return 0;
    }
    

}

/**
 * Fonction retournant le nom de l'utilisateur
 * @param string : l'id de l'utilisateur
 * @return string : le nom de l'utilisateur
 */
function get_nom(string $id):string
{
    $dsn = connect();
    $connexion = pg_connect($dsn);
    $sql = "SELECT nom_uti FROM utilisateur WHERE (id_uti = '$id');";
    $query = pg_query($connexion,$sql);

    if(isset($query))
    {
        $nom = pg_fetch_result($query, 0);
        return $nom;
    }
    else
    {
        return NULL;
    }
}

/**
 * Fonction retournant le prénom de l'utilisateur
 * @param string : l'id de l'utilisateur
 * @return string : le prénom de l'utilisateur
 */
function get_prenom(string $id):string
{
    $dsn = connect();
    $connexion = pg_connect($dsn);
    $sql = "SELECT prenom_uti FROM utilisateur WHERE (id_uti = '$id');";
    $query = pg_query($connexion,$sql);

    if(isset($query))
    {
        $prenom = pg_fetch_result($query, 0);
        return $prenom;
    }
    else
    {
        return NULL;
    }
}

/**
 * Fonction retournant le nombre d'utilisation de l'utilisateur
 * @param string : l'id de l'utilisateur
 * @return string : le nombre d'utilisation de l'utilisateur
 */
function get_utilisation(string $id):string
{

    $est_prof = prof($id);

    $dsn = connect();
    $connexion = pg_connect($dsn);

    if($est_prof == TRUE)
    {
        $sql = "SELECT utilisation_prof FROM enseignant WHERE (id_enseignant = '$id');";
    }
    else
    {
        $sql = "SELECT utilisation_etudiant FROM etudiant WHERE (id_etudiant = '$id');";
    }
    
    $query = pg_query($connexion,$sql);

    if(isset($query))
    {
        $utilisation = pg_fetch_result($query, 0);
        return $utilisation;
    }
    else
    {
        return NULL;
    }
}

/**
 * Fonction permettant de savoir si un utilisateur est un enseignant ou non
 * @param string : l'id de l'utilisateur
 * @return bool : si prof TRUE sinon FALSE
 */
function prof(string $id):bool
{
    $dsn = connect();
    $connexion = pg_connect($dsn);
    $sql = "SELECT id_enseignant FROM enseignant WHERE ( id_enseignant = '$id');";
    $query = pg_query($connexion,$sql);
    $rep = pg_fetch_result($query, 0);
    if($rep == $id)
    {
        return TRUE;
    }
    else
    {
        return FALSE;
    }
}

function departement($id)
{
    $dsn = connect();
    $connexion = pg_connect($dsn);
    $sql = "SELECT departement FROM utilisateur WHERE (id_uti = '$id');";
    $query = pg_query($connexion,$sql);

    $dep = pg_fetch_result($query, 0);

    return $dep;
}

/**
 * Fonction permettant de créer une liste contenant tout les casier libre
 * @param string : le departement de l'utilisateur
 * @return array : la liste des casiers disponible
 */
function free_lockers(string $dep):array
{
    $res = array();
    $dsn = connect();
    $connexion = pg_connect($dsn);
    $sql = "SELECT id_casier FROM casier WHERE ( (occupe IS FALSE AND reserve IS FALSE) AND (id_dep = '$dep' OR id_dep IS NULL));";
    $query = pg_query($connexion,$sql);
    for($i = 0; $i < pg_num_rows($query);$i++)
    {
        $lock = pg_fetch_result($query, $i, 0);
        array_push($res,$lock);
    }
    


    return $res;
}


/**
 * Fonction permettant de réserver le casier séléctionner par l'utilisateur
 * @param string : l'id du casier que l'utilisateur veut réserver
 * @param string : l'id de l'utilisateur qui veut réserver le casier
 */
function reserv_locker(string $id_locker, string $id_uti):void
{
    $est_prof = prof($id_uti);
    $dsn = connect();
    $connexion = pg_connect($dsn);
    $sql = "UPDATE casier SET reserve = TRUE, id_uti = '$id_uti' WHERE (id_casier = '$id_locker');";
    $query = pg_query($sql);
    if($est_prof == TRUE)
    {
        $sql2 = "UPDATE enseignant SET utilisation_prof = utilisation_prof+1 WHERE ( id_enseignant = '$id_uti');";
    }
    else
    {
        $sql2 = "UPDATE etudiant SET utilisation_etudiant = utilisation_etudiant+1 WHERE ( id_etudiant = '$id_uti');";
    }
    
    $query = pg_query($sql2);
}


/**
 * Fonction permettant de créer une liste des casiers réservé par l'utilisateur
 * @param string : l'id de l'utilisateur
 * @return array : une liste des casiers reservé
 */
function reserved_lockers(string $id_user)
{
    $res = array();
    $dsn = connect();
    $connexion = pg_connect($dsn);
    $sql = "SELECT id_casier FROM casier WHERE ( reserve IS TRUE and id_uti = '$id_user' );";
    $query = pg_query($connexion,$sql);
    for($i = 0; $i < pg_num_rows($query);$i++)
    {
        $lock = pg_fetch_result($query, $i, 0);
        array_push($res,$lock);
    }
    

    return $res;
}

/**
 * Fonction retournant le nombre d'utilisation en cours de l'utilisateur
 * @param string : l'id de l'utilisateur
 * @return int : le nombre d'utilisation
 */
function util(string $id):int
{
    $est_prof = prof($id);
    $dsn = connect();
    $connexion = pg_connect($dsn);

    if($est_prof == 1)
    {
        $sql = "SELECT utilisation_prof FROM enseignant WHERE ( id_enseignant = '$id');";
    }
    else
    {
        $sql = "SELECT utilisation_etudiant FROM etudiant WHERE (id_etudiant = '$id');";
    }
    $query = pg_query($sql);
    $res = pg_fetch_result($query, 0);
    return $res;
}

/**
 * Fonction permettant de liberer le casier séléctionner par l'utilisateur
 * @param string : l'id du casier que l'utilisateur veut liberer
 * @param string : l'id de l'utilisateur
 */
function unreserv_locker(string $id_locker, string $id_user):void
{
    $est_prof = prof($id_user);
    $dsn = connect();
    $connexion = pg_connect($dsn);
    $sql = "UPDATE casier SET reserve = FALSE, id_uti = NULL WHERE (id_casier = '$id_locker');";
    $query = pg_query($sql);
    if($est_prof == TRUE)
    {
        $uti_act = util($id_user);
        $var = $uti_act - 1;
        $sql2 = "UPDATE enseignant SET utilisation_prof = $var WHERE ( id_enseignant = '$id_user');";
    }
    else
    {
        $uti_act = util($id_user);
        $var = $uti_act -1;
        $sql2 = "UPDATE etudiant SET utilisation_etudiant = $var WHERE ( id_etudiant = '$id_user');";
    }
    $query = pg_query($sql2);
}


/**
 * Fonction vérifiant si l'utilisateur à une pénalité en cours
 * @param string id : l'id de l'utilisateur
 * @return bool si l'utilisateur à une pénalité
 */
function verif_pena(string $id):bool
{
    $dsn = connect();
    $connexion = pg_connect($dsn);
    $sql = "SELECT penalite FROM utilisateur WHERE ( id_uti = '$id');";
    $query = pg_query($connexion,$sql);
    $res = pg_fetch_result($query, 0);
    if($res == "t")
    {
        return TRUE;
    }
    else{
        return FALSE;
    }
}
?>
