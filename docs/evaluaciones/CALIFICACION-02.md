# Retroalimentación — Laboratorio evaluativo 02: Dividir y vencer

**Estudiante:** Carolina Arango Escobar · **Laboratorio:** Dividir y vencer (subarreglo máximo)
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `f7819e4`

Muy buen trabajo: el código es correcto y el informe se apoya en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 18 / 20 |
| Calidad de la explicación teórica | 15 / 20 |
| Corrección de la implementación | 24 / 25 |
| Calidad del análisis de las gráficas | 21 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **88 / 100** |
| **Nota (0–5)** | **4.40** |

## 1. Corrección conceptual (18 / 20)
**Lo que hizo bien:**
- Identifica que divide y vencerás empieza a ganar desde n = 100 y explica por qué en tamaños pequeños no pasa (costo de las llamadas recursivas).
- Compara con el máximo de un arreglo: plantea `T(n) = 2T(n/2) + Θ(1)`, llega a `Θ(n)` y concluye que dividir no mejora nada.
- Recomienda divide y vencerás, estima 1.000.000 de registros (unas 3,7 horas contra 1,5 segundos), lo declara como estimación y no usa una regla de tres lineal.

**Lo que puede mejorar:**
- En la pregunta 4 faltó decir que, aunque el orden es el mismo, dividir agrega trabajo extra (más llamadas) y por eso recorrer una vez es mejor en la práctica.
- La estimación sería más sólida si mencionara que a un millón de datos la recursión puede costar más de lo que predice la fórmula.

## 2. Calidad de la explicación teórica (15 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)` y explica que el caso cruzado cuesta `Θ(n)`.
- Aplica el método maestro con `a = 2`, `b = 2` y compara `f(n)` con `n^(log₂ 2) = n` para justificar el caso 2.

**Lo que puede mejorar:**
- Explique de dónde sale cada término: por qué son 2 subproblemas y por qué cada uno es de tamaño n/2.
- Para la fuerza bruta solo dice que "los dos ciclos revisan todos los tramos". Falta contar cuántos pares hay (alrededor de n²/2) para justificar `Θ(n²)`.

## 3. Corrección de la implementación (24 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos (ocho días, un elemento, todos negativos, todos positivos, caso cruzado) y en las 20 listas aleatorias.
- `subarreglo_maximo` resuelve los tres casos sin llamar a la fuerza bruta, y ninguna función modifica la lista recibida.
- Tiene tipos y explicaciones (docstrings) en cada función, y el código sigue el estilo PEP 8.

**Lo que puede mejorar:**
- Si dos tramos empatan, la comparación de casos es un poco larga; podría simplificarse con una sola comparación de tres valores.

## 4. Calidad del análisis de las gráficas (21 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda y ambas curvas en los mismos ejes, con 7 tamaños (de 10 a 4000).
- Calcula el factor al duplicar n (≈4,1 para fuerza bruta y 2 a 2,2 para divide y vencerás) y lo contrasta con `Θ(n²)` y `Θ(n log n)`.
- Incluye una tabla con los valores medidos y repite cada medición tres veces.

**Lo que puede mejorar:**
- Las afirmaciones se apoyan en la tabla, pero casi no se lee nada de la gráfica. Conviene citar también valores que se vean en ella.
- Calculó el factor solo en tamaños pequeños. Habría sido útil ver también de 2000 a 4000 o de 1000 a 4000 para confirmar la tendencia.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Carpeta `laboratorios/lab2-divide-y-vencer/` con todos los archivos pedidos y la gráfica visible en el README.
- Cada parte enlaza su código, hay instrucciones claras para reproducir y varios commits descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan, ambos algoritmos coinciden en cientos de listas aleatorias, y `medicion.py` corre bien y genera la gráfica.

## Para el próximo laboratorio
- Explique de dónde sale cada término de la recurrencia (cuántos subproblemas y de qué tamaño).
- Justifique los `Θ(n²)` contando cuántas veces se ejecuta el ciclo interno.
- Lea valores concretos de la gráfica y cítelos junto a los de la tabla.
- Calcule factores de crecimiento también en tamaños grandes.
