# Laboratorio 3 — Estructuras de datos

**Estudiante:** Carolina Arango Escobar

## Cómo ejecutar el laboratorio

Para ejecutar el laboratorio, primero se debe ubicar la carpeta principal del repositorio y activar el entorno virtual.

### 1. Instalar las dependencias

Desde la carpeta principal del repositorio, ejecutar:

```bash
python -m pip install -r requirements.txt
```

### 2. Activar el entorno virtual

Según el sistema operativo, utilizar el comando correspondiente:

**Windows (CMD):**

```cmd
venv\Scripts\activate
```

**Windows (PowerShell):**

```powershell
venv\Scripts\Activate.ps1
```

**Linux o macOS:**

```bash
source venv/bin/activate
```

### 3. Ingresar a la carpeta del laboratorio

```bash
cd laboratorios/lab3-estructuras-datos
```

### 4. Ejecutar las pruebas

```bash
python pruebas.py
```

### 5. Ejecutar los experimentos de medición

```bash
python medicion.py
```

Este último archivo ejecuta los dos experimentos, muestra los tiempos de búsqueda y genera las gráficas correspondientes dentro de la carpeta `graficas`.

---

## Parte 1. Implementación y pruebas de las estructuras de datos

Para esta parte se implementaron dos estructuras de datos: una lista enlazada y una tabla hash.

### Lista enlazada

Se implementó una lista enlazada para almacenar los números de guía y sus respectivos estados. Cada nodo contiene la información de una guía, su estado y una referencia al siguiente nodo.

Las operaciones principales implementadas permiten insertar elementos y buscar una guía dentro de la lista.

### Tabla hash

Se implementó una tabla hash utilizando el método de división para calcular la posición de almacenamiento de cada elemento. Para manejar las colisiones se utilizó encadenamiento, es decir, cada posición de la tabla puede almacenar una lista enlazada.

El factor de carga se calcula dividiendo la cantidad de elementos almacenados entre el tamaño de la tabla:

\[
\alpha = \frac{n}{m}
\]

Donde:

- \(n\): cantidad de elementos almacenados.
- \(m\): tamaño de la tabla.
- \(\alpha\): factor de carga.

### Pruebas realizadas

Se realizaron pruebas para verificar el funcionamiento de las dos estructuras:

- Inserción de elementos en la lista enlazada y en la tabla hash.
- Búsqueda de guías existentes.
- Búsqueda de guías que no se encuentran almacenadas.
- Comparación de los resultados de búsqueda entre las dos estructuras.
- Verificación del manejo de colisiones en la tabla hash.

Para comprobar el manejo de colisiones se insertaron las guías 10, 24 y 17 en una tabla de tamaño 7. Las tres guías quedaron ubicadas en la posición 3, por lo que se comprobó que el encadenamiento permite almacenar varios elementos en una misma posición.

En este caso, la longitud de la cadena fue de 3 y el factor de carga fue:

\[
\alpha = \frac{3}{7} \approx 0.4286
\]

También se realizaron pruebas con 20 colecciones aleatorias, verificando búsquedas exitosas y no exitosas.

---

## Parte 2. Medición y análisis del rendimiento

Para esta parte se realizaron experimentos con el objetivo de comparar el tiempo de búsqueda de una lista enlazada y una tabla hash, y observar cómo influye el factor de carga en el rendimiento de la tabla hash.

Las mediciones se realizaron utilizando `time.perf_counter()`, tomando el tiempo de las búsquedas y calculando el promedio por consulta. Cada medición se repitió tres veces.

### Experimento A. Lista enlazada frente a tabla hash

En este experimento se comparó el tiempo promedio de búsqueda de las dos estructuras utilizando diferentes cantidades de elementos.

Se utilizaron los tamaños:

`[100, 500, 1000, 5000, 20000, 50000]`

Para cada tamaño se generó la misma colección de guías para ambas estructuras. Además, se realizaron 200 búsquedas de guías inexistentes, lo que permitió comparar el comportamiento de las estructuras cuando deben determinar que un elemento no está almacenado.

