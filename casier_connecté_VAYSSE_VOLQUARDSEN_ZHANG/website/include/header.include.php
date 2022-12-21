<?php
session_start();

include(".//include//function.include.php");

if($_SESSION["logged"] == True)
{
    $user_id = $_SESSION["id_user"];
    $user_logged = True;
    $nom = get_nom($user_id);
    $prenom = get_prenom($user_id);
    $utilisation = get_utilisation($user_id);
    $est_prof = prof($user_id);
    $invalid_locker = FALSE;
    $penalite = verif_pena($user_id);

}
else
{
    $user_logged = FALSE;
}


$time = time() + 3600*24;

$title = "CYhub - Lockers";

if(isset($_POST['id']))
{
    $id = $_POST['id'];
}
if(isset($_POST['password']))
{
    $password = $_POST['password'];
    if(isset($id))
    {
        $is_ok = verif_mdp($id,$password);
    }
}
if(isset($_POST['locker']))
{
    
    $locker =$_POST['locker'];
    if($locker == "")
    {
        $invalid_locker = TRUE;
    }
    else
    {
        $invalid_locker = FALSE;
    }
}


?>

<!DOCTYPE html>
<html lang="fr">
    <head>
        <title> <?php echo $title ?> </title>
        <meta charset="utf-8" />
        <link rel="icon" href="image//logo.png" />
        <link rel="stylesheet" href="style.css" />     	
 		<meta name="author" content="alex volquardsen,matthieu vaysse,zhang qinyu" />
        <meta name="date" content="2022-11-10T14:10:23+0200" /> 
    </head>
    <body>
        <header style="width: 0px;height: 0px;">
                <a class="logo" href="index.php" ><img class="logo" src="image//logo.png" width="150px" alt="LOGO" /></a>
                <nav>

                    <ul class="tete">
                        <li><a href="index.php">Accueil</a></li>
                        <?php
                        if($user_logged == FALSE)
                        {
                            echo "<li><a href=\"connexion.php\">Connexion</a></li>";
                        }
                        else
                        {
                            if($est_prof == TRUE)
                            {
                                if(($utilisation < 3)and($penalite == FALSE))
                                {
                                    echo "<li><a href=\"reserv.php\">Reserver</a></li>";
                                }
                                else{
                                    echo "<li><a href=\"unreserv.php\">Annulation</a></li>";
                                }
                            }
                            
                            else{
                                if(($utilisation == 0)and($penalite == FALSE))
                                {
                                    echo "<li><a href=\"reserv.php\">Reserver</a></li>";
                                }
                                else{
                                    echo "<li><a href=\"unreserv.php\">Annulation</a></li>";
                                }
                            }
                            echo "<li><a href=\"deconnect.php\">Deconnexion</a></li>";

                        }
                            

                        ?>
                    </ul>

        </header>