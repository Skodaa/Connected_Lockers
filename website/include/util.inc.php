<?php

    class User 
    {
        public function __construct() {}

        function login(): bool{
            if((isset($_GET["id_user"]))&&($_GET["password"]))
            {
                $result = verif_mdp($_GET["id_user"],$_GET["password"]);
                if((isset($result))and($result == 0))
                {
                    $_SESSION["id_user"] = $_GET["id_user"];
                    $_SESSION["logged"] = $result;
                }
            }
        }
    }


    function ladate(string $lang = "fr" ): string{
        if($lang == "fr"){
            $jours = array("Monday" => "Lundi","Tuesday" => "Mardi","Wednesday" => "Mercredi","Thursday" => "Jeudi","Friday" => "Vendredi","Saturday" => "Samedi","Sunday" => "Dimanche");
            $mois = array("January" => "Janvier","February" => "Fevrier","March" => "Mars","April" => "Avril","May" => "Mai","June" => "Juin","July" => "Juillet","August" => "Aout","September" => "Septembre","October" => "Octobre ","November" => "Novembre","December" => "Decembre",);
            $rep = $jours[date("l")];
            $rep .=" ".date("j");
            $rep .= " ".$mois[date("F")];
            $rep .= " ".date("Y");
        }
        return $rep;
    }

    function get_navigateur(): string{
        return $_SERVER["HTTP_USER_AGENT"];
    }

?>