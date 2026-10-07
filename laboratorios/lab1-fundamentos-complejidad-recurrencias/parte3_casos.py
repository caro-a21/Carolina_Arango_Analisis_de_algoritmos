"""Experimento de casos de Insertion Sort."""

import os
import time
from collections.abc import Callable

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import (
    generar_aleatorio,
    generar_casi_ordenado,
    generar_inverso,
)


TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]


def medir_escenario(
    generador: Callable[[int], list[int]],
    n: int,
) -> tuple[float, int]:
    """Mide el tiempo y las comparaciones de un escenario.

    Genera los datos utilizando el generador recibido y mide únicamente
    el tiempo que tarda Insertion Sort en ordenar la lista.

    Args:
        generador: Función que genera una lista de datos de tamaño n.
        n: Tamaño de la lista que se desea generar.

    Returns:
        Una tupla con el tiempo de ejecución en segundos y el número
        de comparaciones entre elementos.
    """
    datos = generador(n)

    inicio = time.perf_counter()
    _, comparaciones = insertion_sort(datos)
    fin = time.perf_counter()

    tiempo = fin - inicio

    return tiempo, comparaciones


def ejecutar_experimento() -> dict:
    """Ejecuta las pruebas para los tres escenarios.

    Se prueban los escenarios aleatorio, casi ordenado e inverso
    utilizando todos los tamaños definidos en TAMANOS.

    Returns:
        Un diccionario con los tiempos y las comparaciones obtenidas
        para cada escenario.
    """
    resultados = {
        "A - Aleatorio": {
            "tiempos": [],
            "comparaciones": [],
        },
        "B - Casi ordenado": {
            "tiempos": [],
            "comparaciones": [],
        },
        "C - Inverso": {
            "tiempos": [],
            "comparaciones": [],
        },
    }

    generadores = {
        "A - Aleatorio": generar_aleatorio,
        "B - Casi ordenado": generar_casi_ordenado,
        "C - Inverso": generar_inverso,
    }

    for nombre, generador in generadores.items():
        for n in TAMANOS:
            tiempo, comparaciones = medir_escenario(
                generador,
                n,
            )

            resultados[nombre]["tiempos"].append(tiempo)
            resultados[nombre]["comparaciones"].append(
                comparaciones
            )

            print(
                f"{nombre} | n={n} | "
                f"tiempo={tiempo:.6f} s | "
                f"comparaciones={comparaciones}"
            )

    return resultados


def graficar_comparaciones(resultados: dict) -> None:
    """Genera la gráfica de comparaciones.

    Crea una gráfica con el número de comparaciones realizadas por
    Insertion Sort en cada uno de los tres escenarios.

    Args:
        resultados: Diccionario con los resultados del experimento.
    """
    os.makedirs("graficas", exist_ok=True)

    plt.figure()

    for nombre, datos in resultados.items():
        plt.plot(
            TAMANOS,
            datos["comparaciones"],
            marker="o",
            label=nombre,
        )

    plt.title("Comparaciones de Insertion Sort")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Número de comparaciones")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(
        "graficas/parte3_comparaciones.png",
        dpi=300,
    )

    plt.close()


def graficar_tiempos(resultados: dict) -> None:
    """Genera la gráfica de tiempos de ejecución.

    Crea una gráfica con el tiempo de ejecución de Insertion Sort
    para cada uno de los tres escenarios.

    Args:
        resultados: Diccionario con los resultados del experimento.
    """
    os.makedirs("graficas", exist_ok=True)

    plt.figure()

    for nombre, datos in resultados.items():
        plt.plot(
            TAMANOS,
            datos["tiempos"],
            marker="o",
            label=nombre,
        )

    plt.title("Tiempo de ejecución de Insertion Sort")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(
        "graficas/parte3_tiempo.png",
        dpi=300,
    )

    plt.close()


def main() -> None:
    """Ejecuta el experimento y genera las gráficas."""
    resultados = ejecutar_experimento()

    graficar_comparaciones(resultados)
    graficar_tiempos(resultados)

    print("\nExperimento terminado.")
    print("Gráficas guardadas en la carpeta graficas.")


if __name__ == "__main__":
    main()