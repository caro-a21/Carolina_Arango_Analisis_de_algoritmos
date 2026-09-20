import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio


TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]


def medir_tiempo(algoritmo, datos: list[int]) -> float:
    
    inicio = time.perf_counter()
    algoritmo(datos)
    fin = time.perf_counter()

    return fin - inicio


def ejecutar_experimento() -> None:
    
    tiempos_insertion = []
    tiempos_merge = []

    print("Comparacion de algoritmos")
    print("-" * 65)

    for n in TAMANOS:
        datos = generar_aleatorio(n, semilla=42)

        tiempo_insertion = medir_tiempo(
            insertion_sort,
            datos
        )

        tiempo_merge = medir_tiempo(
            merge_sort,
            datos
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
    print("Grafica guardada en la carpeta graficas.")


def crear_grafica(
    tiempos_insertion: list[float],
    tiempos_merge: list[float]
) -> None:

    plt.figure(figsize=(10, 6))

    plt.plot(
        TAMANOS,
        tiempos_insertion,
        marker="o",
        label="Insertion Sort"
    )

    plt.plot(
        TAMANOS,
        tiempos_merge,
        marker="o",
        label="Merge Sort"
    )

    plt.title("Comparacion de tiempos de ordenamiento")
    plt.xlabel("Tamano de entrada (n)")
    plt.ylabel("Tiempo de ejecucion (segundos)")
    plt.legend()
    plt.grid(True)

    plt.savefig(
        "graficas/parte4_tiempo.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()


if __name__ == "__main__":
    ejecutar_experimento()