<?php

    $title = "CYhub - Login";

    include("include/header.include.php"); 

?>
        <main>
            <h2> Formulaire création d'utilisateur : </h2>
            <form action="connexion.php" method="get" id="connect" target="_blank">
                <fieldset><legend><label>Inscriver vous :</legend></label>
                <legend><label> No utilisateur : </label></legend>
                    <input type="text" name="id" />
                <legend><label> Nom  : </label></legend>
                    <input type="text" name="nom" />
                <legend><label> Prénom : </label></legend>
                    <input type="text" name="prenom" />
                <legend><label> Date de naissance : </label></legend>
                    <input type="date" name="birthday" />
                <legend><label> email : </label></legend>
                    <input type="text" name="mail" />   
                <legend><label> numéro de téléphone : </label></legend>
                    <input type="text" name="phone" />       
                <legend><label> êtes vous en situation de hadicap ? </label></legend>
                    <label> oui </label>
                    <input type="radio" name="handicap" value="true"/>
                    <label> non </label>
                    <input type="radio" name="handicap" value="false" checked="checked"/>
                <legend><label> De quel département faite vous partit ? </label></legend>
                    <label> Informatique </label>
                    <input type="radio" name="dep" value="1001"/>
                    <label> Mathématiques </label>
                    <input type="radio" name="dep" value="1002"/>
                    <label> Physique </label>
                    <input type="radio" name="dep" value="1003"/>
                    <label> CUPGE </label>
                    <input type="radio" name="dep" value="1004"/>
                <input type="submit" value="Créer" />
                </fieldset>
            </form>

            <?php

            if($valid == 8)
            {
                $result = add_uti($id,$nom,$prenom,$birthday,$mail,$phone,$handicap,$dep);
                echo $result;
            }
                

            ?>
        </main>

<?php
    include("include/footer.include.php");
?>