# Docker

Docker es una plataforma simplifica el proceso de creación, implementación y gestión de aplicaciones mediante el uso de contenedores. Los contenedores te permiten empaquetar una aplicación con sus dependencias en una unidad estandarizada para el desarrollo de software.

### Dockerfile

Un archivo de texto que contiene instrucciones para construir una imagen de Docker. Especifica la imagen base, establece el directorio de trabajo, instala dependencias, copia el código de la aplicación, expone puertos y define comandos para ejecutar la aplicación.

### ¿Qué es un contenedor?

Una instancia de una imagen de Docker que se ejecuta como un proceso en la máquina anfitriona. Los contenedores son ligeros, portátiles y aislados, lo que los hace ideales para desplegar y escalar aplicaciones.

### ¿Qué es una imagen?

Una imagen es un archivo que representa una plantilla para la creacion de contenedores. A partir de una imagen se pueden generar diferentes contenedores para diferentes propositos.

### ¿Qué es un volumen?

Un volumen es un mecanismo de almacenamiento persistente que se utiliza para almacenar y gestionar datos que sobreviven en el ciclo de vida de un contenedor, es decir, que los datos se guardan fuera del contenedor (en la maquina host), permitiendo ser utilizado incluso si se elimina, actualiza o reinicia el contenedor.

### Beneficios

- Entornos consistentes, ligeros y aislados
- Las implementaciones corren en segundos
- Agiliza el proceso de desarrollo
- Capacidad de automatización
- Soporte a practicas Agiles, CI CD y DevOps
- Facil versionado

## Dockerfile

A continuación se muestra un ejemplo de Dockerfile para referencia. La explicación siguiente detalla los comandos utilizados, proporcionando una comprensión completa de cómo escribir un Dockerfile.

```Dockerfile
# Usamos una imagen oficial de Python como base
FROM python:3.9

# Establecemos variables de entorno
ENV FLASK_ENV=production
ENV PORT=5000

# Creamos y usamos un directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos de dependencias (requisitos)
COPY requirements.txt .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código de la aplicación
COPY . .

# Añadimos un archivo específico (por ejemplo, una página HTML)
ADD templates/index.html /app/templates/index.html

# Exponemos el puerto de la aplicación
EXPOSE $PORT

# Comando por defecto al iniciar el contenedor
CMD ["python", "app.py"]

# Etiquetas para identificar la imagen
LABEL version="1.0"
LABEL description="Imagen Docker de una aplicación Flask en Python"
LABEL maintainer="Tu Nombre"

# Healthcheck para verificar que el contenedor funcione bien
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:$PORT || exit 1
```

Con estos archivos de apoyo para el contenedor

Archivo `app.py`
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

Archivo `requirements.txt`
```nginx
flask
```

Archivo `templates/index.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Mi App Flask</title>
</head>
<body>
    <h1>¡Hola desde Flask en Docker!</h1>
</body>
</html>
```

### Comprendiendo el Dockerfile

1. **Especificar la imagen base**
    ```Dockerfile
    FROM python:3.9
    ```
    `FROM`: especifica la imagen base del contenedor de Docker.

2. **Establecer variables de entorno**
    ```Dockerfile
    ENV FLASK_ENV=production
    ENV PORT=5000
    ```
    `ENV`: establece variables de entorno dentro del contenedor de Docker.

3. **Establecer directorio de trabajo**
    ```Dockerfile
    WORKDIR /app
    ```
    `WORKDIR`: define el directorio de trabajo para las intrucciones posteriores, simplificando las referencias a las rutas posteriores

4. **Copiar archivos de paquete**
    ```Dockerfile
    COPY requirements.txt .
    ```
    `COPY`: copia archivos de tu maquina local al contenedor

5. **Instalar dependencias**
   ```Dockerfile
   RUN pip install --no-cache-dir -r requirements.txt
   ```
   `RUN`: Ejecuta comandos en el contenedor durante el proceso de construcción

6. **Copiar el código de la aplicación**
   ```Dockerfile
   COPY . .
   ```
   `COPY`: Copia todos los archivos y directorios desde el directorio actual en el host local al directorio actual en el contenedor de Docker.


7. **Añadir archivos adicionales**
   ```Dockerfile
   ADD templates/index.html /app/templates/index.html
   ```

    `ADD`: Se utiliza para incluir cualquier archivo extra.
      
8. **Exponer el puerto de la aplicacion**
    ```Dockerfile
    EXPOSE $PORT
    ```

    `EXPOSE`: Informa a Docker que el contenedor escuchará en el puerto especificado en tiempo de ejecución.

9.  **Especificar el comando predeterminado**
    ```Dockerfile
    CMD ["python3","app.py"]
    ```
    `CMD`: Esta instrucción especifica el comando y/o parámetros predeterminados a ejecutar en el punto de entrada del contenedor.
    
10. **Etiquetar la imagen**
    ```Dockerfile
    LABEL version="1.0"
    LABEL description="Python application Docker image"
    LABEL maintainer="Your Name"
    ```

    `LABEL`: Agrega metadatos a la imagen de Docker.
    
11. **Agregar un Healthcheck**
    ```Dockerfile
    HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 CMD curl -fs http://localhost:$PORT || exit 1
    ```

    `HEALTHCHECK`: Configura una verificación de salud para asegurar que el contenedor esté funcionando correctamente.

## Docker CLI
Comandos utilizados para el manejo de Docker (imagenes, contenedores) y comandos para el uso de IBM Cloud para el registro de imagenes y contendedores.

| **Comandos** | **Descripción** |
|---------|-------------|
| `docker build` | Construye una imagen a partir de un Dockerfile. |
| `docker build . -t` | Construye la imagen y etiqueta el id de la imagen. |
| `docker container rm` | Elimina un contenedor. |
| `docker images` | Lista las imágenes. |
| `docker ps` | Lista los contenedores. |
| `docker ps -a` | Lista los contenedores que se ejecutaron y salieron con éxito. |
| `docker pull` | Descarga la última imagen o repositorio de un registro. |
| `docker push` | Sube una imagen o un repositorio a un registro. |
| `docker run` | Ejecuta un comando en un nuevo contenedor. |
| `docker run -p` | Ejecuta el contenedor publicando los puertos. |
| `docker stop` | Detiene uno o más contenedores en ejecución. |
| `docker stop $(docker ps -q)` | Detiene todos los contenedores en ejecución. |
| `docker tag` | Crea una etiqueta para una imagen de destino que se refiere a una imagen de origen. |
| `docker --version` | Muestra la versión del Docker CLI. |
| `ibmcloud cr images` | Lista imágenes en el Registro de Contenedores de IBM Cloud. |
| `ibmcloud cr login` | Inicia sesión en el registro de contenedores de IBM Cloud desde tu daemon de Docker local. |
| `ibmcloud cr namespaces` | Muestra los espacios de nombres a los que tienes acceso. |
| `ibmcloud cr region-set` | Asegura que estás apuntando a la región adecuada para tu cuenta en la nube. |
| `ibmcloud target` | Proporciona información sobre la cuenta que estás apuntando. |
| `ibmcloud version` | Muestra la versión del IBM Cloud CLI. |

