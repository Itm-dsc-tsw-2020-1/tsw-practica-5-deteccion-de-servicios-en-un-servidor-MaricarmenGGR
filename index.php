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
$conexion = mysqli_connect($servidor, $usuario, $clave, "compuservi");
if (!$conexion) {
    echo "No se pudo conectar Amiguito";
    exit;
}
$sql = "select * from computadoras";
$resultado = mysqli_query($conexion, $sql);
echo "Conexion Exitosa :v";
echo "<table border='1'>";
while ($renglon = mysqli_fetch_array($resultado)) {
    $dir_ip = str_replace(" ", "%20", $renglon['dir_ip']);
    $servicio = $renglon['servicio'];
    $puerto = $renglon['puerto'];
    $Estado = $renglon['Estado'];
    echo "<td>
            Direccion IP: " . $renglon['dir_ip'] . "<br/>
            Servicio: " . $renglon['servicio'] . "<br/>
            Puerto: " . $renglon['puerto'] . "<br/>
            Estado: " . $renglon['Estado'] . "<br/>
             </td>";
}
?>

            </div>
      </body>
</html>
