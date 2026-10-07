# Laboratorio 2 — Dividir y vencerás

**Nombre:** Carolina Arango Escobar

## Cómo ejecutar el laboratorio

El laboratorio se encuentra dentro de la carpeta `laboratorios/lab2-divide-y-vencer`.

Primero se debe activar el entorno virtual desde la carpeta principal del repositorio.

### Windows (CMD)

```cmd
venv\Scripts\activate
```

### Windows (PowerShell)

```powershell
venv\Scripts\Activate.ps1
```

### macOS y Linux

```bash
source venv/bin/activate
```

Después se entra a la carpeta del laboratorio:

```bash
cd laboratorios/lab2-divide-y-vencer
```

Para ejecutar las pruebas de la Parte 1:

```bash
python pruebas.py
```

Para realizar las mediciones y generar la gráfica:

```bash
python medicion.py
```

Los comandos `python pruebas.py` y `python medicion.py` se ejecutan desde la carpeta `lab2-divide-y-vencer`.

## Parte 1 — Implementar y verificar las soluciones

Código utilizado:

* [subarreglo.py](subarreglo.py)
* [pruebas.py](pruebas.py)

En esta parte se implementaron dos formas de encontrar el subarreglo de suma máxima. La primera utiliza fuerza bruta y prueba los diferentes tramos posibles acumulando sus sumas. La segunda utiliza divide y vencerás, separando la lista en dos partes y teniendo en cuenta el mejor tramo de la izquierda, el de la derecha y el que cruza el punto medio.

Para verificar que las dos soluciones funcionaran correctamente se hicieron varias pruebas. Primero se utilizó la serie de ocho días de la situación planteada, cuyo resultado esperado es una suma de `17`. También se probó una lista de un solo elemento, una lista con todos los valores negativos y otra con todos los valores positivos.

Además, se hizo una prueba donde el mejor tramo cruza el punto medio. También se comprobó que las funciones no modificaran la lista original. Finalmente, se generaron 20 listas aleatorias y se comparó la suma obtenida por los dos algoritmos.

Las pruebas se realizaron usando `assert`. Si todas son correctas, el programa termina mostrando:

```text
Todas las pruebas pasaron correctamente.
```

## Parte 2 — Medición y gráfica

Código utilizado:

* [medicion.py](medicion.py)

Para esta parte se midió el tiempo de ejecución de los dos algoritmos usando siete tamaños de entrada: `10`, `50`, `100`, `200`, `400`, `1000` y `4000`.

Los datos se generaron con una semilla fija y con valores enteros entre `-100` y `100`. Para cada tamaño se utilizó exactamente la misma lista para los dos algoritmos, para que la comparación se hiciera sobre los mismos datos.

El tiempo se midió utilizando `time.perf_counter()` y solamente se tuvo en cuenta el tiempo de ejecución de cada algoritmo. La generación de los datos y la comprobación de que ambos algoritmos encontraran la misma suma se hicieron por fuera de la medición.

Cada tamaño se midió tres veces y se utilizó la mediana de los resultados para reducir el efecto de posibles variaciones pequeñas en los tiempos.

Los resultados obtenidos fueron:

| Tamaño (n) | Fuerza bruta (s) | Divide y vencerás (s) |
| ---------: | ---------------: | --------------------: |
|         10 |         0.000003 |              0.000006 |
|         50 |         0.000032 |              0.000032 |
|        100 |         0.000120 |              0.000068 |
|        200 |         0.000492 |              0.000136 |
|        400 |         0.002031 |              0.000304 |
|       1000 |         0.013418 |              0.000828 |
|       4000 |         0.214927 |              0.003559 |

### Gráfica

La siguiente gráfica muestra los tiempos obtenidos para los dos algoritmos:

![Tiempo de ejecución de los algoritmos](graficas/tiempo_vs_n.png)

En los tamaños pequeños los tiempos son bastante cercanos. A medida que aumenta el tamaño de la entrada se empieza a notar más la diferencia entre los dos algoritmos. En `n = 4000`, fuerza bruta tarda `0.214927 s`, mientras que divide y vencerás tarda `0.003559 s`.

## Parte 3 — Análisis

### 1. Recurrencia

