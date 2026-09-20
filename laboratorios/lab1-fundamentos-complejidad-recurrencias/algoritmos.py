
def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
  
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
 
    copia = datos.copy()

    def ordenar(lista: list[int]) -> tuple[list[int], int]:
        
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