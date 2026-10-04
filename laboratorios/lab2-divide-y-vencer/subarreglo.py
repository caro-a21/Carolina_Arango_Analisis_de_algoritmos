"""Subarreglo maximo: fuerza bruta y divide y venceras."""


def subarreglo_fuerza_bruta(
    valores: list[float],
) -> tuple[int, int, float]:
    
    mejor_inicio = 0
    mejor_fin = 0
    mejor_suma = valores[0]

    for inicio in range(len(valores)):
        suma_actual = 0

        for fin in range(inicio, len(valores)):
            suma_actual += valores[fin]

            if suma_actual > mejor_suma:
                mejor_suma = suma_actual
                mejor_inicio = inicio
                mejor_fin = fin

    return mejor_inicio, mejor_fin, mejor_suma


def suma_cruzada(
    valores: list[float],
    inicio: int,
    medio: int,
    fin: int,
) -> tuple[int, int, float]:
    
    suma = 0
    mejor_suma_izquierda = float("-inf")
    mejor_inicio = medio

    for indice in range(medio, inicio - 1, -1):
        suma += valores[indice]

        if suma > mejor_suma_izquierda:
            mejor_suma_izquierda = suma
            mejor_inicio = indice

    suma = 0
    mejor_suma_derecha = float("-inf")
    mejor_fin = medio + 1

    for indice in range(medio + 1, fin + 1):
        suma += valores[indice]

        if suma > mejor_suma_derecha:
            mejor_suma_derecha = suma
            mejor_fin = indice

    return (
        mejor_inicio,
        mejor_fin,
        mejor_suma_izquierda + mejor_suma_derecha,
    )


def subarreglo_maximo(
    valores: list[float],
    inicio: int,
    fin: int,
) -> tuple[int, int, float]:
    
    if inicio == fin:
        return inicio, fin, valores[inicio]

    medio = (inicio + fin) // 2

    mejor_izquierda = subarreglo_maximo(
        valores,
        inicio,
        medio,
    )

    mejor_derecha = subarreglo_maximo(
        valores,
        medio + 1,
        fin,
    )

    mejor_cruzada = suma_cruzada(
        valores,
        inicio,
        medio,
        fin,
    )

    if mejor_izquierda[2] >= mejor_derecha[2] and (
        mejor_izquierda[2] >= mejor_cruzada[2]
    ):
        return mejor_izquierda

    if mejor_derecha[2] >= mejor_izquierda[2] and (
        mejor_derecha[2] >= mejor_cruzada[2]
    ):
        return mejor_derecha

    return mejor_cruzada