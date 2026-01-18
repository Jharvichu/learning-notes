#include <iostream>
#include <glad/glad.h>
#include <GLFW/glfw3.h>

using namespace std;

float  ColorValue(int velocity);

int main() 
{
    float greenValue, redValue, blueValue;

    // 1. Inicializar GLFW
    if (!glfwInit()) {
        cerr << "Error al inicializar GLFW" << endl;
        return -1;
    }

    // 2. Especificar version de OpenGL y funciones modernas

    // Se puede especificar mas hints (Documentacion)
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    // 3. Crear la ventana

    GLFWwindow* window = glfwCreateWindow(800, 800, "Mi primera ventana", NULL, NULL);
    
    if (window == NULL)
    {
        cout << "Fallo al crear la ventana GLFW" << endl;
        glfwTerminate();
        return -1;
    }

    // Establece el contexto 
    glfwMakeContextCurrent(window);

    // Carga la libreria OpenGL
    gladLoadGL();

    // Definir el comienzo de la ventana
    glViewport(0, 0, 800, 800);

    // 4. Loop
    while (!glfwWindowShouldClose(window)) 
    {
        glfwPollEvents();           // Procesa los eventos del SO (teclado, ratón, etc.)

        redValue = ColorValue(4);
        greenValue = ColorValue(2);
        blueValue = ColorValue(10);

        glClearColor(redValue, greenValue, blueValue, 1.0f);    // Definir el color del fondo
        glClear(GL_COLOR_BUFFER_BIT);                           // Limpia el buffer de color

        glfwSwapBuffers(window);    // Intercambia los buffers de dibujo (evita parpadeo)
    }

    glfwDestroyWindow(window);
    glfwTerminate();
    return 0;

}

float  ColorValue(int velocity) 
{
    float time = glfwGetTime();
    return (sin(velocity * time) / 2.0f) + 0.5f;
}