# Regresion Lineal

La regresión lineal es un método supervisado que busca modelar la relación entre una o más variables de entrada (features) y una variable de salida (target), asumiendo que esta relación es lineal.

Digamos que tenemos el siguiente archivo `casa_venta.csv`:

| Id | Antiguedad | Año | #Cuartos | #Baños | #Pisos | ... | Precio |
|----|------------|-----|----------|--------|--------|-----|--------|
|----|------------|-----|----------|--------|--------|-----|--------|
|----|------------|-----|----------|--------|--------|-----|--------|

- Variables independientes (x): entradas o features
- Variables dependientes (y): salida o target

Planteamos una hipotesis para el modelo de la siguiente manera (Funcion Objetivo)

$$
h_\theta(x) = \theta_0 + \theta_1 x
$$

Donde los parametros son $\theta_0, \theta_1$ o tambien llamados pesos $w_0, w_1$. Trataremos de minizar la diferencia entre la recta prediccion $h_\theta(x)$ y $y$

## Funcion de Costo

Mide qué tan lejos están las predicciones del modelo respecto a los valores reales:

$$
J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})^2
$$

Donde $m$ es el numero de ejemplos

## Descenso del gradiente

Encontrar los valores de $\theta_0$ y $\theta_1$ que minimizan $J(\theta)$.

**Algoritmo:**

$$
\theta_j := \theta_j - \alpha \frac{\partial J(\theta)}{\partial \theta_j}
$$

Donde:
- $\alpha$: tasa de aprendizaje (*learning rate*), $0 < \alpha < 1$
- $\frac{\partial J}{\partial \theta_j}$: gradiente (pendiente de la función de costo)

## Elección del *learning rate* ($\alpha$)

| Caso | Efecto |
|------|---------|
| $\alpha$ muy grande | No converge (rebota) |
| $\alpha$ muy pequeño | Converge lento |
| $\alpha$ adecuado | Disminuye $J$ suavemente hasta el mínimo |







### Dataset

Este tiene como variables de entrada: variables independientes, atributos, caracteristicas, features, variables predictivas y variables de salida: variables dependientes, variables objetivo y targets.