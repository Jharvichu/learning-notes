!/bin/bash
# Este script es la resolucion del ejercicio numero 1

echo "Ingrese su nombre completo :"
read nombre
echo "Ingrese su año de nacimiento: "
read anio

edad=$((2025-$anio))

echo "Bienvenido $nombre con una edad de $edad años, espero que la pase bien"
