"""
Refactorización del código anterior
"""


def validar_nombre(nombre: str) -> bool:
    if len(nombre) < 3:
        print("🚫 El nombre debe tener al menos 3 caracteres")
        return False
    elif not nombre.isalpha():
        print("🚫 El nombre debe contener letras")
        return False
    return True


def validar_dni(dni: str) -> bool:
    longitud = len(dni) >= 8 and len(dni) <= 10
    entrada_numerica = dni.isdecimal()
    if longitud and entrada_numerica:
        return True
    else:
        print("🚫 El DNI debe tener 8 a 10 dígitos")
        return False


def registrar_miembro(miembros_club):
    dni: int
    nombre: str
    print("REGISTRO DEL MIEMBROS DEL CLUB")
    while True:
        # ***********
        # *** DNI ***
        # ***********
        dni_input = input("DNI del miembro: ")
        validacion_dni = validar_dni(dni_input)
        if not validacion_dni:
            continue
        dni = int(dni_input)
        if dni in miembros_club:
            print(" 🚫El miembro ya está registrado.")
            continue
        # **************
        # *** NOMBRE ***
        # **************
        nombre_input = input("Nombre del miembro: ")
        validacion_nombre = validar_nombre(nombre_input)
        if not validacion_nombre:
            continue
        nombre = nombre_input
        break
    miembros_club[dni] = nombre


def mostrar_miembros_del_club(miembros_club):
    print("LISTA DE MIEMBROS DEL CLUB")
    for dni, nombre in miembros_club.items():
        print(dni, nombre)


def entrar_al_sistema(miembros_club):
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
    miembros_club: dict[int, str] = {}
    miembros_club = {
        12345678: "Agustina",
        23456789: "Tomás",
        34567890: "Isabel",
    }
    registrar_miembro(miembros_club)
    mostrar_miembros_del_club(miembros_club)
    entrar_al_sistema(miembros_club)


main()
