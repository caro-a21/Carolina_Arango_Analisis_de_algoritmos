"""Experimento de comparación entre Insertion Sort y Merge Sort."""

import time
from collections.abc import Callable

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio


TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]


def medir_tiempo(
    algoritmo: Callable[[list[int]], tuple[list[int], int]],
    datos: list[int],
) -> float:
    """Mide el tiempo de ejecución de un algoritmo de ordenamiento.

    El tiempo medido corresponde únicamente a la ejecución del
    algoritmo sobre los datos recibidos.

    Args:
        algoritmo: Función de ordenamiento que recibe una lista de
            enteros y devuelve la lista ordenada junto con el número
            de comparaciones.
        datos: Lista de enteros que se utilizará como entrada.

    Returns:
        Tiempo de ejecución del algoritmo en segundos.
    """
    inicio = time.perf_counter()
    algoritmo(datos)
    fin = time.perf_counter()

    return fin - inicio


def ejecutar_experimento() -> None:
    """Ejecuta la comparación de tiempos entre los dos algoritmos.

    Prueba Insertion Sort y Merge Sort con diferentes tamaños de
    entrada utilizando datos aleatorios y genera una gráfica con
    los tiempos obtenidos.
    """
    tiempos_insertion = []
    tiempos_merge = []

    print("Comparación de algoritmos")
    print("-" * 65)

    for n in TAMANOS:
        datos = generar_aleatorio(n, semilla=42)

        tiempo_insertion = medir_tiempo(
            insertion_sort,
            datos,
        )

        tiempo_merge = medir_tiempo(
            merge_sort,
            datos,
        )

        tiempos_insertion.append(tiempo_insertion)
        tiempos_merge.append(tiempo_merge)

        print(
            f"n={n} | "
            f"insertion sort={tiempo_insertion:.6f} s | "
            f"merge sort={tiempo_merge:.6f} s"
        )

    crear_grafica(tiempos_insertion, tiempos_merge)

    print()
    print("Experimento terminado.")
    print("Gráfica guardada en la carpeta graficas.")


def crear_grafica(
    tiempos_insertion: list[float],
    tiempos_merge: list[float],
) -> None:
    """Genera y guarda la gráfica de comparación de tiempos.

    Args:
        tiempos_insertion: Tiempos obtenidos por Insertion Sort
            para cada tamaño de entrada.
        tiempos_merge: Tiempos obtenidos por Merge Sort para cada
            tamaño de entrada.
    """
    plt.figure(figsize=(10, 6))

    plt.plot(
        TAMANOS,
        tiempos_insertion,
        marker="o",
        label="Insertion Sort",
    )

    plt.plot(
        TAMANOS,
        tiempos_merge,
        marker="o",
        label="Merge Sort",
    )

    plt.title("Comparación de tiempos de ordenamiento")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)

    plt.savefig(
        "graficas/parte4_tiempo.png",
        dpi=300,
        bbox_inches="tight",
    )

    plt.close()


if __name__ == "__main__":
    ejecutar_experimento()