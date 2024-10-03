<?php

    $host = "sql10.freemysqlhosting.net";
    $user = "sql10734546";
    $pass = "1BHCaGxmuw";
    $db = "sql10734546";
    $con = mysqli_connect($host, $user, $pass, $db);

    if ($con) {

        if (isset($_POST["idProducto"])) {
            $idProducto = $_POST["idProducto"];
        }

        if (isset($_POST["Temperatura"])) {
            $Temperatura = $_POST["Temperatura"];
        }

        if (isset($_POST["Humedad"])) {
            $Humedad = $_POST["Humedad"];

            $sql = "INSERT INTO infoesp32 (idProducto, Temperatura, Humedad) VALUES ('$idProducto', '$Temperatura', '$Humedad')";
            $insertToBD = mysqli_query($con, $sql);

        }



    }

