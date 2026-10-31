
"""Experimentos para comparar una lista enlazada y una tabla hash."""

import math
import random
import time
from collections.abc import Callable
from pathlib import Path

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash


# Configuracion general de los experimentos.
TAMANOS = [100, 500, 1000, 5000, 20000, 50000]
CANTIDAD_BUSQUEDAS = 200
REPETICIONES = 3
SEMILLA = 42

ESTADOS = ["en bodega", "en reparto", "entregado"]

DIRECTORIO_GRAFICAS = Path(__file__).resolve().parent / "graficas"


def es_primo(numero: int) -> bool:
    """Comprueba si un numero es primo.

    Args:
        numero: Numero entero que se desea comprobar.

    Returns:
        True si el numero es primo, False en caso contrario.
    """
    if numero < 2:
        return False

    if numero == 2:
        return True

    if numero % 2 == 0:
        return False

    divisor = 3

    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False

        divisor += 2

    return True


def siguiente_primo(numero: int) -> int:
    """Encuentra el primer numero primo mayor o igual al recibido.

    Args:
        numero: Numero desde el cual comienza la busqueda.

    Returns:
        El primer numero primo encontrado.
    """
    candidato = max(2, numero)

    while not es_primo(candidato):
        candidato += 1

    return candidato


def generar_guias_existentes(
    cantidad: int,
    semilla: int = SEMILLA
) -> list[int]:
    """Genera guias distintas de diez digitos.

    Args:
        cantidad: Cantidad de guias que se deben generar.
        semilla: Semilla para reproducir los datos.

    Returns:
        Lista de guias enteras sin repetir.
    """
    azar = random.Random(semilla)

    return azar.sample(range(10**9, 10**10), cantidad)


def generar_guias_inexistentes(
    existentes: set[int],
    cantidad: int,
    semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: Guias almacenadas en las estructuras.
        cantidad: Cuantas guias inexistentes generar.
        semilla: Semilla del generador para reproducir la medicion.

    Returns:
        Una lista con la cantidad solicitada de guias inexistentes.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []

    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)

        if guia not in existentes:
            inexistentes.append(guia)

    return inexistentes


def construir_lista(guias: list[int]) -> ListaEnlazada:
    """Construye una lista enlazada con las guias recibidas.

    Args:
        guias: Lista de numeros de guia que se almacenaran.

    Returns:
        Lista enlazada con todas las guias y sus estados.
    """
    lista = ListaEnlazada()

    for indice, guia in enumerate(guias):
        estado = ESTADOS[indice % len(ESTADOS)]
        lista.insertar(guia, estado)

    return lista


def construir_tabla(guias: list[int], m: int) -> TablaHash:
    """Construye una tabla hash con las guias recibidas.

    Args:
        guias: Lista de numeros de guia que se almacenaran.
        m: Cantidad de casillas de la tabla.

    Returns:
        Tabla hash con todas las guias y sus estados.
    """
    tabla = TablaHash(m)

    for indice, guia in enumerate(guias):
        estado = ESTADOS[indice % len(ESTADOS)]
        tabla.insertar(guia, estado)

    return tabla


def verificar_estructuras(
    lista: ListaEnlazada,
    tabla: TablaHash,
    guias: list[int]
) -> None:
    """Comprueba que ambas estructuras devuelvan los mismos estados.

    Args:
        lista: Lista enlazada que se desea verificar.
        tabla: Tabla hash que se desea verificar.
        guias: Guias existentes que se utilizaran en la prueba.

    Raises:
        AssertionError: Si las estructuras devuelven resultados diferentes.
    """
    muestra = guias[:min(20, len(guias))]

    for guia in muestra:
        resultado_lista = lista.buscar(guia)
        resultado_tabla = tabla.buscar(guia)

        assert resultado_lista == resultado_tabla, (
            f"Resultados diferentes para la guia {guia}"
        )

        assert resultado_lista is not None, (
            f"No se encontro la guia existente {guia}"
        )


def medir_tiempo_medio(
    buscar: Callable[[int], str | None],
    consultas: list[int],
    repeticiones: int = REPETICIONES
) -> float:
    """Mide el tiempo promedio de una busqueda.

    Args:
        buscar: Metodo de busqueda de la estructura.
        consultas: Guias que se van a buscar.
        repeticiones: Numero de veces que se repite la medicion.

    Returns:
        Tiempo promedio en segundos por busqueda.
    """
    tiempos: list[float] = []

    for _ in range(repeticiones):
        inicio = time.perf_counter()

        for guia in consultas:
            buscar(guia)

        fin = time.perf_counter()

        tiempo_medio = (fin - inicio) / len(consultas)
        tiempos.append(tiempo_medio)

    return sum(tiempos) / len(tiempos)


