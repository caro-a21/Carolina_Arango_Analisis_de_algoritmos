"""Medicion de tiempos para los algoritmos de subarreglo maximo."""

import random
import statistics
import time

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


TAMANOS = [10, 50, 100, 200, 400, 1000, 4000]
REPETICIONES = 3
SEMILLA = 42


def generar_datos(tamano: int, generador: random.Random) -> list[int]:
    
    return [
        generador.randint(-100, 100)
        for _ in range(tamano)
    ]


def medir_fuerza_bruta(valores: list[int]) -> float:
    
    inicio = time.perf_counter()
    subarreglo_fuerza_bruta(valores)
    fin = time.perf_counter()

    return fin - inicio


def medir_divide_y_venceras(valores: list[int]) -> float:
   
    inicio = time.perf_counter()
    subarreglo_maximo(valores, 0, len(valores) - 1)
    fin = time.perf_counter()

    return fin - inicio


def realizar_mediciones() -> tuple[list[int], list[float], list[float]]:
    
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
            f"Divide y venceras: {mediana_divide:.6f} s"
        )

    return TAMANOS, tiempos_fuerza, tiempos_divide


def crear_grafica(
    tamanos: list[int],
    tiempos_fuerza: list[float],
    tiempos_divide: list[float],
) -> None:
   
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
    print("Grafica guardada en graficas/tiempo_vs_n.png")