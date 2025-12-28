# Ejercicios de Expresiones Regulares

Este documento contiene ejercicios de expresiones regulares desde nivel básico hasta avanzado. Cada ejercicio incluye pistas para ayudarte a resolverlo.

---

## Nivel Básico

### Ejercicio 1: Buscar palabras exactas
**Objetivo:** Encuentra todas las ocurrencias de la palabra "casa" en un texto.

**Texto de prueba:**
```
La casa es grande. Mi casa tiene jardín. Casamiento es diferente de casa.
```

**Pistas:**
- Usa literales simples
- Recuerda que regex distingue entre mayúsculas y minúsculas

<details>
<summary>Solución</summary>

```regex
casa
```
</details>

---

### Ejercicio 2: Buscar cualquier dígito
**Objetivo:** Encuentra todos los números de un solo dígito en el texto.

**Texto de prueba:**
```
Tengo 3 gatos, 2 perros y 15 peces.
```

**Pistas:**
- Usa corchetes `[]` con un rango
- Los dígitos van del 0 al 9

<details>
<summary>Solución</summary>

```regex
[0-9]
```
o también: `\d`
</details>

---

### Ejercicio 3: Buscar vocales
**Objetivo:** Encuentra todas las vocales (mayúsculas y minúsculas) en el texto.

**Texto de prueba:**
```
Aprender Expresiones regulares Es muy útil.
```

**Pistas:**
- Usa corchetes `[]` para definir un conjunto
- Incluye tanto mayúsculas como minúsculas

<details>
<summary>Solución</summary>

```regex
[aeiouAEIOU]
```
</details>

---

### Ejercicio 4: Palabras que empiezan con mayúscula
**Objetivo:** Encuentra palabras que comienzan con una letra mayúscula.

**Texto de prueba:**
```
Juan y María fueron a París. Compraron Pan en la Panadería.
```

**Pistas:**
- Usa `^` para el inicio (en este caso, con el modificador de multilínea o usa `\b`)
- Combina mayúsculas con `[A-Z]`
- Usa el punto `.` o `\w` para el resto de la palabra

<details>
<summary>Solución</summary>

```regex
\b[A-Z][a-z]*
```
</details>

---

## Nivel Intermedio

### Ejercicio 5: Validar números de teléfono (formato simple)
**Objetivo:** Valida números de teléfono en formato: XXX-XXX-XXXX

**Textos de prueba:**
```
123-456-7890 ✓
1234567890 ✗
123-45-6789 ✗
abc-def-ghij ✗
```

**Pistas:**
- Usa `\d` para dígitos
- Especifica la cantidad exacta con `{n}`
- No olvides escapar el guion `-` si es necesario

<details>
<summary>Solución</summary>

```regex
^\d{3}-\d{3}-\d{4}$
```
</details>

---

### Ejercicio 6: Extraer direcciones de correo electrónico
**Objetivo:** Encuentra todas las direcciones de correo electrónico en el texto.

**Texto de prueba:**
```
Contacta con juan@example.com o maria_lopez@correo.es para más información.
También puedes escribir a soporte123@empresa.com.mx
```

**Pistas:**
- El formato básico es: usuario@dominio.extension
- Usa `\w` para caracteres alfanuméricos
- El símbolo `@` es literal
- Usa `\.` para el punto (escapado)
- Permite letras después del punto con `[a-z]+`

<details>
<summary>Solución</summary>

```regex
[\w.-]+@[\w.-]+\.[a-z]{2,}
```
</details>

---

### Ejercicio 7: Encontrar fechas en formato DD/MM/AAAA
**Objetivo:** Encuentra fechas en formato día/mes/año.

**Texto de prueba:**
```
La reunión es el 15/03/2024. Nació el 01/12/1990.
El evento fue el 32/13/2023 (inválido, pero debe coincidir con el patrón).
```

**Pistas:**
- Los días van de 01 a 31 (usa `\d{2}`)
- Los meses van de 01 a 12
- El año tiene 4 dígitos
- Usa `/` como separador literal

<details>
<summary>Solución</summary>

```regex
\d{2}/\d{2}/\d{4}
```
</details>

---

### Ejercicio 8: Palabras con al menos 5 letras
**Objetivo:** Encuentra palabras que tengan al menos 5 caracteres.

**Texto de prueba:**
```
El desarrollo de software requiere práctica constante y dedicación.
```

**Pistas:**
- Usa `\b` para delimitar palabras
- Usa `\w` para caracteres de palabra
- Usa `{n,}` para "al menos n"

<details>
<summary>Solución</summary>

```regex
\b\w{5,}\b
```
</details>

---

### Ejercicio 9: Números decimales
**Objetivo:** Encuentra números decimales (con punto decimal).

**Texto de prueba:**
```
Los precios son: 19.99, 5.50, 100.00 y 0.99 euros.
También hay enteros como 42 y 7.
```

