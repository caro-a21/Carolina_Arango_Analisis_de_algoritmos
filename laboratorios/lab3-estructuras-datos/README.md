# Laboratorio 3 — Estructuras de datos

**Nombre:** Carolina Arango Escobar

## Cómo ejecutar el laboratorio

Para ejecutar el laboratorio se necesita tener Python instalado y utilizar el entorno virtual del repositorio.

Primero, desde la carpeta principal del repositorio, se debe activar el entorno virtual.

**En Windows (CMD):**

```cmd
venv\Scripts\activate
```

**En Windows (PowerShell):**

```powershell
venv\Scripts\Activate.ps1
```

**En Linux o macOS:**

```bash
source venv/bin/activate
```

Después, se debe ingresar a la carpeta del laboratorio:

```bash
cd laboratorios/lab3-estructuras-datos
```

Para ejecutar las pruebas de la primera parte, se utiliza el siguiente comando:

```bash
python pruebas.py
```

Para ejecutar los experimentos y generar las gráficas, se utilizará:

```bash
python medicion.py
```

Si se necesita instalar las dependencias del proyecto, se puede ejecutar desde la carpeta principal:

```bash
python -m pip install -r requirements.txt
```

## Parte 1 — Implementación y verificación de las estructuras

**Archivos de esta parte:** [estructuras.py](estructuras.py) y [pruebas.py](pruebas.py).

En esta primera parte se implementaron una lista enlazada y una tabla hash para almacenar y consultar los números de guía de los envíos.

La lista enlazada permite agregar nuevas guías al inicio y buscarlas recorriendo sus nodos. Por otro lado, la tabla hash utiliza el método de división para calcular la posición de cada guía y utiliza listas enlazadas para guardar los elementos que llegan a una misma casilla.

Para verificar que las dos estructuras funcionaran correctamente, se realizaron pruebas de búsqueda de guías existentes y de guías que no están almacenadas. También se comprobó el manejo de colisiones utilizando las guías 10, 24 y 17 con una tabla de 7 casillas, ya que las tres llegan a la posición 3.

Además, se verificó que la lista de esa casilla tuviera tres elementos y que el factor de carga fuera igual a 3/7.

Finalmente, se realizaron pruebas con 20 colecciones aleatorias. En ellas se compararon los resultados de las dos estructuras para guías existentes y no existentes, comprobando que ambas devolvieran la misma respuesta.

