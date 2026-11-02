# Retroalimentación — Laboratorio 3: Estructuras de datos

**Estudiante:** Carolina Arango Escobar · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `913e136`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 18 / 20 |
| Calidad de la explicación teórica | 16 / 20 |
| Corrección de la implementación | 24 / 25 |
| Calidad del análisis de las gráficas | 24 / 25 |
| Documentación y organización del informe | 7 / 10 |
| **Total** | **89 / 100** |
| **Nota (0–5)** | **4.45** |

Buen trabajo: las estructuras funcionan y las mediciones se ven claras.

## 1. Corrección conceptual (18 / 20)
**Lo que hizo bien:**
- Explica bien qué es una colisión y compara el encadenamiento con el direccionamiento abierto, usando el ejemplo de las guías 10, 24 y 17 con m = 7.
- Justifica que la tabla hash no sirve para rangos y que el árbol sí.
- Estima la altura y las comparaciones del árbol degenerado (400.000 niveles) frente al equilibrado (unos 19 o 20).
- Recomienda tabla hash más árbol equilibrado y declara que los tiempos a 5.000.000 son estimaciones.

**Lo que puede mejorar (y cómo corregirlo):**
- La explicación de por qué hay colisiones aunque sobren casillas es muy corta ("la función puede asignar diferentes valores a una misma posición").
  → *Cómo corregirlo:* piense cuántas guías posibles hay frente a cuántas casillas, y qué le pasa a dos guías distintas con el mismo residuo.
- Para la tabla hash a 5.000.000 de envíos repite el tiempo medido sin analizar si seguirá igual (por ejemplo, con más memoria usada).
  → *Cómo corregirlo:* explique si algo del experimento podría cambiar al crecer tanto la tabla, y diga por qué mantiene o no el valor.

## 2. Calidad de la explicación teórica (16 / 20)
**Lo que hizo bien:**
- Dice que la lista cuesta Θ(n) y la tabla Θ(1 + α).
- Nombra el supuesto de distribución uniforme y explica que, si todas las guías caen en una casilla, la tabla se vuelve una lista con costo Θ(n).

**Lo que puede mejorar (y cómo corregirlo):**
- No explica por qué buscar una guía inexistente en la lista obliga a revisar todos los nodos más allá de decir que "hay que recorrerlos".
  → *Cómo corregirlo:* compare lo que ocurre cuando la guía existe (puede parar antes) con cuando no existe.

## 3. Corrección de la implementación (24 / 25)
**Lo que hizo bien:**
- `ListaEnlazada` y `TablaHash` están completas, con la búsqueda hecha con ciclo y sin usar `dict`, `set` ni `hash()` en las estructuras.
- La tabla reutiliza la lista para cada casilla.
- Las pruebas cubren búsqueda exitosa e infructuosa, la colisión forzada con m = 7 (casilla 3, longitud 3), el factor de carga 3/7 y veinte colecciones aleatorias; todas pasan.
- Tiene docstrings con `Args` y `Returns`, *type hints* y las líneas en blanco entre funciones.

**Lo que puede mejorar (y cómo corregirlo):**
- La prueba de colisión solo revisa la longitud de la casilla 3 en la tabla, pero no comprueba que las tres guías aparezcan en esa lista.
  → *Cómo corregirlo:* recorra la lista de la casilla 3 y verifique con `assert` que están las tres guías.

## 4. Calidad del análisis de las gráficas (24 / 25)
**Lo que hizo bien:**
- Las dos gráficas existen, con título, ejes rotulados y leyenda; la primera tiene seis valores de n con ambas curvas en los mismos ejes y la segunda cuatro valores de α.
- En la pregunta 2 calcula factores de crecimiento (2,54 para la lista entre 20.000 y 50.000, y 1,23 para la tabla) y los contrasta con Θ(n) y Θ(1). Los valores coinciden con la gráfica publicada.
- Usa sus propias mediciones para estimar el tiempo con 5.000.000 de envíos.

**Lo que puede mejorar (y cómo corregirlo):**
- En la segunda gráfica dice que el tiempo creció 4,1 veces cuando α pasó de 0,5 a 10, y concluye que es "coherente" con Θ(1 + α) sin hacer la comparación con lo que esa fórmula predice.
  → *Cómo corregirlo:* calcule cuánto crece 1 + α entre esos dos valores y compare ese número con el 4,1 medido, explicando la diferencia.

## 5. Documentación y organización del informe (7 / 10)
**Lo que hizo bien:**
- La carpeta del laboratorio está en un lugar válido (`laboratorios/lab3-estructuras-datos/`) con todos los archivos y las dos gráficas incrustadas con ruta relativa, que se ven bien.
- Incluye su nombre, instrucciones para reproducir, las partes en el orden pedido y tres commits descriptivos.

**Lo que puede mejorar (y cómo corregirlo):**
- Las partes prácticas no enlazan el código: al inicio de la Parte 1 faltan los enlaces a `estructuras.py` y `pruebas.py`, y al inicio de la Parte 2 falta el de `medicion.py`. Solo se nombran los archivos al final, sin enlace.
  → *Cómo corregirlo:* use la sintaxis `[estructuras.py](estructuras.py)` al comienzo de cada parte.
- En las instrucciones, instala las dependencias antes de activar el entorno virtual.
  → *Cómo corregirlo:* ponga primero la activación del entorno y después `python -m pip install -r requirements.txt`.

## ¿El código funciona?
Sí. Las pruebas corren sin errores y las dos estructuras responden igual. Los experimentos se ejecutan y generan las gráficas pedidas.
