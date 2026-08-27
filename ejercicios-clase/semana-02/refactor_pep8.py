
def calcular_promedio(lista: list[int]) -> float:
    """Calcula el promedio de una lista de números.

    Args:
        lista: Lista de números enteros.

    Returns:
        El promedio de los números de la lista.
    """
    suma = 0

    for numero in lista:
        suma = suma + numero

    return suma / len(lista)


def main() -> None:
    """Ejecuta el programa principal."""
    numeros = [1, 2, 3, 4, 5]
    promedio = calcular_promedio(numeros)

    print(promedio)


if __name__ == "__main__":
    main()

