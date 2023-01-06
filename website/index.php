<?php

    $title = "CYhub - acceuil";

    include("include/header.include.php");

if(isset($locker))
{
    $is_ok = verif_mdp($user_id,$_POST['password']);
    if(($is_ok == 1)and($locker != ""))
    {

        reserv_locker($locker, $user_id);

    }

}

?>
        <main>


        <?php

            if($user_logged == FALSE)
            {   
                echo '<div class="logs"><div class="logs-contain"><h2 class="field-container"> Veuillez vous connecter</h2><p>Vous pourrez acceder aux fonctionnalités du site après connexion</p><a class="retour" href="connexion.php">se connecter</a></div></div>';
            }
            else
            {
                echo "<div class=\"logs\"><div class=\"logs-contain\">";
                if(isset($prenom))
                {
                    echo "<div class =\"field-container\"><h3> Prenom :</h3><p> $prenom </p></div>";
                }
                if(isset($nom))
                {
                    echo "<div class =\"field-container\"><h3> Nom :</h3><p> $nom </p></div>";
                }
                if(isset($user_id))
                {
                    echo "<div class =\"field-container\"><h3> Id :</h3><p> $user_id </p></div>";
                }
                if(isset($utilisation))
                {
                    echo "<div class =\"field-container\"><h3> Utilisation en cours :</h3><p> $utilisation </p></div>";
                }
                if($invalid_locker == TRUE)
                {
                    echo "<div class=\"field-container\"><p> Casier non réserver ! Erreur de sélection du casier !</p></div>";
                }
                else if((isset($locker))and($is_ok == FALSE))
                {
                    echo "<div class=\"field-container\"><p> Casier non réserver ! Erreur de mot de passe !</p></div>";
                }
                else if(isset($locker))
                {
                    echo "<div class=\"field-container\"><p> Casier réservé avec succès !</p></div>";
                }

            }



        ?>

        </main>
<?php
    include("include/footer.include.php");
?>