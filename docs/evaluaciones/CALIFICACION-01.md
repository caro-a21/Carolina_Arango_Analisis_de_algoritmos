# Retroalimentación — Laboratorio 1: Fundamentos, complejidad y recurrencias

**Estudiante:** Carolina Arango Escobar · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-06 23:59 · **Versión revisada:** commit `362d6c5`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 9 / 25 |
| Calidad de la explicación teórica | 12 / 25 |
| Corrección de la implementación | 13 / 20 |
| Calidad del análisis de las gráficas | 14 / 20 |
| Documentación y organización del informe | 8 / 10 |
| **Total** | **56 / 100** |
| **Nota (0–5)** | **2.80** |

## 1. Corrección conceptual (9 / 25)
**Lo que hizo bien:**
- Distingue entre un algoritmo que da el resultado correcto y uno que además lo da a tiempo, y menciona las 4 horas.
- Plantea un segundo ejemplo propio (Black Friday) y explica que comprar un computador más rápido no cambia cómo crece el trabajo.
- Relaciona el tiempo de ejecución con el gasto de energía.

**Lo que puede mejorar:**
- Parte 1: el ejemplo del Black Friday no dice cuántos datos hay ni qué límite se incumple. No se nombra claramente la restricción que Tamiza incumple (terminar antes de las 6:00 a. m. con 1.200.000 registros).
- Parte 2: falta explicar por qué el consumo se multiplica al correr todas las madrugadas durante años.
- Parte 2: faltan al menos dos perjuicios concretos para una persona (por ejemplo, un paciente de alto riesgo al que no se llama a tiempo) y quién asume el costo de cada uno.
- Parte 2: no se discute que el orden de la lista decide a quién se llama primero y qué obligación trae eso.

## 2. Calidad de la explicación teórica (12 / 25)
**Lo que hizo bien:**
- La Parte 3.1 define los tres casos, indica sobre qué se toma cada uno, justifica que usaría el peor caso por la ventana estricta y deja escrita la predicción antes de medir.
- La tabla de complejidades es correcta.

**Lo que puede mejorar:**
- Parte 4.1: la recurrencia de merge sort se escribe, pero no se explica de dónde sale cada término (dos subproblemas, mitad del tamaño, costo de mezclar).
- Se dice "al aplicar el método maestro" sin mostrar `a`, `b`, `f(n)` ni verificar la condición del caso. Falta el desarrollo paso a paso.
- Falta el cálculo de insertion sort línea a línea (cuántas veces se ejecuta cada línea y la suma).
- En 3.1 la definición del caso promedio es muy general.

## 3. Corrección de la implementación (13 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien (de mayor a menor) los tres escenarios, no cambian la lista original y cuentan comparaciones entre elementos. No usan `sorted()` ni `list.sort()`.
- Los generadores producen listas de tamaño `n` con valores distintos, y el escenario B queda con el 2 % desordenado al final.

**Lo que puede mejorar:**
- Casi ninguna función de `algoritmos.py`, `datos.py` ni de los scripts tiene su explicación (docstring estilo Google).
- Algunas funciones auxiliares no tienen todos los tipos indicados.
- Hay pequeños detalles de formato PEP 8: espacios en líneas vacías, falta de línea en blanco entre funciones y final de archivo sin salto de línea.

## 4. Calidad del análisis de las gráficas (14 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, tienen título, ejes con unidad y leyenda, y se ven en el informe.
- Identifica con cifras que C es el peor caso, B el mejor y A se acerca al promedio, y lo contrasta con su predicción.
- En 4.2 concluye que merge sort es mejor, describe cómo crece cada curva y lo conecta con `O(n²)` y `O(n log n)`.
- En 4.3 recomienda merge sort, da una estimación (declarada como tal) y menciona la memoria extra.

**Lo que puede mejorar:**
- No explica cómo hizo la extrapolación a 1.200.000 registros; solo da el resultado.
- La respuesta a la compra del servidor no cita la gráfica ni el tamaño del que tomó el dato.
- Falta decir por qué en tamaños pequeños las dos curvas casi coinciden.
- No pidió una sola recomendación pensando en que el canal de entrada puede cambiar (si el lote llega casi ordenado, insertion sort sería rápido).

## 5. Documentación y organización del informe (8 / 10)
**Lo que hizo bien:**
- La carpeta del laboratorio está en una ubicación válida, con todos los archivos y gráficas pedidos.
- El informe está dividido por partes, enlaza el código y muestra las gráficas.
- Tiene varios commits con mensajes descriptivos.

**Lo que puede mejorar:**
- Las instrucciones de reproducción usan la ruta `lab1-fundamentos-complejidad-recurrencias/...`, pero la carpeta está dentro de `laboratorios/`, así que los comandos no funcionan tal como están escritos. Además, solo sirven en Windows.

## ¿El código funciona?
Sí. Los dos algoritmos ordenan correctamente, los scripts corren sin errores y generan las gráficas.

## Para el próximo laboratorio
- Responda cada punto que pide el enunciado, uno por uno (por ejemplo, los perjuicios a personas y quién asume el costo).
- Muestre el desarrollo completo de las recurrencias y del cálculo línea a línea, no solo el resultado.
- Explique cómo hace sus extrapolaciones y cite la gráfica y el tamaño que usa como dato.
- Agregue docstrings y tipos a todas las funciones y revise el formato PEP 8.
- Revise que los comandos del informe funcionen desde la ruta real de la carpeta.
