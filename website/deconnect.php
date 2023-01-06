<?php

    $title = "CYhub - Decconection";

    include("include/header.include.php");

    $_SESSION["logged"] = FALSE;
    $_SESSION["id_user"] = "";


?>
        <main>

        <div class="logs"><div class="logs-contain"><p class="field"> Vous êtes maintenant déconnecté !</p><a class="retour" href="index.php"> Retour au menu </a></div></div>

        </main>
<?php
    include("include/footer.include.php");
?>