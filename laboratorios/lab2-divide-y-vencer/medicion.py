"""Medición de tiempos para los algoritmos de subarreglo máximo."""

import random
import statistics
import time

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


TAMANOS = [10, 50, 100, 200, 400, 1000, 4000]
REPETICIONES = 3
SEMILLA = 42


def generar_datos(tamano: int, generador: random.Random) -> list[int]:
    """Genera una lista de valores enteros aleatorios.

    Los valores generados están entre -100 y 100.

    Args:
        tamano: Cantidad de valores que tendrá la lista.
        generador: Generador de números aleatorios utilizado.

    Returns:
        Una lista de enteros aleatorios.
    """
    return [
        generador.randint(-100, 100)
        for _ in range(tamano)
    ]


def medir_fuerza_bruta(valores: list[int]) -> float:
    """Mide el tiempo de ejecución de fuerza bruta.

    Args:
        valores: Lista de valores que recibe el algoritmo.

    Returns:
        Tiempo de ejecución en segundos.
    """
    inicio = time.perf_counter()
    subarreglo_fuerza_bruta(valores)
    fin = time.perf_counter()

    return fin - inicio


def medir_divide_y_venceras(valores: list[int]) -> float:
    """Mide el tiempo de ejecución de divide y vencerás.

    Args:
        valores: Lista de valores que recibe el algoritmo.

    Returns:
        Tiempo de ejecución en segundos.
    """
    inicio = time.perf_counter()
    subarreglo_maximo(valores, 0, len(valores) - 1)
    fin = time.perf_counter()

    return fin - inicio


def realizar_mediciones() -> tuple[list[int], list[float], list[float]]:
    """Realiza las mediciones de tiempo para ambos algoritmos.

    Genera los mismos datos para los dos algoritmos y utiliza la
    mediana de varias repeticiones para obtener el tiempo de cada
    tamaño de entrada.

    Returns:
        Una tupla con los tamaños utilizados, los tiempos de fuerza
        bruta y los tiempos de divide y vencerás.
    """
    generador = random.Random(SEMILLA)

    tiempos_fuerza = []
    tiempos_divide = []

    for tamano in TAMANOS:
        valores = generar_datos(tamano, generador)

        resultado_fuerza = subarreglo_fuerza_bruta(valores)
        resultado_divide = subarreglo_maximo(
            valores,
            0,
            len(valores) - 1,
        )

        assert resultado_fuerza[2] == resultado_divide[2]

        mediciones_fuerza = []
        mediciones_divide = []

        for _ in range(REPETICIONES):
            tiempo_fuerza = medir_fuerza_bruta(valores)
            mediciones_fuerza.append(tiempo_fuerza)

            tiempo_divide = medir_divide_y_venceras(valores)
            mediciones_divide.append(tiempo_divide)

        mediana_fuerza = statistics.median(mediciones_fuerza)
        mediana_divide = statistics.median(mediciones_divide)

        tiempos_fuerza.append(mediana_fuerza)
        tiempos_divide.append(mediana_divide)

        print(
            f"n={tamano:4d} | "
            f"Fuerza bruta: {mediana_fuerza:.6f} s | "
            f"Divide y vencerás: {mediana_divide:.6f} s"
        )

    return TAMANOS, tiempos_fuerza, tiempos_divide


def crear_grafica(
    tamanos: list[int],
    tiempos_fuerza: list[float],
    tiempos_divide: list[float],
) -> None:
    """Crea y guarda la gráfica de los tiempos de ejecución.

    Args:
        tamanos: Tamaños de entrada utilizados en las mediciones.
        tiempos_fuerza: Tiempos obtenidos con fuerza bruta.
        tiempos_divide: Tiempos obtenidos con divide y vencerás.
    """
    plt.figure()

    plt.plot(
        tamanos,
        tiempos_fuerza,
        marker="o",
        label="Fuerza bruta",
    )

    plt.plot(
        tamanos,
        tiempos_divide,
        marker="o",
        label="Divide y vencerás",
    )

    plt.title("Tiempo de ejecución de los algoritmos")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)

    plt.savefig("graficas/tiempo_vs_n.png", dpi=150)
    plt.close()


if __name__ == "__main__":
    tamanos, tiempos_fuerza, tiempos_divide = realizar_mediciones()

    crear_grafica(
        tamanos,
        tiempos_fuerza,
        tiempos_divide,
    )

    print()
    print("Experimento terminado.")
    print("Gráfica guardada en graficas/tiempo_vs_n.png")