"""Algoritmos para encontrar el subarreglo de suma máxima."""


def subarreglo_fuerza_bruta(
    valores: list[float],
) -> tuple[int, int, float]:
    """Encuentra el subarreglo de suma máxima usando fuerza bruta.

    Recorre todas las posibles posiciones de inicio y fin y calcula
    la suma de cada subarreglo.

    Args:
        valores: Lista de valores sobre la que se busca el subarreglo.

    Returns:
        Una tupla con el índice inicial, el índice final y la suma máxima.
    """
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
    """Encuentra el mejor subarreglo que cruza el punto medio.

    Busca la mejor suma desde el punto medio hacia la izquierda y
    desde el punto medio hacia la derecha, y combina ambas partes.

    Args:
        valores: Lista de valores sobre la que se busca el subarreglo.
        inicio: Índice inicial del rango que se está evaluando.
        medio: Índice que divide el rango en dos partes.
        fin: Índice final del rango que se está evaluando.

    Returns:
        Una tupla con el índice inicial, el índice final y la suma
        máxima del subarreglo que cruza el punto medio.
    """
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
    """Encuentra el subarreglo de suma máxima por divide y vencerás.

    Divide el problema en dos mitades y compara el mejor subarreglo
    de la izquierda, el mejor de la derecha y el mejor que cruza
    el punto medio.

    Args:
        valores: Lista de valores sobre la que se busca el subarreglo.
        inicio: Índice inicial del rango que se está evaluando.
        fin: Índice final del rango que se está evaluando.

    Returns:
        Una tupla con el índice inicial, el índice final y la suma máxima.
    """
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