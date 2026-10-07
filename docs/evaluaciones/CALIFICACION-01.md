# Retroalimentación — Laboratorio 1: Fundamentos, complejidad y recurrencias

**Estudiante:** Carolina Arango Escobar · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-07 23:59 · **Versión revisada:** commit `ed3cbcc`

Muy buen trabajo, el informe es claro y las mediciones respaldan sus conclusiones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 21 / 25 |
| Calidad de la explicación teórica | 20 / 25 |
| Corrección de la implementación | 19 / 20 |
| Calidad del análisis de las gráficas | 18 / 20 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **87 / 100** |
| **Nota (0–5)** | **4.35** |

## 1. Corrección conceptual (21 / 25)
**Lo que hizo bien:**
- Distingue entre resultado correcto y resultado a tiempo, y nombra la restricción que Tamiza incumple: terminar los 1.200.000 registros entre las 2:00 y las 6:00 a. m.
- Explica que un servidor más rápido no cambia cómo crece el trabajo del algoritmo.
- El ejemplo propio (tienda en línea en Black Friday) trae cantidad de datos y límite de tiempo.
- Relaciona el tiempo de ejecución con el consumo de energía y su acumulación noche tras noche.
- Da dos perjuicios concretos (el paciente de riesgo alto sin llamar a tiempo y el operador con una lista incompleta) e indica quién asume el costo.
- Reconoce que el orden de la lista decide a quién se llama primero.

**Lo que puede mejorar:**
- Parte 1: explique con más detalle por qué el servidor doble no basta (por ejemplo, qué pasa con el tiempo si los registros siguen creciendo).
- Parte 2: el costo de cada perjuicio queda repartido de forma general; diga con claridad quién lo asume en cada caso.
- Parte 2.3: desarrolle la obligación adicional (verificar que el orden sea correcto, no solo rápido).

## 2. Calidad de la explicación teórica (20 / 25)
**Lo que hizo bien:**
- Define los tres casos, dice sobre qué se toma el máximo, el mínimo y el promedio, justifica que usaría el peor caso por la ventana estricta y deja la predicción antes de medir.
- Explica cada término de `T(n) = 2T(n/2) + Θ(n)`.
- Resuelve con el método maestro: identifica `a = 2`, `b = 2`, `f(n) = Θ(n)`, verifica el caso 2 y concluye `Θ(n log n)`.
- La tabla de complejidades es correcta.

**Lo que puede mejorar:**
- El cálculo de insertion sort no es línea a línea: falta indicar cuántas veces se ejecuta cada línea del código y sumar esos costos.
- El caso promedio de insertion sort se afirma sin justificarlo (por ejemplo, que en promedio cada elemento se desplaza la mitad del camino).
- En 3.1 el caso promedio queda definido de forma muy general.

## 3. Corrección de la implementación (19 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien de mayor a menor los tres escenarios, no cambian la lista recibida y cuentan solo comparaciones entre elementos. No usan `sorted()` ni `list.sort()`, y la mezcla de `merge_sort` es propia y recursiva.
- Los generadores dan listas de tamaño `n` con valores distintos y semilla reproducible.
- Todas las funciones tienen tipos y docstrings estilo Google, y el formato es limpio.

**Lo que puede mejorar:**
- En `generar_casi_ordenado`, el 2 % final son los valores más bajos de la lista, así que el caso es algo más favorable que un lote real con valores mezclados.
- Los docstrings de `algoritmos.py` y `datos.py` difieren un poco de los pedidos en el enunciado.

## 4. Calidad del análisis de las gráficas (18 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes rotulados y leyenda, y se ven en el informe.
- Identifica con cifras que C es el peor caso, B el mejor y A se acerca al promedio, y lo contrasta con su predicción.
- Concluye que merge sort es mejor describiendo cada curva y lo conecta con `O(n²)` y `O(n log n)`; explica por qué en tamaños pequeños están cerca.
- Extrapola a 1.200.000 registros con su razonamiento (factor de tamaño al cuadrado y `n log n`) y declara que es una estimación: unas 4,71 horas para insertion sort contra unos 2 segundos para merge sort.
- Responde a la compra del servidor con el dato de n = 6400 y recomienda merge sort pensando en que el canal puede cambiar; menciona la memoria extra.

**Lo que puede mejorar:**
- Las gráficas de la Parte 3 usan una escala en la que el escenario B queda pegado a cero; una escala logarítmica mostraría mejor las diferencias.
- Discuta más consideraciones además de la memoria (estabilidad, mantenimiento, riesgo de que B deje de ser casi ordenado).
- Aclare si repitió las mediciones o si usó una sola corrida.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- La carpeta del laboratorio está en una ubicación válida, con todos los archivos y gráficas pedidos.
- El informe sigue el orden de las partes, enlaza el código de cada parte práctica y tiene las gráficas incrustadas con rutas que funcionan.
- Incluye instrucciones de reproducción para varios sistemas y 8 commits descriptivos.

**Lo que puede mejorar:**
- Las instrucciones parten de una carpeta llamada `curso-analisis-algoritmos`, que puede no coincidir con el nombre real de su repositorio.
- La carpeta `graficas/` y los scripts están bien, pero el informe se divide en secciones extra (4.4, 4.5) en lugar de un único concepto técnico dirigido a la Secretaría.

## ¿El código funciona?
Sí. Los dos algoritmos ordenan bien, los dos scripts corren sin errores y generan las gráficas.

## Para el próximo laboratorio
- Desarrolle el cálculo línea a línea indicando cuántas veces se ejecuta cada línea y sumando.
- Justifique el caso promedio con un argumento y no solo con la afirmación.
- Profundice las consideraciones distintas del tiempo (estabilidad, mantenimiento, riesgos del flujo de datos).
- Repita cada medición varias veces y reporte el promedio o la mediana.
- Use una escala logarítmica cuando una curva quede pegada al eje.
