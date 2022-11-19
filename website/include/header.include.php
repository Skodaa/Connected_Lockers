<?php

include(".//include//function.include.php");
$time = time() + 3600*24;

$title = "CYhub - Lockers";
$id ="";
$nom = "";
$prenom = "";
$birthday = "";
$phone = 0;
$handicap = "";
$dep = "";
$valid = 0;

if(isset($_GET["id"]))
{
    $id = $_GET["id"];
    $valid += 1;
}
if(isset($_GET["nom"]))
{
    $nom = mb_strtoupper($_GET["nom"]);
    $valid += 1;
}
if(isset($_GET["prenom"]))
{
    $prenom = $_GET["prenom"];
    $valid += 1;
}
if(isset($_GET["birthday"]))
{
    $birthday = $_GET["birthday"];
    $valid += 1;
}
if(isset($_GET["mail"]))
{
    $mail = $_GET["mail"];
    $valid += 1;
}
if(isset($_GET["phone"]))
{
    $phone = $_GET["phone"];
    $valid += 1;
}else{
    $phone = null;
    $valid += 1;
}
if(isset($_GET["handicap"]))
{
    $handicap = $_GET["handicap"];
    $valid += 1;
}
if(isset($_GET["dep"]))
{
    $dep = $_GET["dep"];
    $valid += 1;
}


?>

<!DOCTYPE html>
<html lang="fr">
    <head>
        <title> <?php echo $title ?> </title>
        <meta charset="utf-8" />
        <link rel="icon" href="images//logo.png" />
        <link rel="stylesheet" href="style.css" />     	
 		<meta name="author" content="alex volquardsen" />
        <meta name="date" content="2022-11-10T14:10:23+0200" /> 
    </head>
    <body>
        <header>
            <div id="nav_menu">
                <nav>
                    <ul>
                        <li><a href="index.php">Accueil</a></li>
                        <li><a href="connexion.php">Connexion</a></li>
                        <li>Historique</a></li>
                        <li>autre</a></li>
                    </ul>
                </nav>
            </div>

        </header>