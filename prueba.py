"""
Programa para registrar miembros de un club: tendrán un nombre y dni.
"""

miembros_club = {}


def registrar_miembro():
    print("REGISTRO DEL MIEMBROS DEL CLUB")
    nombre = input("Nombre: ")
    dni = int(input("DNI: "))
    if dni in miembros_club:
        print("El miembro ya está registrado.")
    else:
        miembros_club[dni] = nombre


def mostrar_miembros_del_club():
    print("LISTA DE MIEMBROS DEL CLUB")
    for dni, nombre in miembros_club.items():
        print(dni, nombre)


def entrar_al_sistema():
    print("ACCESO AL SISTEMA")
    nombre = input("Nombre: ")
    dni = int(input("DNI: "))
    if dni in miembros_club:
        if miembros_club[dni] == nombre:
            print("Bienvenido al club")
        else:
            print("El nombre no coincide")
    else:
        print("El dni no está registrado")


def main():
    registrar_miembro()
    registrar_miembro()
    mostrar_miembros_del_club()
    entrar_al_sistema()


main()
