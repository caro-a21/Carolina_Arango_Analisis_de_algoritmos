"""Algoritmos de ordenamiento para el Laboratorio 1."""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de mayor a menor usando Insertion Sort.

    La función crea una copia de la lista original para no modificarla.
    También cuenta las comparaciones realizadas entre elementos.

    Args:
        datos: Lista de números enteros que se desea ordenar.

    Returns:
        Una tupla que contiene la lista ordenada de mayor a menor
        y el número total de comparaciones entre elementos.
    """
    copia = datos.copy()
    comparaciones = 0

    for i in range(1, len(copia)):
        clave = copia[i]
        j = i - 1

        while j >= 0:
            comparaciones += 1

            if copia[j] < clave:
                copia[j + 1] = copia[j]
                j -= 1
            else:
                break

        copia[j + 1] = clave

    return copia, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de mayor a menor usando Merge Sort.

    La función crea una copia de la lista original para no modificarla.
    El ordenamiento se realiza de forma recursiva y se cuentan las
    comparaciones realizadas entre elementos durante la mezcla.

    Args:
        datos: Lista de números enteros que se desea ordenar.

    Returns:
        Una tupla que contiene la lista ordenada de mayor a menor
        y el número total de comparaciones entre elementos.
    """
    copia = datos.copy()

    def ordenar(lista: list[int]) -> tuple[list[int], int]:
        """Ordena recursivamente una lista y cuenta comparaciones.

        Args:
            lista: Lista de números enteros que se desea ordenar.

        Returns:
            Una tupla con la lista ordenada de mayor a menor y el
            número de comparaciones realizadas.
        """
        if len(lista) <= 1:
            return lista, 0

        mitad = len(lista) // 2

        izquierda, comparaciones_izquierda = ordenar(
            lista[:mitad]
        )
        derecha, comparaciones_derecha = ordenar(
            lista[mitad:]
        )

        resultado = []
        i = 0
        j = 0
        comparaciones_mezcla = 0

        while i < len(izquierda) and j < len(derecha):
            comparaciones_mezcla += 1

            if izquierda[i] >= derecha[j]:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1

        while i < len(izquierda):
            resultado.append(izquierda[i])
            i += 1

        while j < len(derecha):
            resultado.append(derecha[j])
            j += 1

        total_comparaciones = (
            comparaciones_izquierda
            + comparaciones_derecha
            + comparaciones_mezcla
        )

        return resultado, total_comparaciones

    return ordenar(copia)