# Diccionario para almacenar usuario y contraseña
base_usuarios: dict[str, str] = {}

def validar_usuario(usuario: str) -> bool:
    """Valida que el nombre de usuario tenga al menos 3 letras y contenga solo letras."""
    if len(usuario) < 3:
        print("Nombre de usuario debe tener al menos 3 caracteres")
        return False
    elif not usuario.isalpha():
        print("Nombre de usuario debe contener solo letras")
        return False
    return True

def validar_clave(clave: str) -> bool:
    """Valida que la clave tenga entre 8 y 10 caracteres y sea alfanumérica."""
    longitud = 8 <= len(clave) <= 10
    es_alphanumerica = clave.isalnum()
    if longitud and es_alphanumerica:
        return True
    else:
        print("Clave debe tener entre 8 y 10 caracteres, solo letras y/o números")
        return False

def registrar_usuario(base_usuarios: dict[str, str]) -> None:
    """Permite registrar un nuevo usuario en el sistema."""
    print("REGISTRO DE USUARIO (escriba 'salir' para volver al menú)")
    while True:
        # Solicitar y validar el nombre de usuario
        usuario_input = input("Nombre de Usuario: ").lower()
        if usuario_input == "salir":  # Permite al usuario salir del registro
            print("Registro cancelado.")
            break
        if not validar_usuario(usuario_input):
            continue
        usuario = usuario_input
        if usuario in base_usuarios:
            print("El usuario ya está registrado.")
            continue

        # Solicitar y validar la clave
        clave_input = input("Clave del usuario (8-10 caracteres alfanuméricos): ")
        if not validar_clave(clave_input):
            continue
        base_usuarios[usuario] = clave_input  # Guardar usuario y clave
        print("Usuario registrado con éxito.")
        break

def mostrar_usuarios(base_usuarios: dict[str, str]) -> None:
    """Muestra la lista de usuarios registrados en el sistema."""
    print("Lista de usuarios registrados:")
    for usuario, clave in base_usuarios.items():
        print(f"Usuario: {usuario.upper()}, Clave: {'*' * len(clave)}")

def entrar_al_sistema(base_usuarios: dict[str, str]) -> None:
    """Permite a un usuario registrado iniciar sesión en el sistema."""
    print("ACCESO AL SISTEMA")
    usuario = input("Usuario: ")
    clave = input("Clave: ")
    if usuario in base_usuarios:
        if base_usuarios[usuario] == clave:
            print("Acceso concedido")
        else:
            print("La clave no coincide")
    else:
        print("El usuario no está registrado")

def mostrar_menu() -> str:
    """Muestra el menú de opciones y devuelve la elección del usuario."""
    print("\nMENU PRINCIPAL")
    print("1. Registrar un nuevo usuario")
    print("2. Mostrar usuarios registrados")
    print("3. Entrar al sistema")
    print("4. Salir")
    opcion = input("Seleccione una opción (1-4): ")
    return opcion

def main() -> None:
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            registrar_usuario(base_usuarios)
        elif opcion == "2":
            mostrar_usuarios(base_usuarios)
        elif opcion == "3":
            entrar_al_sistema(base_usuarios)
        elif opcion == "4":
            print("Gracias por utilizar nuestros servicios, Federico Furgiuele.")
            break
        else:
            print("Opción inválida, por favor intente nuevamente.")

main()
