# **Doble de Pruebas**

# Mocks

Los mocks son objetos simulados que se utilizan en pruebas unitarias para reemplazar partes del sistema que quieres probar, permitiéndote aislar el código bajo prueba y controlar el entorno de prueba.

Por ejemplo: Imagina que tu código envía un mensaje de texto o accede a una base de datos. No quieres gastar dinero, conectarte a internet o borrar datos reales cada vez que haces una prueba. Entonces, reemplazas esa parte por un mock: un objeto falso que se comporta como si fuera real, pero no hace nada de verdad.

### Casos comunes donde se usan Mocks:
*  Llamadas a APIs externas (como OpenAI, Twitter, Google Maps…)
*  Acceso a bases de datos
*  Envío de correos o SMS
*  Lectura de archivos o sistemas de archivos complejos
*  Acciones que dependen del tiempo (como `time.sleep()`)
*  Comportamiento aleatorio (como `random.random()`)

## ¿Cómo instalar y usar `unittest.mock`?

La librería unittest.mock ya viene incluida con Python desde la versión 3.3, así que no necesitas instalar nada. Asi que olo debes importar lo necesario:

``` python
from unittest.mock import Mock
```

## Conceptos basicos de un Mock

### Creacion de un Mock

Para crear unmock basico:

``` python
from unittest.mock import Mock

mock_funcion = Mock()
```

Esto crea un objeto que puede actuar como una función falsa, registrando si fue llamada y con qué argumentos.

### Configurar lo que devueve: `return_value`

Por defecto, un mock devuelve otro mock. Pero puedes decirle qué devolver:

``` python
mock_funcion.return_value = "Correo enviado"
print(mock_funcion())  # => "Correo enviado"
```

### Verificar llamadas; `.called` y `.call_count`

Estas propiedades te ayudan a ver si el mock fue usado:

``` python
print(mock_funcion.called)      # True si fue llamado
print(mock_funcion.call_count)  # Cuántas veces fue llamado
```

### Verificar con asserts

Para comprobar que el mock fue llamado como esperabas:

``` python
mock_funcion.assert_called_with(argumento_1, argumento_2)
```

Esto refleja si el mock al ser llamado por otra funcion en la prueba, tomo lo *argumentos_1* y *argumento_2* como esperabamos.

Tambien podemos verificar si el mock nunca fue llamado en la prueba con: 

```python
mock_funcion.assert_not_called()
```

## ¿Que son los Patch?

`patch` es una función/decorador de la librería `unittest.mock` que te permite reemplazar temporalmente un objeto/funcion durante una prueba con un objeto mock. Es la forma más común y elegante de usar mocks en Python.

Con `patch()` puede decir: "Durante esta prueba, reemplaza la función real por un mock"

#### Tipos de `patch`

* `patch` como decorador

    ``` python
    @patch('module.function_to_replace')
    def test_example(mock_function):
        mock_function.return_value = 'valor simulado'
        # ... tu prueba aquí ...
    ```

* `patch` como context manager

    ``` python
    def test_example():
        with patch('module.Class') as MockClass:
            instance = MockClass.return_value
            instance.method.return_value = 'resultado falso'
            # ... tu prueba aquí ...
    ```

La regla de oro del mocking es: `"Parchea donde se usa, no donde se define."`. Por ejemplo tenemos el siguiente código:

```python
# api.py
import requests

def get_user_name(user_id):
    response = requests.get(f'https://api.example.com/users/{user_id}')
    return response.json()['name']
```

Su prueba utilizando patch como `context manager`:

```python
# test_api.py
from unittest.mock import patch
import api

def test_get_user_name():
    # Simulamos la respuesta de requests.get
    fake_response = {'name': 'Ana López'}
    
    with patch('requests.get') as mock_get:
        # Configuramos el mock
        mock_get.return_value.json.return_value = fake_response
        
        # Llamamos a nuestra función
        result = api.get_user_name(123)
        
        # Verificaciones
        assert result == 'Ana López'
        mock_get.assert_called_once_with('https://api.example.com/users/123')
```

**¿Qué ocurre en el ejemplo?**

1. `patch('requests.get')` remplaza temporalmente `request.get` con un mock.
2. Configuramos el mock para devolver una respuesta falsa cuando se llame a `.json()`.
3. Ejecutamos nuestro código normal (que usa el mock sin saberlo)
4. Verificamos que:
   1. El resultado es el esperado.
   2. Se llamó a la API con los parámetros correctos.

### Parametros importantes de Patch

* target: Cadena con la ruta completa al objeto a reemplazar (ej: `'module.ClassName'`)
* new: Objeto que reemplazará al original (si no se especifica, crea un Mock)
* autospec: Si True, el mock tendrá la misma interfaz que el objeto real
* return_value: Valor que devolverá el mock cuando sea llamado
* side_effect: Permite lanzar excepciones o devolver valores dinámicos

## ¿Qué es `side_effects`?

`side_effect` es un atributo especial de los mocks que permite cambiar el comportamiento cuando se llama al mock. Estos son usados comúnmente para simular errores como si algo hubiera fallado, simular respuestas diferentes cada vez que se llama y crear un comportamiento personalizado.

* `side_effects` para simular excepciones (como si fallara una API):

    ```python
    mock = Mock()
    mock.side_effect = Exception("¡Error de conexión!")  # Al llamar al mock, lanza esta excepción
    ```

* `side_effects` como un lista de valores:

    ```python
    mock = Mock()
    mock.side_effect = [10, 20, 30]  # Primera llamada: 10, segunda: 20, tercera: 30
    print(mock())  # 10
    print(mock())  # 20
    ```

* `side_effects` como lógico personalizada con funciones (como un "if" dentro del mock)
  
    ```python
    def logica_personalizada(param):
        if param == "hola":
            return "mundo"
        elif param == "error":
            raise ValueError("¡Parametro incorrecto!")

    mock = Mock()
    mock.side_effect = logica_personalizada  # ¡El mock ejecuta esta función!
    print(mock("hola"))  # "mundo"
    mock("error")        # Lanza ValueError
    ```

## Mocks en clases y métodos

### 




## Ejercicios

1. Crear una función que dependa de otra externa (por ejemplo, llamar a una API ficticia) y simular su resultado con un Mock.


