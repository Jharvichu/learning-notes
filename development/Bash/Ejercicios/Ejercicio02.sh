#!/bin/bash

# Este script resuelve el ejercicio numero 2

echo "Ingrese su nombre completo"
read nombre
echo "Ingrese su año de nacimiento"
read anio

edad=$((2025-$anio))

if [ $edad -ge 18 ]&& [ $edad -lt 60 ]; then
	echo "$nombre	$edad">>registro.txt
	echo "Bienvenido $nombre de $edad años"
elif [ $edad -lt 18 ]; then
	echo "Usted $nombre es menor de edad, no puede registrarse"
else 
	echo "Usted $nombre es mayor de edad, no puede registrarse"
fi
