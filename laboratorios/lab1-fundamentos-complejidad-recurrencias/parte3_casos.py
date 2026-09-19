import os
import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import (
    generar_aleatorio,
    generar_casi_ordenado,
    generar_inverso,
)


TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]


def medir_escenario(generador, n: int) -> tuple[float, int]:
    
    datos = generador(n)

    inicio = time.perf_counter()
    _, comparaciones = insertion_sort(datos)
    fin = time.perf_counter()

    tiempo = fin - inicio

    return tiempo, comparaciones


def ejecutar_experimento() -> dict:
    
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
    """Genera la grafica de comparaciones."""
    os.makedirs("graficas", exist_ok=True)

    plt.figure()

    for nombre, datos in resultados.items():
        plt.plot(
            TAMANOS,
            datos["comparaciones"],
            marker="o",
            label=nombre,
        )

    plt.title("Comparaciones de insertion sort")
    plt.xlabel("Tamano de entrada (n)")
    plt.ylabel("Numero de comparaciones")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(
        "graficas/parte3_comparaciones.png",
        dpi=300,
    )

    plt.close()


def graficar_tiempos(resultados: dict) -> None:
    """Genera la grafica de tiempos."""
    os.makedirs("graficas", exist_ok=True)

    plt.figure()

    for nombre, datos in resultados.items():
        plt.plot(
            TAMANOS,
            datos["tiempos"],
            marker="o",
            label=nombre,
        )

    plt.title("Tiempo de ejecucion de insertion sort")
    plt.xlabel("Tamano de entrada (n)")
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
    """Ejecuta el experimento y genera las graficas."""
    resultados = ejecutar_experimento()

    graficar_comparaciones(resultados)
    graficar_tiempos(resultados)

    print("\nExperimento terminado.")
    print("Graficas guardadas en la carpeta graficas.")


if __name__ == "__main__":
    main()