**Pistas:**
- Usa `\d+` para la parte entera
- El punto debe ser escapado: `\.`
- La parte decimal es opcional: usa `?` o haz dos patrones
- Usa `\d+` para decimales

<details>
<summary>Solución</summary>

```regex
\d+\.\d+
```
</details>

---

### Ejercicio 10: Etiquetas HTML simples
**Objetivo:** Encuentra etiquetas HTML de apertura y cierre (sin atributos).

**Texto de prueba:**
```html
<p>Este es un párrafo</p>
<div>Contenido del div</div>
<span>Texto en span</span>
```

**Pistas:**
- Las etiquetas están entre `<` y `>`
- Usa `\w+` para el nombre de la etiqueta
- Para capturar apertura y cierre, puedes usar grupos

<details>
<summary>Solución</summary>

```regex
<\w+>.*?</\w+>
```
</details>

---

## Nivel Avanzado

### Ejercicio 11: Validar contraseñas seguras
**Objetivo:** Valida que una contraseña tenga:
- Al menos 8 caracteres
- Al menos una mayúscula
- Al menos una minúscula
- Al menos un número
- Al menos un carácter especial (@, #, $, etc.)

**Textos de prueba:**
```
Pass123! ✗ (muy corta)
password123 ✗ (sin mayúscula ni especial)
Password123! ✓
Abc@1234 ✓
```

**Pistas:**
- Usa lookaheads positivos `(?=...)`
- Cada lookahead verifica una condición sin consumir caracteres
- `(?=.*[A-Z])` verifica al menos una mayúscula
- Al final usa `.{8,}` para verificar longitud

<details>
<summary>Solución</summary>

```regex
^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$
```
</details>

---

### Ejercicio 12: Extraer URLs complejas
**Objetivo:** Encuentra URLs que incluyan protocolo, dominio, ruta y parámetros opcionales.

**Texto de prueba:**
```
Visita https://www.example.com/path/to/page?id=123&name=test
O también http://subdomain.site.co.uk/resource
Más info en ftp://files.server.net:8080/download
```

**Pistas:**
- Protocolo: `https?://` o `ftp://`
- Dominio: combinación de `\w`, `-` y `.`
- Puerto opcional: `(:\d+)?`
- Ruta y parámetros: `[/?][\w./?=&-]*`

<details>
<summary>Solución</summary>

```regex
(https?|ftp)://[\w.-]+(:\d+)?(/[\w./?=&-]*)?
```
</details>

---

### Ejercicio 13: Extraer hashtags y menciones de Twitter
**Objetivo:** Encuentra hashtags (#palabra) y menciones (@usuario) en un tweet.

**Texto de prueba:**
```
¡Hola @usuario1! Mira este #tutorial sobre #regex. 
Compártelo con @amigo_2 y @maria-lopez
```

**Pistas:**
- Hashtags empiezan con `#`
- Menciones empiezan con `@`
- Los nombres pueden tener letras, números, guiones y guiones bajos
- Usa `\b` para límites de palabra

<details>
<summary>Solución</summary>

```regex
[#@]\w+
```
o más específico:
```regex
(#\w+)|(@[\w-]+)
```
</details>

---

### Ejercicio 14: Validar direcciones IPv4
**Objetivo:** Valida direcciones IP en formato IPv4 (0.0.0.0 a 255.255.255.255).

**Textos de prueba:**
```
192.168.1.1 ✓
255.255.255.0 ✓
300.168.1.1 ✗
192.168.1 ✗
```

**Pistas:**
- Cada octeto puede ser 0-255
- Para simplificar: `\d{1,3}` (aunque acepta 256-999, es un inicio)
- Para hacerlo exacto, usa alternación: `(25[0-5]|2[0-4]\d|[01]?\d\d?)`
- Repite 4 veces separado por puntos

<details>
<summary>Solución</summary>

```regex
^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$
```
</details>

---

### Ejercicio 15: Extraer código entre comillas
**Objetivo:** Extrae todo el contenido entre comillas dobles, incluso si contiene comillas escapadas.

**Texto de prueba:**
```python
mensaje = "Hola, este es un \"mensaje\" especial"
otro = "Simple"
vacio = ""
```

**Pistas:**
- Comienza y termina con `"`
- Usa `.*?` para captura no codiciosa
- Para comillas escapadas: `(\\.)`
- Combina con `|` para permitir cualquier carácter o escape

<details>
<summary>Solución</summary>

```regex
"([^"\\]|\\.)*"
```
</details>

---

### Ejercicio 16: Balancear paréntesis (limitado)
**Objetivo:** Encuentra expresiones con paréntesis balanceados de un nivel.

**Texto de prueba:**
```
(a + b)
(x * (y + z))
((nested))
(sin cerrar
)sin abrir
```

**Pistas:**
- Comienza con `\(`
- Contenido sin paréntesis: `[^()]*`
- Para un nivel de anidación: permite un grupo interno
- Termina con `\)`

<details>
<summary>Solución (un nivel)</summary>

```regex
\([^()]*\)
```

Para dos niveles:
```regex
\([^()]*(\([^()]*\)[^()]*)*\)
```
</details>

---

### Ejercicio 17: Extraer números con formato internacional
**Objetivo:** Encuentra números de teléfono con código de país opcional.

**Texto de prueba:**
```
+34 123 456 789
+1-555-123-4567
123-456-7890
(555) 123-4567
```

**Pistas:**
- Código de país opcional: `(\+\d{1,3})?`
- Separadores opcionales: espacios, guiones, paréntesis
- Usa `[\s\-()]?` para separadores opcionales
- Dígitos en grupos: `\d{3}`

<details>
<summary>Solución</summary>

```regex
(\+\d{1,3})?[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{4}
```
</details>

---

### Ejercicio 18: Reemplazar palabras repetidas consecutivas
**Objetivo:** Encuentra palabras que se repiten consecutivamente (como "el el" o "la la").

**Texto de prueba:**
```
El el gato está en en la la casa.
```

**Pistas:**
- Usa grupos de captura: `(\b\w+\b)`
- Usa referencias hacia atrás: `\1`
- No olvides el espacio entre palabras
- El modificador de caso puede ser útil

<details>
<summary>Solución</summary>

```regex
\b(\w+)\s+\1\b
```
</details>

---

### Ejercicio 19: Extraer valores de JSON simple
**Objetivo:** Extrae pares clave-valor de un objeto JSON simple.

**Texto de prueba:**
```json
{"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
```

**Pistas:**
- Las claves están entre comillas: `"(\w+)"`
- Seguidas de `:` y espacio opcional
- Los valores pueden ser cadenas `"..."` o números `\d+`
- Usa alternación para diferentes tipos de valores

<details>
<summary>Solución</summary>

```regex
"(\w+)"\s*:\s*("[\w\s]+"|\d+)
```
</details>

---

### Ejercicio 20: Validar formato de tarjeta de crédito
**Objetivo:** Valida números de tarjeta de crédito (16 dígitos, opcionalmente separados por espacios o guiones cada 4 dígitos).

**Textos de prueba:**
```
1234 5678 9012 3456 ✓
1234-5678-9012-3456 ✓
1234567890123456 ✓
1234 5678 9012 ✗ (incompleto)
```

**Pistas:**
- 4 grupos de 4 dígitos
- Separadores opcionales: `[\s\-]?`
- Usa `\d{4}` para cada grupo
- El último grupo no tiene separador después

<details>
<summary>Solución</summary>

```regex
^(\d{4}[\s\-]?){3}\d{4}$
```
</details>

---

## Ejercicios de Práctica Adicionales

### Ejercicio 21: Hora en formato 24 horas
**Objetivo:** Valida horas en formato HH:MM (00:00 a 23:59).

<details>
<summary>Pista</summary>
Horas: 00-23, Minutos: 00-59. Usa alternación para rangos.
</details>

---

### Ejercicio 22: Nombres de archivos con extensión
**Objetivo:** Encuentra nombres de archivos con extensiones .jpg, .png, .gif.

<details>
<summary>Pista</summary>
Nombre: `[\w-]+`, punto literal: `\.`, extensiones con alternación.
</details>

---

### Ejercicio 23: Código postal español
**Objetivo:** Valida códigos postales españoles (5 dígitos, no empiezan con 00).

<details>
<summary>Pista</summary>
Usa lookahead negativo para evitar 00, luego `\d{5}`.
</details>

---

### Ejercicio 24: Extraer comentarios de código
**Objetivo:** Encuentra comentarios de una línea en código (// comentario).

<details>
<summary>Pista</summary>
`//` seguido de `.*` hasta el final de línea `$`.
</details>

---

### Ejercicio 25: Palabras palíndromas simples
**Objetivo:** Encuentra palabras de 3 letras que sean palíndromos (aba, oro).

<details>
<summary>Pista</summary>
Captura primera letra `(\w)`, cualquier letra, referencia hacia atrás `\1`.
</details>

---

## Consejos finales

1. **Practica en línea:** Usa herramientas como regex101.com o regexr.com
2. **Prueba incremental:** Construye tu regex paso a paso
3. **Usa grupos de captura:** `()` para extraer partes específicas
4. **Modificadores útiles:**
   - `i` - case insensitive
   - `g` - global (todas las coincidencias)
   - `m` - multilínea
5. **Documenta tus regex:** Son difíciles de leer, agrega comentarios

¡Sigue practicando y mejorando tus habilidades con expresiones regulares!