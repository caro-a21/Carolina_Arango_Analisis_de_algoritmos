"""Generadores de datos para las pruebas de los algoritmos."""


import random


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera una lista de números enteros en orden aleatorio.

    La lista contiene números entre 1 y n sin repetir. Se utiliza
    una semilla para que los resultados sean reproducibles.

    Args:
        n: Cantidad de elementos que tendrá la lista.
        semilla: Semilla utilizada para generar el orden aleatorio.

    Returns:
        Una lista de n números enteros en orden aleatorio.
    """
    generador = random.Random(semilla)
    datos = list(range(1, n + 1))
    generador.shuffle(datos)

    return datos


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera una lista con aproximadamente un 2 % de desorden.

    El 98 % inicial de los elementos queda ordenado de mayor a menor,
    mientras que el 2 % restante se mezcla aleatoriamente. Se utiliza
    una semilla para obtener resultados reproducibles.

    Args:
        n: Cantidad de elementos que tendrá la lista.
        semilla: Semilla utilizada para mezclar los elementos finales.

    Returns:
        Una lista de n números enteros con aproximadamente un 2 %
        de los elementos desordenados al final.
    """
    generador = random.Random(semilla)

    cantidad_ordenada = int(n * 0.98)
    cantidad_nueva = n - cantidad_ordenada

    datos_ordenados = list(
        range(n, n - cantidad_ordenada, -1)
    )

    datos_nuevos = list(
        range(n - cantidad_ordenada, 0, -1)
    )

    generador.shuffle(datos_nuevos)

    return datos_ordenados + datos_nuevos


def generar_inverso(n: int) -> list[int]:
    """Genera una lista ordenada de menor a mayor.

    Esta entrada representa el escenario inverso para los algoritmos
    que ordenan de mayor a menor.

    Args:
        n: Cantidad de elementos que tendrá la lista.

    Returns:
        Una lista de n números enteros ordenados de menor a mayor.
    """
    return list(range(1, n + 1))