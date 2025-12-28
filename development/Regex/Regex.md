# Regex

Una expresión regular (o regex) es una secuencia de caracteres que forman un patrón de búsqueda. Se utiliza para encontrar, manipular o validar cadenas de texto que siguen un patrón específico. En pocas palabras, nos ayuda a buscar y trabajar con texto de una manera muy precisa.

### ¿Para qué se usan las expresiones regulares?

Algunos de los casos mas comunes de uso son:

- Validación de formularios (por ejemplo, verificar si un correo electrónico es válido).
- Búsqueda y extracción de información específica de un texto (como números de teléfono, fechas, etc.).
- Reemplazo de texto en archivos o cadenas.

 ### Instalación de la libreria `re` en Python

 Python tiene una librería llamada `re` que nos permite trabajar y practicar con expresiones regulares de manera fácil y eficiente. Esta libreria se importa de la siguiente manera:

 ``` python
 import  re
 ```

 Las funciones que mas se utilizaran son:

 - `re.match()`: Busca el patrón al principio de la cadena.
 - `re.search()`: Busca el patrón en cualquier cadena.
 - `re.findall()`: Devuelve una lista con todas las ocurrencias del patrón en el texto.
 - `re.sub()`: Reemplaza las ocurrencias del patrón por otro texto.

## Sintaxis Basica

### 1. Literales

Los literales son los caracteres que representan exactamente lo que aparece en la cadena. Es decir, si escribes "gato" en una expresión regular, buscará exactamente "gato" en el texto.

```
gato
```

Este patrón coincidiría con cualquier aparición de la palabra "gato" en el texto.

### 2. Metacaracteres

Los metacaracteres son símbolos especiales que tienen un significado único en Regex. Estos nos permiten crear patrones más complejos y realizar búsquedas más flexibles.

- El punto `.`: Coincide con cualquier carácter, excepto los saltos de línea. Por ejemplo

    ```
    o.a
    ```

    Este patron coincide con "ooa", "ola", "o@a", "o1a", etc. Siempre el punto coincidira con **un solo** caracter.

- El caret `^`: indica que el patrón debe coincidir al inicio de la cadena.

    ```
    ^gatiñoo
    ```

    Este patron buscara cualquier cadena que comience con la palabra "gatiñoo".

- El dolar `$`: indica que el patrón debe coincidir al final de la cadena.
  
    ```
    perriñoo$
    ```

    Este patron buscara cualquier cadena que termine con la palabra "perriñoo".  
    
- Corchetes `[]`: Se utilizan para definir un conjunto de caracteres. Cualquier carácter dentro de los corchetes será una coincidencia válida.
  
    ```
    [gpGP]ato
    ```

    Este patron coincidirá con "gato", "Gato", "Pato", "pato", ya que esta buscando entre "g", "p", "P" y "G"

- Rango `-`: Dentro de los corchetes, el guion se utiliza para definir un rango de caracteres.
  
    ```
    [A-Z][0-9]
    ```

    Este patron coincidira con cualquier par de caracteres que siga el siguiente orden (cualquier letra mayuscula)(cualquier numero) como: D1, A8, C4, etc.

- Alternancia `|`: Funciona como un "o lógico" dentro de las expresiones regulares. Permite buscar coincidencias entre dos o más opciones

    ```
    perro|gato
    ```
    
    Este patron buscara "gato" o "perro" en el texto que estamos evaluando

- Parentecias `()`: Los paréntesis en Regex tienen dos funciones principales
  - Agrupar: Cuando pones parte de tu patrón entre paréntesis, estás agrupando esos caracteres, lo que permite aplicar cuantificadores al grupo completo.
    
    ```
    (a|b)c
    ```

    Este patron coincide con "a" o "b" (esto es la agrupación), seguido de "c", es decir, "ac" o "bc".

  - Capturar subexpresiones: Cuando usas paréntesis en una expresión regular, las partes dentro de los paréntesis se capturan y pueden ser referenciadas o extraídas posteriormente.

    ```
    (\d{2})[/-](\d{2})[/-](\d{4})
    ```

    Este patrón coincidiría con una fecha en formato DD-MM-AAAA o DD/MM/AAAA.


### 3. Cuantificadores

Los cuantificadores en Regex nos permiten especificar cuántas veces debe ocurrir un patrón determinado.

- Asterisco `*`: Significa "cero o más" de lo que lo precede. Es decir, el patrón puede aparecer cero o más veces.
  
    ```
    a*b
    ```

    Este patron coincidira con lo siguiente "b", "ab", "aab", "aaab", "aaaab", "aaaaab", etc. Este patron es detectado en cualquier lugar de la frase, pero no es necesario el antecesor que este.

