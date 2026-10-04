# Laboratorio 2 — Dividir y vencer

**Nombre:** Carolina Arango Escobar

## Cómo ejecutar el laboratorio

Primero se debe activar el entorno virtual desde la carpeta principal del repositorio:

```cmd
venv\Scripts\activate
```

Después se entra a la carpeta del laboratorio:

```cmd
cd laboratorios\lab2-divide-y-vencer
```

Para ejecutar las pruebas de la Parte 1 se utiliza:

```cmd
python pruebas.py
```

## Parte 1 — Implementar y verificar las soluciones

Código utilizado:

* [subarreglo.py](subarreglo.py)
* [pruebas.py](pruebas.py)

En esta parte se implementaron dos formas de encontrar el subarreglo máximo. La primera utiliza fuerza bruta y prueba los diferentes tramos posibles acumulando la suma. La segunda utiliza divide y vencerás, separando la lista en dos partes y teniendo en cuenta los casos izquierdo, derecho y cruzado.

Para verificar que las dos soluciones funcionaran correctamente se hicieron varias pruebas. Primero se utilizó la serie de ocho días de la situación planteada, cuyo resultado esperado es una suma de `17`. También se probó una lista de un solo elemento, una lista con todos los valores negativos y otra con todos los valores positivos.

Además, se hizo una prueba donde el mejor tramo cruza el punto medio, para comprobar que esta parte del algoritmo funcionara correctamente. Finalmente, se generaron 20 listas aleatorias y se comparó la suma obtenida por los dos algoritmos.

Las pruebas se realizaron usando `assert` y todas las pruebas deben terminar mostrando el mensaje:

```text
Todas las pruebas pasaron correctamente.
```

## Parte 2 — Medición y gráfica

Código utilizado:

* [medicion.py](medicion.py)

Para esta parte se midió el tiempo de ejecución de los dos algoritmos usando diferentes tamaños de entrada. Los tamaños utilizados fueron `10`, `50`, `100`, `200`, `400`, `1000` y `4000`.

Los datos se generaron con una semilla fija y con valores enteros entre `-100` y `100`. Para cada tamaño se utilizó la misma lista para los dos algoritmos, para que la comparación fuera sobre los mismos datos.

El tiempo se midió utilizando `time.perf_counter()` y solamente se tuvo en cuenta el tiempo de ejecución de cada algoritmo. La generación de los datos y la comprobación de los resultados se hicieron por fuera de la medición.

Cada medición se repitió tres veces y se utilizó la mediana de los tiempos para reducir un poco las variaciones que pueden ocurrir durante la ejecución.

También se verificó dentro del experimento que la suma encontrada por fuerza bruta y por divide y vencerás fuera la misma para cada tamaño.

### Gráfica

La siguiente gráfica muestra los tiempos obtenidos para los dos algoritmos:

![Tiempo de ejecución de los algoritmos](graficas/tiempo_vs_n.png)

En la gráfica se pueden comparar las dos curvas a medida que aumenta el tamaño de la entrada. La fuerza bruta aumenta más rápido, mientras que divide y vencerás mantiene tiempos menores en los tamaños más grandes.