Para divide y vencerás, el problema se divide en dos partes de tamaño aproximadamente `n/2`. Después se busca el mejor subarreglo que cruza el punto medio. Este último paso cuesta `Θ(n)` porque se recorren los elementos de las dos mitades.

Por eso la recurrencia es:

`T(n) = 2T(n/2) + Θ(n)`

En el Teorema Maestro:

* `a = 2`
* `b = 2`
* `f(n) = Θ(n)`

Calculamos:

`n^(log₂ 2) = n`

Como `f(n)` tiene el mismo orden que `n^(log₂ 2)`, corresponde al caso 2 del Teorema Maestro. Por lo tanto:

`T(n) = Θ(n log n)`

Para fuerza bruta, los dos ciclos permiten revisar todos los posibles tramos de la lista, por lo que su complejidad es `Θ(n²)`.

### 2. Lo medido contra lo esperado

Los resultados muestran que fuerza bruta crece más rápido que divide y vencerás. Por ejemplo, al pasar de `n=100` a `n=200`, fuerza bruta pasó de `0.000120 s` a `0.000492 s`, un aumento de aproximadamente `4.10` veces.

En cambio, divide y vencerás pasó de `0.000068 s` a `0.000136 s`, un aumento de `2` veces.

También de `n=200` a `n=400`, fuerza bruta aumentó aproximadamente `4.13` veces y divide y vencerás aproximadamente `2.24` veces.

Esto se parece a lo esperado por las complejidades teóricas: al duplicar `n`, `Θ(n²)` crece cerca de 4 veces, mientras que `Θ(n log n)` crece un poco más de 2 veces.

### 3. Tamaños pequeños

En los tamaños pequeños no siempre gana divide y vencerás. Con `n=10`, fuerza bruta fue más rápida (`0.000003 s` frente a `0.000006 s`) y con `n=50` los dos tiempos fueron iguales.

Desde `n=100` en nuestra medición empieza a verse la ventaja de divide y vencerás. Esto puede pasar porque con entradas pequeñas el costo adicional de las llamadas recursivas y de dividir el problema puede compensar la ventaja de tener una menor complejidad.

### 4. ¿Cuándo conviene dividir?

Para encontrar el máximo valor de un arreglo se puede recorrer una sola vez y guardar el mayor valor encontrado. Esto tiene un costo de `Θ(n)`.

Si se divide el arreglo en dos partes, la recurrencia sería:

`T(n) = 2T(n/2) + Θ(1)`

porque después de resolver las dos partes solamente sería necesario comparar sus resultados. Esta recurrencia también da como resultado `Θ(n)`.

Por lo tanto, dividir el arreglo no mejora la complejidad en este problema. Recorrerlo directamente es más sencillo y tiene el mismo orden de crecimiento.

### 5. Concepto para la gerente

Recomendaría utilizar divide y vencerás para la cooperativa, especialmente si se van a analizar cientos de miles o millones de registros.

En la medición con `n=4000`, fuerza bruta tardó `0.214927 s`, mientras que divide y vencerás tardó `0.003559 s`. Esto muestra una diferencia importante incluso con una cantidad relativamente pequeña de datos.

Para estimar qué ocurriría con `1.000.000` de registros no se utilizó una simple regla de tres. Se tomó como referencia la medición de `n=4000` y se tuvo en cuenta la complejidad de cada algoritmo.

Para fuerza bruta, que es `Θ(n²)`, se escala el tiempo usando el factor cuadrático:

`0.214927 × (1.000.000 / 4.000)² ≈ 13.432,94 segundos`

Esto corresponde aproximadamente a **3,73 horas**.

Para divide y vencerás, que es `Θ(n log n)`, se utiliza el crecimiento de `n log n`:

`0.003559 × [(1.000.000 log₂(1.000.000)) / (4.000 log₂(4.000))] ≈ 1,48 segundos`

Por lo tanto, para `1.000.000` de registros se estima aproximadamente **3,73 horas para fuerza bruta** y **1,48 segundos para divide y vencerás**.

Estos valores son solamente estimaciones basadas en las mediciones realizadas y en las complejidades teóricas; no representan una medición real con un millón de registros. Aun así, la diferencia estimada muestra que para cantidades grandes de datos es mucho más conveniente utilizar divide y vencerás.
