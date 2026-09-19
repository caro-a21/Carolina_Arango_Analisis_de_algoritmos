import random


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:

    generador = random.Random(semilla)
    datos = list(range(1, n + 1))
    generador.shuffle(datos)

    return datos


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
 
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
  
    return list(range(1, n + 1))