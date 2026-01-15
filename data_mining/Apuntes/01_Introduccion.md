# Mineria de Datos

Es el conjunto de técnicas y tecnologías que permiten explorar grandes bases de datos, de manera automática o semiautomática, con el objetivo de encontrar patrones repetitivos, tendencias o reglas que expliquen el comportamiento de los datos en un determinado contexto. 

> **Knowledge Discovery in Database**: Descubrimiento de conocimiento en bases de datos (KDD) es el proceso de descubrir conocimiento útil a partir de una colección de datos.

```
DATOS -> INFORMACION -> CONOCIMIENTO
```

#### ¿ Qué tipos de datos hay ?

| Categoría de datos        | Descripción breve                     | Ejemplos de formatos                  |
|---------------------------|----------------------------------------|----------------------------------------|
| Datos estructurados       | Datos organizados en tablas            | SQL tables, CSV                        |
| Datos semiestructurados   | Datos con estructura flexible          | HTML, XML, JSON, YAML                 |
| Datos no estructurados    | Datos sin estructura definida          | MP3, MP4, MKV, DOC, TXT, JPG, PNG     |

## Proceso de la mineria de datos

Un proceso típico de minería de datos consta de los siguientes pasos generales:
1. **Selección del conjunto de datos**, tanto en lo que se refiere a las variables objetivo (aquellas que se quiere predecir, calcular o inferir), como a las variables independientes (las que sirven para hacer el cálculo o proceso), como posiblemente al muestreo de los registros disponibles.
2. **Análisis de las propiedades de los datos**, en especial los histogramas, diagramas de dispersión, presencia de valores atípicos y ausencia de datos.
3. **Transformación del conjunto de datos de entrada**, se realizará de diversasformas en función del análisis previo, con el objetivo de prepararlo para aplicar la técnica de minería de datos que mejor se adapte a los datos y al problema, a este paso también se le conoce como *preprocesamiento de los datos*.
4. **Seleccionar y aplicar la técnica de minería de datos**, se construye el modelopredictivo, de clasificación o segmentación.
5. **Extracción de conocimiento**, mediante una técnica de minería de datos, se obtiene un modelo de conocimiento, que representa patrones de comportamiento observados en los valores de las variables del problema o relaciones de asociación entre dichas variables. También pueden usarse varias técnicas a la vez para generar distintos modelos, aunque generalmente cada técnica obliga a un preprocesado diferente de los datos.
6. **Interpretación y evaluación de datos**, una vez obtenido el modelo, se debe proceder a su
validación comprobando que las conclusiones que arroja son válidas y suficientemente
satisfactorias. En el caso de haber obtenido varios modelos mediante el uso de distintastécnicas,
se deben comparar los modelos en busca de aquel que se ajuste mejor al problema. Si ninguno
de los modelos alcanza los resultados esperados,debe alterarse alguno de los pasos anteriores
para generar nuevos modelos.

---

## Data Mining vs Machine Learning

| Aspecto | Data Mining | Machine Learning |
|-------|-------------|------------------|
| Enfoque | Descubrimiento de patrones ocultos o conocimiento a partir de los datos | Desarrollo de algoritmos que aprenden a partir de los datos |
| Objetivo | Extraer información y conocimiento de datasets existentes | Construir modelos para hacer predicciones o realizar tareas |
| Uso | Identificar patrones, tendencias y anomalías | Modelado predictivo, clasificación, clustering, etc. |
| Entrada | Datos históricos o grandes volúmenes de datos | Datos etiquetados o no etiquetados para entrenamiento y prueba |
| Salida | Conocimiento en forma de patrones o reglas | Predicciones, clasificaciones, recomendaciones, etc. |
| Métodos | Estadística descriptiva, clustering, reglas de asociación | Árboles de decisión, regresión, redes neuronales, SVM, etc. |
| Alcance | Más amplio en el análisis de distintos tipos de datos | Enfocado en desarrollar modelos para aplicaciones específicas |
| Dominio | Muy usado en negocios, marketing, salud, etc. | Muy usado en IA, robótica, reconocimiento de patrones, etc. |



---

### Bussines Analytics:

Extraer conocimiento, patrones y predicciones. Por ejemplo:

- Análisis de comentarios de clientes (texto)
- Análisis de imágenes o videos
- Predicción de demanda
- Machine Learning

Tabaja principalmente con **Datos estructurados**, **Datos semiestructurados** y **Datos no estructurados**, osea con fuentes como Texto libre, imagenes, audio, video, logs, redes sociales, etc. 

---

### Business Intelligence:

Convertir datos en información comprensible. Por ejemplo:

- Tablas SQL
- CSV
- JSON controlado
- Reportes de ventas, KPIs

Tabaja principalmente con **Datos estructurados** y **Datos semiestructurados**, ya que los datos estan organizados, limpios y modelados

#### **SQL Server para BI**

1. Integration Services (SSIS): SSIS es la herramienta de **integración y procesamiento** de datos de SQL Server.
Su función principal es realizar procesos ETL:

   - Extract (Extraer datos de fuentes heterogeneas como oracle, csv, wiki, etc)
   - Transform (Tranformar los datos, limpiar, estandariza, etc)
   - Load (Sube o se carga en un data warehouse)

2. Analysis Services (SSAS): SSAS es el servicio que permite **analizar** grandes volúmenes de datos de forma eficiente usando modelos analíticos. Existen dos tipos de modelos:

    - Multidimensional (Cubo OLAP, Data Mart)
    - Tabular (Dimensional table, Facts table)

3. Reporting Services (SSRS): SSRS es la herramienta de creación de reportes empresariales. Permite crear:

    - Reportes tabulares
    - Reportes graficos
    - Dashboards interactivos

| Característica | MDX (Multidimensional Expressions) | DAX (Data Analysis Expressions) |
|---------------|-----------------------------------|---------------------------------|
| Uso principal | Consultas y cálculos en cubos OLAP | Cálculos y análisis en modelos tabulares |
| Modelo de datos | Multidimensional (cubos OLAP) | Tabular (tablas y relaciones) |
| Dónde se usa | SQL Server Analysis Services (SSAS Multidimensional) | Power BI, SSAS Tabular, Power Pivot |
| Tipo de lenguaje | Lenguaje de consultas | Lenguaje de fórmulas |
| Enfoque | Navega dimensiones y jerarquías | Trabaja con columnas, filas y filtros |
| Complejidad | Más complejo y menos intuitivo | Más sencillo y similar a Excel |
| Forma de consulta | Basado en ejes (filas, columnas, páginas) | Basado en contexto de filas y filtros |

## Conceptos

1. **Data Warehouse**: es un repositorio central de datos diseñado para almacenar, integrar y analizar información histórica proveniente de múltiples fuentes (bases de datos, sistemas transaccionales, archivos, APIs, etc.), con el objetivo principal de apoyar la toma de decisiones
2. **Data Mart**: es un subconjunto de un Data Warehouse, diseñado para atender un área específica del negocio y facilitar análisis más rápidos y enfocados.
3. **Cubo OLAP**: es una estructura de datos multidimensional que permite analizar información desde diferentes perspectivas de forma rápida e interactiva, normalmente sobre datos almacenados en un Data Warehouse.
4. **Dimensional Table**: Una tabla dimensional describe una entidad del negocio. No mide nada, solo da contexto a los datos como tabla usuarios, rol, etc.
5. **Facts Table**: Una tabla de hechos registra eventos reales del negocio. Es donde se guardan los datos que se quieren medir como una tabla llamada asignacion que tiene horas trabajados o salario.