
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