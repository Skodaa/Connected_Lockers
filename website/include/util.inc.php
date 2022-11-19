<?php

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