<?php

    $title = "CYhub - login"; 
    $invalid = 3;

    include("include/header.include.php");

    if($user_logged == False)
    {
        $aff = 0;
    }
    else
    {
        $aff = 1;
    }

    if(isset($id))
    {
        if(isset($password))
        {
            $invalid = verif_mdp($id,$password);
            if($invalid == 1)
            {
                $aff = 1;
                $_SESSION["logged"] = TRUE;
                $_SESSION["id_user"] = $id;
            }
            else
            {
                $aff = 0;

            }
        }
    }

?>
    <main>  
        <?php

        if($aff == 0)
        {
            
            echo "<div class=\"logs\"><div class=\"logs-contain\"><form class=\"form\" action=\"connexion.php\" method=\"post\" id=\"connect\">
            <label> Connecter vous : </label>
            <div class=\"field-container\">
            <label> Id utilisateur : </label>
                <input class=\"field\" type=\"text\" name =\"id\"/>
            </div><div class=\"field-container\">
            <label> Mot de passe : </label>
                <input class=\"field\" type=\"password\" name=\"password\"/>";
            if(($invalid == 0) and (isset($_POST['id'])))
            {
                echo "<label class=\"erreur\"> Erreur de mot de passe ! </label>";
            }
            echo "</div>
                <input type=\"submit\" value=\"connexion\"/>";
            
            echo "\t\n\n</form>";
            echo "<a id=\"activado\" href=\"activation.php\"> Activer votre compte </a></div></div>";
        }
        else if($aff == 1)
            echo " <div class=\"logs\"><div class=\"logs-contain\"><p class=\"field\"> Vous êtes maintenant connecté !</p><a class=\"retour\" href=\"index.php\"> Retour au menu </a></div></div>";
        ?>

<?php

    include("include/footer.include.php")

?>