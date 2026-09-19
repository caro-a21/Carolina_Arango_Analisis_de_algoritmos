# Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias

**Estudiante:** Carolina Arango Escobar

## Instrucciones para reproducir el experimento
Los algoritmos base se encuentran en [`algoritmos.py`](algoritmos.py) y los generadores de datos en [`datos.py`](datos.py). 

Para reproducir este laboratorio, abre la consola (CMD) en la raíz del repositorio y ejecuta:
1. Activar el entorno virtual: `venv\Scripts\activate.bat`
2. Ejecutar experimento de la Parte 3: `python lab1-fundamentos-complejidad-recurrencias/parte3_casos.py`
3. Ejecutar experimento de la Parte 4: `python lab1-fundamentos-complejidad-recurrencias/parte4_complejidad.py`

---

## Parte 1 — Analizar el algoritmo antes de comprar hardware

Un algoritmo correcto es el que da el resultado que esperamos, pero uno eficiente también tiene que hacerlo en el tiempo que tenemos disponible, en este caso 4 horas.

Por ejemplo, en Black Friday una tienda recibe muchísimas compras y necesita revisar cuáles productos se vendieron más. Si el programa compara cada compra con todas las demás, puede llegar al resultado correcto, pero se puede demorar demasiado.

Si hay 1.000 compras, hace muchísimas comparaciones, y si las compras aumentan a 2.000, el trabajo aumenta mucho más, porque el algoritmo crece como n².

Entonces, aunque dupliquemos el hardware y tengamos un computador más potente, no necesariamente se soluciona el problema. Si siguen aumentando las compras, el programa puede terminar demorándose más de las 4 horas permitidas.

Por eso, no solo importa que el algoritmo funcione, sino que también sea lo suficientemente rápido para las condiciones que tenemos.


---

## Parte 2 — Responsabilidad ambiental y ética de la implementación

La eficiencia de un algoritmo también tiene que ver con la cantidad de energía y recursos que utiliza el computador. Si un algoritmo es poco eficiente, puede tardar más tiempo y hacer que el procesador trabaje más, gastando más energía.

Esto puede traer algunos problemas, como un mayor consumo de electricidad y más uso del computador. Además, cuando se manejan muchos datos, esto puede hacer que otros programas tengan menos recursos disponibles.

Por eso, la responsabilidad es de todos. Los desarrolladores deben intentar crear algoritmos que sean adecuados y no gasten recursos de más. Por otro lado, las organizaciones también deben dar los recursos necesarios y tratar de usar la tecnología de una manera responsable.

---
### Parte 3 — Peor caso, mejor caso y caso promedio

#### 3.1 — Explicación teórica

El peor caso de un algoritmo es la entrada que hace el mayor número de comparaciones o el mayor tiempo de ejecución dentro de todas las entradas posibles de un tamaño fijo `n`. El mejor caso es la entrada que necesita el menor número de comparaciones o tiempo para ese mismo tamaño. El caso promedio representa el comportamiento medio sobre un conjunto de entradas de tamaño `n`, considerando cómo se distribuyen las entradas.

En insertion sort, el peor caso es cuando los elementos están en sentido contrario al que necesitamos, porque el algoritmo debe mover muchos elementos. El mejor caso ocurre cuando la lista ya está ordenada y casi no se necesitan movimientos. El caso promedio es el que tiene entradas que no están completamente ordenadas ni completamente al revés.

Para decidir si Tamiza puede utilizar un algoritmo en producción, utilizaría el peor caso que considere entradas difíciles. Esto por que la ventana de cuatro horas es estricta y no se puede asumir que siempre llegarán datos fáciles de ordenar. El sistema debe terminar a las 6:00 a. m. para que los pacientes sean contactados correctamente.

Antes de realizar las mediciones, mi predicción es que el escenario C será el peor caso, porque los datos llegan de menor a mayor y Tamiza necesita ordenarlos de mayor a menor. El escenario B se acercará al mejor caso, porque el 98 % inicial ya está ordenado y solo una parte pequeña está desordenada al final. El escenario A se aproximará al caso promedio, porque sus datos llegan en un orden aleatorio.

#### 3.2 — Demostración experimental

El código utilizado para realizar el experimento se encuentra en [código de la Parte 3](parte3_casos.py). La implementación de insertion sort está en [algoritmos.py](algoritmos.py) y los generadores de los escenarios están en [datos.py](datos.py).

Para el experimento se utilizaron los tamaños de entrada 100, 200, 400, 800, 1600, 3200 y 6400. Se midió el tiempo de ejecución utilizando `time.perf_counter()` y se contó el número de comparaciones entre elementos. El tiempo de generación de los datos no se incluyó en la medición.

**Gráfica de comparaciones**

![Comparaciones de insertion sort](graficas/parte3_comparaciones.png)

**Gráfica de tiempo**

![Tiempo de ejecución de insertion sort](graficas/parte3_tiempo.png)

#### Análisis de los resultados

Los resultados confirmaron las predicciones iniciales. El escenario B presentó los menores tiempos y la menor cantidad de comparaciones. Por ejemplo, para 6.400 elementos se realizaron 10.277 comparaciones y el tiempo fue de 0.000578 segundos.

El escenario A presentó un comportamiento mayor que el escenario B. Para 6.400 elementos, realizó 10.276.753 comparaciones y tardó 0.506246 segundos.

El escenario C obtuvo los valores más altos. Para 6.400 elementos, realizó 20.476.800 comparaciones y tardó 0.995081 segundos. Esto demuestra que el orden inverso representa el peor caso para Insertion Sort.

Al aumentar el tamaño de los datos, el tiempo y las comparaciones también aumentaron. Por esta razón, el algoritmo puede resultar poco conveniente para procesar grandes cantidades de registros cuando existe una restricción de tiempo estricta.