def ejecutar_experimento_a() -> None:
    """Compara los tiempos de la lista enlazada y la tabla hash."""
    tiempos_lista: list[float] = []
    tiempos_tabla: list[float] = []

    print("\nEXPERIMENTO A: LISTA FRENTE A TABLA HASH")
    print("-" * 85)
    print(
        f"{'n':>8} {'m':>8} {'Alfa':>12} "
        f"{'Lista (s/busq.)':>22} {'Tabla (s/busq.)':>22}"
    )
    print("-" * 85)

    for n in TAMANOS:
        guias = generar_guias_existentes(n)
        existentes = set(guias)

        consultas = generar_guias_inexistentes(
            existentes,
            CANTIDAD_BUSQUEDAS
        )

        # Se elige un numero primo cercano a n / 2.
        m = siguiente_primo(n // 2)

        # La construccion se realiza antes de medir.
        lista = construir_lista(guias)
        tabla = construir_tabla(guias, m)

        # Se verifica que ambas estructuras respondan igual.
        verificar_estructuras(lista, tabla, guias)

        # Se cronometra unicamente la busqueda.
        tiempo_lista = medir_tiempo_medio(
            lista.buscar,
            consultas
        )

        tiempo_tabla = medir_tiempo_medio(
            tabla.buscar,
            consultas
        )

        alfa = n / m

        tiempos_lista.append(tiempo_lista)
        tiempos_tabla.append(tiempo_tabla)

        print(
            f"{n:>8} {m:>8} {alfa:>12.4f} "
            f"{tiempo_lista:>22.10e} "
            f"{tiempo_tabla:>22.10e}"
        )

    # Generacion de la primera grafica.
    plt.figure(figsize=(10, 6))

    plt.plot(
        TAMANOS,
        tiempos_lista,
        marker="o",
        label="Lista enlazada"
    )

    plt.plot(
        TAMANOS,
        tiempos_tabla,
        marker="s",
        label="Tabla hash"
    )

    plt.title("Tiempo de busqueda: lista enlazada frente a tabla hash")
    plt.xlabel("Numero de guias (n)")
    plt.ylabel("Tiempo medio por busqueda (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    DIRECTORIO_GRAFICAS.mkdir(parents=True, exist_ok=True)

    plt.savefig(
        DIRECTORIO_GRAFICAS / "lista_vs_tabla.png",
        dpi=150
    )

    plt.close()

    print("\nPrimera grafica guardada correctamente.")


def ejecutar_experimento_b() -> None:
    """Mide el tiempo de busqueda para diferentes factores de carga."""
    n = 20000
    factores_deseados = [0.5, 1, 4, 10]

    guias = generar_guias_existentes(n)
    existentes = set(guias)

    consultas = generar_guias_inexistentes(
        existentes,
        CANTIDAD_BUSQUEDAS
    )

    # Se construye una lista de referencia para verificar los resultados.
    lista_referencia = construir_lista(guias)

    factores_medidos: list[float] = []
    tiempos_tabla: list[float] = []

    print("\nEXPERIMENTO B: EFECTO DEL FACTOR DE CARGA")
    print("-" * 70)
    print(
        f"{'Alfa deseado':>15} {'m':>10} "
        f"{'Alfa real':>15} {'Tiempo (s/busq.)':>22}"
    )
    print("-" * 70)

    for alfa_deseado in factores_deseados:
        # Se calcula m para obtener el factor de carga solicitado.
        m_aproximado = math.ceil(n / alfa_deseado)
        m = siguiente_primo(m_aproximado)

        tabla = construir_tabla(guias, m)

        # Se verifica que la lista y la tabla devuelvan lo mismo.
        verificar_estructuras(lista_referencia, tabla, guias)

        # Se mide unicamente la busqueda de guias inexistentes.
        tiempo_tabla = medir_tiempo_medio(
            tabla.buscar,
            consultas
        )

        alfa_real = tabla.factor_carga()

        factores_medidos.append(alfa_real)
        tiempos_tabla.append(tiempo_tabla)

        print(
            f"{alfa_deseado:>15.2f} {m:>10} "
            f"{alfa_real:>15.6f} "
            f"{tiempo_tabla:>22.10e}"
        )

    # Generacion de la segunda grafica.
    plt.figure(figsize=(10, 6))

    plt.plot(
        factores_medidos,
        tiempos_tabla,
        marker="o",
        label="Tabla hash (n = 20.000)"
    )

    plt.title("Tiempo de busqueda segun el factor de carga")
    plt.xlabel("Factor de carga (alfa)")
    plt.ylabel("Tiempo medio por busqueda (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    DIRECTORIO_GRAFICAS.mkdir(parents=True, exist_ok=True)

    plt.savefig(
        DIRECTORIO_GRAFICAS / "tiempo_vs_alfa.png",
        dpi=150
    )

    plt.close()

    print("\nSegunda grafica guardada correctamente.")


if __name__ == "__main__":
    ejecutar_experimento_a()
    ejecutar_experimento_b()

    print("\nLos dos experimentos finalizaron correctamente.")