- Mas `+`: Significa "uno o más" de lo que lo precede. Es decir, el patrón debe aparecer al menos una vez.
  
    ```
    a+b
    ```

    Este patron coincidira con lo siguiente "ab", "aab", "aaab", "aaaab", "aaaaab", etc. Este patron es detectado en cualquier lugar de la frase, pero debe tener el antecesor obligatorio.

- Integración `?`: significa "cero o uno" de lo que lo precede. Es decir, el patrón puede aparecer cero o una vez.
  
    ```
    a?b
    ```

    Este patron coincidira con lo siguiente "b" y "ab", pero no coincidira con "aab", "aaab", etc.

- Llaves `{}`: se usan para especificar el número exacto de repeticiones o un rango de repeticiones para el patrón.
  
  - `{n}`: Coincide con exactamente n repeticiones del patrón.

        a{3}b
    
    Este patron coincide con "aaab", no coincide con mas.

  - `{n,m}`: Coincide con entre n y m repeticiones.
  
        a{2,4}b

    Este patron coincide con "aab", "aaab" y "aaaab", no coincide con mas.

### 4. Lookaheads y Lookbehinds

Los Lookaheads y Lookbehinds son patrones avanzados de búsqueda en expresiones regulares que permiten buscar algo sin incluirlo en la coincidencia. En otras palabras, nos permiten mirar hacia adelante o hacia atrás en la cadena de texto sin incluir esos elementos en el resultado.

- Lookahead positivo `(?=pattern)`: Asegura que lo que sigue después del patrón coincida con una condición, pero sin incluirlo en la coincidencia.
  
    ```
    gato(?= perro)
    ```
    
    Esto encontrará "gato" solo si está seguido de "perro", pero no incluirá la palabra

- Lookahead negativo `(?!pattern)`: Asegura que lo que sigue después del patrón no coincida con un patrón específico.

    ```
    gato(?! perro)
    ```

    Esto encontrará "gato" si no está seguido de "perro", excluyendo las coincidencias con "gato perro".


- Lookbehind positivo `(?<=pattern)`: Asegura que lo que precede al patrón coincida con una condición, pero sin incluirlo en la coincidencia.

    ```
    (?<= gato) perro
    ```

    Esto encontrará "perro" solo si está precedido por "gato", pero no incluirá "gato".

- Lookbehind negativo `(?<!pattern)`: Asegura que lo que precede al patrón no coincida con una condición.
  
    ```
    (?<! gato) perro
    ```

    Esto encontrará "perro" solo si NO está precedido por "gato", pero no incluirá "gato".

    > **Nota**: puedes utilizar `(?:pattern)` ya sea antes o despues de la palabra para validarlo y ademas que la condicion (pattern) quede como resultado (ver resolucion ejercicio 4)

### 5. Metacaracteres Especiales:

Los metacaracteres especiales son secuencias de escape que nos permiten coincidir con tipos de caracteres de forma simplificada. En lugar de escribir patrones complejos para encontrar letras, números, espacios, etc., usamos estos metacaracteres para simplificar la expresión regular.

- `\d`: Coincide con cualquier digito numerico del 0 al 9.
- `\D`: Coincide con cualquier caracter que no sea un digito numerico como letras, signos de puntuacion, espacios, etc.
- `\w`: Coincide con cualquier letra alfabetica (mayuscula o minuscula), número y el guion bajo excepto con espacios, signos de puntuacion, etc.
- `\W`: Coincide con cualquier caracter que no sea letra alfabetica (mayuscula y minuscula), numero ni guion bajo.
- `\s`: Coincide con cualquier caracter de espacio en blanco como ` `, `\t`, `\n`, `\r`, `\f`.
- `\S`: Coincide con cualquier caracter que no sea espacios en blanco.
- `b`: Coincide con un límite de palabra. Un límite de palabra es cualquier lugar donde un carácter de palabra (`\w`) es seguido por un carácter que no es palabra (`\W`), o viceversa.
- `\B`: Es el opuesto de `\b`. Coincide con un lugar que no es un límite de palabra.

### Extras:

`[^"]`: Cualquier carácter que NO sea una comilla doble


## Ejercicios

1. Validar la direccion de correo que sigan la siguiente estructura "usuario@dominio.com". Donde **@** y **.com** deben estar obligatoriamente.
2. Escribe una expresión regular que valide números de teléfono en formato (XXX) XXX-XXXX donde X es un dígito.
3. Validar una contraseña, considerando que cumpla lo siguiente
   1. Debe tener al menos una letra mayúscula.
   2. Debe tener al menos un número.
   3. Debe tener al menos un carácter especial (por ejemplo, !, @, #, $).
   4. Debe contener minimo 10 caracteres.
4. Crear una expresión regular que extraiga precios con sus símbolos de moneda, usando lookaheads y lookbehinds.
   
        
    






