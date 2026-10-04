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
