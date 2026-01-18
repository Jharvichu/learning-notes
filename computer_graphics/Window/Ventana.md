# **Creación del Contexto y Ventana (OpenGL/GLFW)**

Este apunte resume los conceptos para levantar una aplicación gráfica (ventana), explicando el rol de las dependencias y la API de gestión de ventanas.

## **¿Qué hace cada librería?**
Antes de escribir código, es importante entender por qué necesitamos herramientas externas, ya que OpenGL por sí mismo no puede crear ventanas.

### GLFW ([Graphics Library Framework](https://www.glfw.org/docs/latest/pages.html))

¿Por qué la usamos? OpenGL es una especificación gráfica, no un sistema de ventanas. No sabe cómo crear una ventana en Windows, Linux o macOS, ni cómo leer el teclado o el mouse.

#### Funcionalidad:

- Crea y gestiona ventanas y contextos de OpenGL.
- Maneja la entrada (Input) de teclado, mouse y joysticks.
- Gestiona múltiples monitores y modos de video (pantalla completa/ventana).

### GLAD (OpenGL Loader Generator)
¿Por qué la usamos? Los drivers de las tarjetas gráficas (NVIDIA, AMD, Intel) implementan las funciones de OpenGL en archivos binarios (.dll o .so). La ubicación de estas funciones no se conoce en tiempo de compilación.

#### Funcionalidad:

- Busca la dirección de memoria de las funciones de OpenGL (ej: glViewport, glClear) en tiempo de ejecución para que podamos llamarlas.

## **Conceptos de la API de GLFW**

### Configuración de la Ventana (Hints)

Antes de crear la ventana, debemos configurar cómo será. Esto se hace mediante "Hints" (Pistas o Sugerencias). Funcionan como una configuración previa. Si no se configuran, GLFW usa valores por defecto.

Función: `glfwWindowHint(GLenum hint, int value)`

| Hint (Opción) | Valor Común | Descripción |
|----------------|--------------|--------------|
| `GLFW_CONTEXT_VERSION_MAJOR` | `3` | Versión mayor de OpenGL requerida. |
| `GLFW_CONTEXT_VERSION_MINOR` | `3` | Versión menor de OpenGL requerida. |
| `GLFW_OPENGL_PROFILE` | `GLFW_OPENGL_CORE_PROFILE` | Usa el perfil moderno (descarta funciones obsoletas). |
| `GLFW_RESIZABLE` | `GLFW_FALSE` | **UI/UX:** Impide que el usuario cambie el tamaño de la ventana. |
| `GLFW_FLOATING` | `GLFW_TRUE` | **Debug:** Mantiene la ventana siempre encima de otras ("Always on top"). |
| `GLFW_DECORATED` | `GLFW_FALSE` | **Estilo:** Quita bordes y barra de título (útil para *splash screens*). |
| `GLFW_TRANSPARENT_FRAMEBUFFER` | `GLFW_TRUE` | **Estilo:** Permite transparencia en la ventana (requiere soporte del OS). |

### Creación del Objeto

La función `glfwCreateWindow` devuelve un puntero `GLFWwindow*`. Este puntero es el identificador único de nuestra ventana y se pasará a casi todas las funciones de GLFW subsiguientes.

> **Importante**: Al crear la ventana, también se crea un Contexto de OpenGL asociado a ella, pero este contexto no está activo automáticamente. Debemos llamar a `glfwMakeContextCurrent(window)` para decirle al hilo de ejecución actual que dibuje sobre esa ventana.

### El Viewport

No confundir el tamaño de la ventana (GLFW) con el tamaño del renderizado (OpenGL).

- Ventana: Dimensiones en coordenadas de pantalla del SO.
- Viewport (glViewport): Área dentro de la ventana donde OpenGL puede dibujar. Transforma las coordenadas normalizadas (-1 a 1) a píxeles (0 a 800).

## **Ciclo de Vida y Double Buffering**
El "Render Loop" mantiene la aplicación viva. Dentro de este ciclo ocurre un proceso crítico llamado Double Buffering (Doble Búfer).

- Front Buffer: Contiene la imagen final que el monitor está mostrando actualmente.
- Back Buffer: Es donde se están ejecutando los comandos de dibujo actuales (`glClear`, `DrawTriangles`, etc.).

Si dibujáramos directamente en el Front Buffer, el usuario vería parpadeos y artefactos mientras la imagen se construye. Por eso dibujamos en el Back Buffer y, al terminar el frame, usamos `glfwSwapBuffers` para intercambiarlos instantáneamente.

### Funciones extra

#### Control de Flujo y Eventos

- `glfwInit()` / `glfwTerminate()`: Inicia y destruye la librería completa.
- `glfwWindowShouldClose(window)`: Retorna un booleano (flag). Se usa como condición del while.
- `glfwSetWindowShouldClose(window, true)`: Fuerza el cierre de la ventana manualmente (ej: al presionar ESC).
- `glfwPollEvents()`: Procesa eventos pendientes en la cola (teclas presionadas, movimiento de mouse). Si no se llama, la ventana se congelará.

#### Callbacks (Reacción a eventos)

- GLFW usa punteros a funciones para notificar cambios.
- `glfwSetFramebufferSizeCallback(...)`: Crítico. Se dispara cuando la ventana cambia de tamaño. Aquí debemos llamar a glViewport nuevamente para ajustar el renderizado a la nueva resolución.
- `glfwSetCursorPosCallback(...)`: Para obtener la posición X, Y del mouse (útil para cámaras FPS).
- `glfwSetKeyCallback(...)`: Para detectar pulsaciones simples (no continuas).

#### Utilidades de Ventana
- `lfwSetWindowUserPointer(window, void* ptr)`: Permite guardar un puntero a una clase propia (ej: MiAplicacion*) dentro de la ventana de C. Es fundamental para conectar la API de C de GLFW con Programación Orientada a Objetos en C++.
- `glfwGetTime()`: Devuelve el tiempo en segundos desde que se inició GLFW. Esencial para calcular el DeltaTime y animaciones.
- `glfwSetInputMode(window, GLFW_CURSOR, GLFW_CURSOR_DISABLED)`: Oculta el mouse y lo captura dentro de la ventana (estándar en juegos FPS).