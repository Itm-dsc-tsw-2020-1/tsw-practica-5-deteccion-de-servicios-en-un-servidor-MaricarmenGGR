"""Maricarmen Guadalupe Gonzalez Rodriguez"""
import os
import mysql.connector as mysql
computadora = "200.33.171.124"
#computadora = "200.33.171.86"
from subprocess import Popen, PIPE
process = Popen(['nmap', ' -sT ', computadora], stdout = PIPE, stderr=PIPE)
stdout, stder = process.communicate()
print(stdout)
#En caso de que el archivo file.txt no se encuentre edtitado en la misma carpeta de la aplicacion
#Favor de verificar la ruta en su computador: Directorio de Usuarios/Users/Nombre_del_Usuario/file.txt
file = open("file.txt","w")
file.write(str(stdout))
file.close()

print("--------------LECTURA-------------")
file = open("file.txt","r")
text = ""
for linea in file.readlines(): 
    print (linea)
    text += linea
file.close()

print(text)

textoSplit = text.split('\\r\\n')

print("-----El Split.------")
print(textoSplit)
print("---------LONGITUD----------")
print(len(textoSplit))
r = len(textoSplit)
for i in range(r):
    datos = list(filter(None, textoSplit[i].split(" ")))
    if i > 5 and i < (len(textoSplit)-3):
        print(datos)


# Inicio del código
print ("Python conectándose a MySQL")

# Conectándose a MySQL
conexion = mysql.connect( host='localhost', user= 'root', passwd='', db='compuservi' )
operacion = conexion.cursor()
for i in range(r):
    datos = list(filter(None, textoSplit[i].split(" ")))
    if i > 5 and i < (len(textoSplit)-3):
        print(datos)
        val = datos
        sql = "INSERT INTO computadoras (id_computadora, dir_ip, puerto, Estado, servicio) VALUES (0,'200.33.171.124', %s, %s, %s)"
        operacion.execute(sql, val)
        conexion.commit()
        
conexion.close()
