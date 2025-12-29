# Infrastructura como Código

La infraestructura como código (IaC del ingles Infrastructure as Code) es la capacidad de aprovisionar y respaldar su infraestructura de computación como sistemas operativos, conexiones de bases de datos, almacenamiento, etc, a través de código en lugar de procesos y configuraciones manuales. 

Con este tipo de infraestructura, se crean archivos de configuración que contienen las especificaciones que esta necesita, lo cual facilita la edición y la distribución de las configuraciones. Asimismo, garantiza que siempre se prepare el mismo entorno.

Tradicionalmente el aprovisonamiento de TI era costoso y requeria mucho tiempo, que requería la configuración física del hardware, instalacion y configuracion del sistema operativo, conecciones, etc.

Hoy en día, puede usar IaC para configurar automáticamente su entorno en cuestión de minutos y administrarlo de manera más eficiente. Los beneficios que hay al utilizar IaC son:

* Tiempo de producción o comercialización más rápido
* Reduccion de costos
* Disminución de la cantidad de errores
* Mayor uniformidad de la infrastructura

## Tipo de Infrastructura como Código

### Infrastructura mutable

La infraestructura mutable es aquella que puede modificarse o actualizarse tras su aprovisionamiento inicial. Ofrece a los equipos de desarrollo la flexibilidad de realizar personalizaciones en los servidores para, por ejemplo, ajustarse mejor a los requisitos de desarrollo o de la aplicación, o responder a un problema de seguridad emergente.

### Infrastructura inmutable

infraestructura inmutable es aquella infraestructura que no se puede modificar tras su aprovisionamiento original. Si es necesario cambiar la infraestructura inmutable, debe reemplazarse por una nueva. Dado que la nueva infraestructura se puede implementar rápidamente en la nube, especialmente con IaC, la infraestructura inmutable es mucho más viable y práctica.

## Enfoques de la Infrastrucutura como Código

### Declarativa

La IaC declarativa permite al desarrollador describir los recursos y la configuración que componen el estado final de un sistema deseado. Esto hace que la IaC declarativa sea fácil de usar, siempre que el desarrollador sepa qué componentes y configuraciones necesita para ejecutar su aplicación.

### Imperativa

La IaC imperativa permite al desarrollador describir todos los pasos para configurar los recursos y llegar al sistema y al estado de ejecución deseados. Si bien no es tan sencillo escribir la IaC imperativa como la IaC declarativa, el enfoque imperativo se hace necesario en las implementaciones de infraestructuras complejas.

## La importancia de la Infrastructure as Code para DevOps

La Infrastructure as Code es fundamental en la implementación de las prácticas de DevOps y de la integración y distribución continuas (CI/CD). Esto libera a los desarrolladores de tener que realizar la mayor parte del trabajo de preparación, ya que solo deben ejecutar un script y la infraestructura estará lista para funcionar.

De este modo, las implementaciones de aplicaciones no necesitan esperar a la infraestructura, y los administradores de sistemas no tienen que gestionar procesos manuales que consumen mucho tiempo.

