<?php

    $title = "CYhub - Reservation";

    include("include/header.include.php");

$lockers = reserved_lockers($user_id);

if(isset($_POST['locker']))
{
    $locker = $_POST['locker'];
    $is_ok = verif_mdp($user_id,$_POST['password']);
    if($is_ok == 1)
    {

        unreserv_locker($locker,$user_id);

    }

}
?>

    <main>

        <div class="logs">
            <div class="logs-contain">

            <form class="form" action="unreserv.php" method="post" id="reserv">
                <label> Annuler la reservation d'un casier :</label>
                <div class="field-container">
                <label> choisissez un casier : </label>
                    <select name="locker" >
                        <option value="">--Choisissez un casier--</option>
                    <?php
                        for($i = 0; $i < sizeof($lockers);$i++)
                        {
                            $option = $lockers[$i];
                            echo "<option value=\"$option\"> $option </option>";
                        }

                    ?>
                    </select>
                </div><div class="field-container">
                <label> Mot de passe : </label>
                    <input class="field" type="password" name="password" />
                </div>       
                <input type="submit" value="Annuler réservation" />
                <?php

                    if(isset($is_ok) and ($is_ok == 1))
                    {
                        echo "<p class=\"connected\">Reservation Annulé !</p>";
                    }
                    else if(isset($is_ok))
                    {
                        echo "<p class=\"erreur\"> Erreur de mot de passe </p>";
                    }

                ?>
                
            </form>



            </div>
        </div>


    </main>

<?php

    include("include/footer.include.php");
?>