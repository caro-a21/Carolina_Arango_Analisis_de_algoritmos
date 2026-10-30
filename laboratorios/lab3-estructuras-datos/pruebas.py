
"""Pruebas para la lista enlazada y la tabla hash."""

import random

from estructuras import ListaEnlazada, TablaHash


# Pruebas basicas de la lista enlazada.
lista = ListaEnlazada()
lista.insertar(1000000010, "en bodega")
lista.insertar(1000000024, "en reparto")

assert lista.buscar(1000000010) == "en bodega"
assert lista.buscar(1000000024) == "en reparto"
assert lista.buscar(9999999999) is None
assert lista.tamano == 2


# Pruebas basicas de la tabla hash.
tabla = TablaHash(7)
tabla.insertar(1000000010, "en bodega")
tabla.insertar(1000000024, "en reparto")

assert tabla.buscar(1000000010) == "en bodega"
assert tabla.buscar(1000000024) == "en reparto"
assert tabla.buscar(9999999999) is None
assert tabla.tamano == 2


# Prueba de colision forzada con m = 7.
tabla_colisiones = TablaHash(7)

guias_colision = {
    10: "en bodega",
    24: "en reparto",
    17: "entregado",
}

for guia, estado in guias_colision.items():
    tabla_colisiones.insertar(guia, estado)

assert tabla_colisiones.hash(10) == 3
assert tabla_colisiones.hash(24) == 3
assert tabla_colisiones.hash(17) == 3

for guia, estado in guias_colision.items():
    assert tabla_colisiones.buscar(guia) == estado

assert tabla_colisiones.casillas[3].tamano == 3
assert tabla_colisiones.factor_carga() == 3 / 7


# Pruebas con colecciones aleatorias.
azar = random.Random(42)

for numero_prueba in range(20):
    cantidad = azar.randint(30, 100)

    guias = azar.sample(range(10**9, 10**10), cantidad)

    lista_aleatoria = ListaEnlazada()
    tabla_aleatoria = TablaHash(101)

    estados = {}

    for guia in guias:
        estado = azar.choice(
            ["en bodega", "en reparto", "entregado"]
        )

        estados[guia] = estado
        lista_aleatoria.insertar(guia, estado)
        tabla_aleatoria.insertar(guia, estado)

    # Verificar las guias existentes.
    for guia in guias:
        resultado_lista = lista_aleatoria.buscar(guia)
        resultado_tabla = tabla_aleatoria.buscar(guia)

        assert resultado_lista == estados[guia]
        assert resultado_lista == resultado_tabla

    # Generar guias inexistentes.
    inexistentes = []

    while len(inexistentes) < 20:
        guia = azar.randint(10**9, 10**10 - 1)

        if guia not in estados and guia not in inexistentes:
            inexistentes.append(guia)

    # Verificar que ambas estructuras coinciden.
    for guia in inexistentes:
        resultado_lista = lista_aleatoria.buscar(guia)
        resultado_tabla = tabla_aleatoria.buscar(guia)

        assert resultado_lista is None
        assert resultado_tabla is None

print("Todas las pruebas fueron exitosas.")
print("Se verificaron las dos estructuras y 20 colecciones aleatorias.")
