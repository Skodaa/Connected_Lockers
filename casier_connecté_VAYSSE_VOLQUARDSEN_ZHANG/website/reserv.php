<?php

    $title = "CYhub - Reservation";

    include("include/header.include.php");


$dep = departement($user_id);
$lockers = free_lockers($dep);

?>

    <main>

        <div class="logs">
            <div class="logs-contain">

            <form class="form" action="index.php" method="post" id="reserv">
                <label> Reservation d'un casier :</label>
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
                <input type="submit" value="Reserver" />
                
            </form>
            <a href="unreserv.php" > Annuler réservation </a>



            </div>
        </div>


    </main>

<?php

    include("include/footer.include.php");
?>