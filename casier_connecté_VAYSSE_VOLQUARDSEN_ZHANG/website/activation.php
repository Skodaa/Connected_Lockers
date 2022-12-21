<?php

    $title = "CYhub - sign in";

    include("include/header.include.php"); 

?>

        <main>
            <div class="logs">
            <div class="logs-contain">
            <form class="form" action="activation.php" method="post" id="inscrire">
                <label> Activer votre compte :</label>
                <div class="field-container">
                <label> No utilisateur : </label>
                    <input class="field" type="text" name="id" />
                </div><div class="field-container">
                <label> Mot de passe : </label>
                    <input class="field" type="password" name="password" />
                </div>       
                <input type="submit" value="Activer" />
                
            </form>
            
            <?php
            if(isset($id)and(isset($password)))
            {
                $result = activate_uti($id,$password);
                echo "<p class=\"connected\">$result</p>";
            }
                

            ?>
            </div>
        </div>
        </main>

<?php
    include("include/footer.include.php");
?>