<!DOCTYPE html>
<html lang = "es">
    <head>
        <meta charset="utf-8"/>
          <title>Servicios Detectados</title>
          <meta name = "author" content="Maricarmen Gonzalez Rodriguez"/>
      </head>
      <body>
          <div>
              <h1>Resultados</h1>
              <?php
$servidor = "localhost";
$usuario = "root";
$clave = "";
$conexion = mysqli_connect($servidor, $usuario, $clave, "miyama");
if (!$conexion) {
    echo "<h1>No se pudo conectar Amiguito</h1>";
    exit;
}
echo "<h1>Conexion Exitosa</h1>";

?>

            </div>
      </body>
</html>
