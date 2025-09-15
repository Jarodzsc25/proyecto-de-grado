print("HOLA MUNDO")

# Diccionario para registrar usuarios con contraseña prueba
usuarios = {
    "admin": "15KA",
    "jarod": "SOLA",
    "usuario": "clave"
}
#primero se pedira que se ingrese el usuria, seguido de la contraseña
def login():
    print("=== Sistema de Login ===")
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
#en aka se validara tanto el usuario como la contraseña si estas estan registradas
    if usuario in usuarios and usuarios[usuario] == contraseña:
        print(f"Bienvenido {usuario}, acceso concedido.")
    else:
        print("Usuario o contraseña incorrectos.")
#aka llamamos a la funcion login
if __name__ == "__main__":
    login()