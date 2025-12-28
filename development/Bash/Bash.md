# Scripting en Bash

## ¿Qué es bash?

Bash significa Bourne Again Shell, y es un intérprete de comandos muy usado en sistemas Linux y macOS. También puede usarse en Windows si instalas Git Bash o WSL (Windows Subsystem for Linux).

Un intérprete de comandos permite que escribas instrucciones (comandos) para que la computadora las ejecute, como los siguientes comandos basicos:

``` bash
ls                  # lista archivos
cd Documentos/      # cambia de directorio 
mkdir carpeta       # crea una carpeta
touch archivo.txt   # crea un archivo vacio
rm archivo.txt      # elimina archivos
cp doc.c destino/   # copia archivos o directorios
mv doc.c destino/   # mueve o renombra archivos o directorios
```

Pero más poderoso aún: puedes guardar estos comandos en un script para automatizarlos.

## ¿Qué es un script de Bash?

Un script en Bash es simplemente un archivo de texto plano que contiene una lista de comandos que se ejecutan uno tras otro. Ejemplo de archivo `mi_script.sh`:

``` bash
#!/bin/bash
echo "Hola, mundo"
```

### ¿Cómo creo y ejecuto mi script de Bash?

Primeramente abrimos la terminal (Linux/macOS) o abrimos Git Bash (Windows). Posteriomente en la terminal creamos el archivo de la siguiente forma:

``` bash
nano mi_script.sh
```

Esto abre un editor de texto y escribimos lo que queremos que ejecute:

``` bash
#!/bin/bash
echo "Hola, mundo"
```

Guardamos y cerramos el archivo. Luego para permitir que el script se pueda ejecutar, se le da permisos como:

``` bash
chmod +x mi_cript.sh
```

Este comando le da al archivo permiso de ejecución (`+x` = ejecutable). Finalmente ejecutamos el script de la siguiente manera:

``` bash
./mi_script.sh
```

## Variables y entrada de Usuario

### Variables

Una variable es como una caja donde guardas información (un texto, un número, etc.) para usarla más adelante. Su sintaxis es:

``` bash
nombre_variable=valor
```

> **Nota**: No se pone espacios alrededor del `=`. Si se pone espacio, da error.

### Tipos de variable

Bash no necesita que le digas si una variable es texto o número. Pero tú sí debes entender la diferencia:

- Texto (String):

    ``` bash
    nombre="Jharvy" 
    ```

- Número:
  
    ``` bash
    anio=2004 
    ```

---

### Leer entrada del usuario `read`

Su sintaxis es:

```bash
read nombre_variable
```

Esto pausa el script hasta que el usuario escriba algo. Lo que escriba se guarda en la variable. Por ejemplo:

```bash
echo "¿Cuál es tu nombre?"
read nombre
echo "Hola, $nombre"
```

> **Nota**: para referenciar a una variable se utiliza `$` antes de la variable, para poder utilizarlo en otra linea del script.

### Imprimir variables: `echo`

Sirve para mostrar texto, variables, resultados etc. Su sintaxis es:

```bash
echo "imprimir"
```

---

### Uso de comillas

- Comillas dobles `""`: Estas permiten expandir variables

    ```bash
    nombre="Pedro"
    echo "Hola, $nombre"  # => Hola, Pedro
    ```

- Comillas simples `''`: No expanden variables, todo se toma literal

    ```bash
    echo 'Hola, $nombre'  # => Hola, $nombre
    ```

- Sin comillas: Solo recomendable si no hay espacios ni caracteres especiales.
  
    ```bash
    echo hola # => hola
    ```


## Condicionales y lógica

### Estructura básica de condicionales

Los condicionales nos permiten ejecutar código solo si se cumple una condición. En Bash, usamos `if`, `else` y `elif` para verificar si algo es verdadero, y luego decidimos qué hacer si esa condición es verdadera o falsa. Su sintaxis es:

```bash
if [ condición1 ]; then
    # código si condición1 es verdadera
elif [ condición2 ]; then
    # código si condición2 es verdadera
else
    # código si ninguna condición es verdadera
fi
```
- `if` inicia la condición
- `then` indica lo que ocurrirá si la condición es verdadera
- `fi` termina el bloque de `if`
  
### Comparaciones en Bash

Bash tiene operadores para hacer comparaciones de números y cadenas de texto.

- Comparación de números.
  - `-eq`: igual que
  - `-ne`: diferente que
  - `-lt`: menor que
  - `-le`: menor o igual que
  - `-gt`: mayor que
  - `-ge`: mayor igual que
  
  Ejemplo:
    ```bash
    #!/bin/bash
    # Pedir la edad
    echo "¿Cuál es tu edad?"
    read edad

    # Condicionales
    if [ $edad -lt 18 ]; then
        echo "Eres menor de edad."
    elif [ $edad -ge 18 ] && [ $edad -le 60 ]; then
        echo "Eres un adulto."
    else
        echo "Eres mayor de 60 años."
    fi
    ```

- Comparación de cadenas de texto.
  - `=`: igual a
  - `!=`: diferente de
  - `<`: menor que (lexicograficamente)
  - `>`: mayor que (lexicograficamente)
  
  Ejemplo:
    ```bash
    #!/bin/bash
    nombre="Carlos"

    # Condicional
    if [[ $nombre == "Carlos" ]]; then
        echo "Hola, Carlos"
    fi
    ```  
    > **Nota:** Cuando comparas cadenas de texto, usa dobles corchetes `[[ ]]` en lugar de `[ ]`.

### Expresiones lógicas

- `&&`: Y lógico". Solo se ejecuta el segundo comando si el primero es verdadero.
- `||`: "O lógico". Se ejecuta el segundo comando si el primero es falso.
- `!`: "Negación". Invierte el valor de la condición (verdadero se convierte en falso y viceversa).

## Ejercicios
1. Crea una script que pifa el nombre completo del usuario, pida su año de nacimiento, calcule su edad y le de un saludo con sus datos calculados.
2. Crea un script que pida el nombre completo del usuario, pida su año de nacimiento, calcule su edad, verfique si es mayor de edad, en caso sea mayor de edad sea registrado en un archivo txt y que envie un mensaje de bienvenido.