El tamaño de la tabla hash se calculó utilizando un valor primo cercano a la mitad de la cantidad de elementos.

**Resultados obtenidos:**

| n | m | Factor de carga (α) | Lista (s/búsqueda) | Tabla hash (s/búsqueda) |
|---:|---:|---:|---:|---:|
| 100 | 53 | 1.8868 | 1.88567e-06 | 1.17667e-07 |
| 500 | 251 | 1.9920 | 9.76233e-06 | 1.85833e-07 |
| 1.000 | 503 | 1.9881 | 1.90572e-05 | 1.49333e-07 |
| 5.000 | 2.503 | 1.9976 | 9.36710e-05 | 1.79000e-07 |
| 20.000 | 10.007 | 1.9986 | 3.82069e-04 | 2.10167e-07 |
| 50.000 | 25.013 | 1.9990 | 9.68655e-04 | 2.59500e-07 |

**Gráfica del experimento A:**

![Comparación del tiempo de búsqueda de la lista enlazada y la tabla hash](graficas/lista_vs_tabla.png)

**Análisis de resultados:**

Los resultados muestran que el tiempo de búsqueda de la lista enlazada aumenta a medida que crece la cantidad de elementos. Esto ocurre porque, para encontrar una guía o comprobar que no existe, es necesario recorrer los nodos de la lista.

Por otro lado, la tabla hash presenta tiempos de búsqueda mucho menores y con variaciones pequeñas a medida que aumenta la cantidad de elementos. Esto se debe a que utiliza una función hash para ubicar los elementos en una posición de la tabla.

Por ejemplo, cuando se trabaja con 50.000 elementos, la búsqueda en la lista enlazada tarda aproximadamente 0.00096865 segundos por consulta, mientras que en la tabla hash tarda aproximadamente 0.0000002595 segundos.

Esto permite observar que la tabla hash presenta un mejor rendimiento en las búsquedas realizadas en este experimento, especialmente cuando aumenta la cantidad de elementos almacenados.

### Experimento B. Efecto del factor de carga

En este experimento se analizó cómo cambia el tiempo de búsqueda de una tabla hash cuando se modifica su factor de carga.

Se mantuvo fija la cantidad de elementos en 20.000 y se probaron cuatro factores de carga deseados: 0.5, 1, 4 y 10.

Para conseguir estos valores se modificó el tamaño de la tabla, manteniendo la misma colección de guías. También se realizaron 200 búsquedas de guías inexistentes para cada configuración.

**Resultados obtenidos:**

| Factor de carga deseado | m | Factor de carga real | Tiempo (s/búsqueda) |
|---:|---:|---:|---:|
| 0.50 | 40.009 | 0.499888 | 1.11167e-07 |
| 1.00 | 20.011 | 0.999450 | 1.51667e-07 |
| 4.00 | 5.003 | 3.997601 | 2.41000e-07 |
| 10.00 | 2.003 | 9.985022 | 4.56333e-07 |

**Gráfica del experimento B:**

![Efecto del factor de carga en el tiempo de búsqueda de la tabla hash](graficas/tiempo_vs_alfa.png)

**Análisis de resultados:**

Los resultados muestran que, a medida que aumenta el factor de carga, también aumenta el tiempo promedio de búsqueda.

Cuando el factor de carga es cercano a 0.5, el tiempo de búsqueda es aproximadamente 1.11167e-07 segundos por consulta. En cambio, cuando el factor de carga aumenta a aproximadamente 10, el tiempo llega a 4.56333e-07 segundos.

Esto ocurre porque, al aumentar el factor de carga, hay más elementos almacenados en relación con la cantidad de posiciones disponibles en la tabla. Como consecuencia, se presentan más colisiones y las listas de encadenamiento pueden tener más elementos que recorrer durante una búsqueda.

Por lo tanto, en este experimento se observa que un factor de carga menor favorece el rendimiento de las búsquedas, mientras que un factor de carga mayor puede aumentar el tiempo necesario para encontrar un elemento o comprobar que no existe.

---


