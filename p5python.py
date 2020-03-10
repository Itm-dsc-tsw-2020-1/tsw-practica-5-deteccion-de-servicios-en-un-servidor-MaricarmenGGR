"""Maricarmen Guadalupe Gonzalez Rodriguez"""

import os
computadora = "200.33.171.86"
from subprocess import Popen, PIPE
process = Popen(['nmap', ' -sT ', computadora], stdout = PIPE, stderr=PIPE)
stdout, stder = process.communicate()
print(stdout)

file = open("C:/Users/Maricarmen Gonzalez/file.txt","w")
file.write(str(stdout))
file.close()

print("--------------LECTURA-------------")
file = open("C:/Users/Maricarmen Gonzalez/file.txt","r")
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
"""
print("---Puertos---")
for i in range(r):
    datos = list(filter(None, textoSplit[i].split(" ")))
    if i > 5 and i < (len(textoSplit)-3):
        print(datos[0])

print("---Estado---")
for i in range(r):
    datos = list(filter(None, textoSplit[i].split(" ")))
    if i > 5 and i < (len(textoSplit)-3):
        print(datos[1])

print("---Servicio---")
for i in range(r):
    datos = list(filter(None, textoSplit[i].split(" ")))
    if i > 5 and i < (len(textoSplit)-3):
        print(datos[2])
        """


import mysql.connector as mysql

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
        sql = "INSERT INTO computadoras (id_computadora, dir_ip, puerto, Estado, servicio) VALUES (0,'200.33.171.86', %s, %s, %s)"
        operacion.execute(sql, val)
        conexion.commit()
        """
for id_compu, dir_ip, servicio, puerto, Estado in operacion.fetchall() :
    print (id_compu, dir_ip, servicio, puerto,Estado)
    """
conexion.close()
