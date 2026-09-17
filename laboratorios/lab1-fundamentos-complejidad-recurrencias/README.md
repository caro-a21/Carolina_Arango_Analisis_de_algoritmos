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

