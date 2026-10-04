import random

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


# Caso 1: serie de la situacion problema
serie = [-3, 5, -2, 8, -6, 3, 9, -4]

assert subarreglo_fuerza_bruta(serie)[2] == 17
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 17


# Caso 2: un solo elemento
serie = [7]

assert subarreglo_fuerza_bruta(serie)[2] == 7
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 7


# Caso 3: todos los valores negativos
serie = [-8, -3, -10, -5]

assert subarreglo_fuerza_bruta(serie)[2] == -3
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == -3


# Caso 4: todos los valores positivos
serie = [2, 4, 1, 3, 5]

assert subarreglo_fuerza_bruta(serie)[2] == 15
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 15


# Caso 5: el mejor tramo cruza el punto medio
serie = [2, 3, -1, 5, -10]

resultado_fuerza = subarreglo_fuerza_bruta(serie)
resultado_divide = subarreglo_maximo(
    serie,
    0,
    len(serie) - 1,
)

assert resultado_fuerza[2] == 9
assert resultado_divide[2] == 9

# Caso 6: veinte listas aleatorias
random.seed(42)

for _ in range(20):
    serie = [
        random.randint(-20, 20)
        for _ in range(random.randint(1, 20))
    ]

    resultado_fuerza = subarreglo_fuerza_bruta(serie)
    resultado_divide = subarreglo_maximo(
        serie,
        0,
        len(serie) - 1,
    )

    assert resultado_fuerza[2] == resultado_divide[2]


print("Todas las pruebas pasaron correctamente.")