import requests

def crear_usuario(nombre, correo,contra):
    # URL a la que se enviará la solicitud POST
    url = 'http://localhost:5000/usuarios'  # Asegúrate de que esta URL es correcta

    # Datos a enviar en el formulario
    datos = {'nombre': nombre, 'correo': correo, 'contra': contra}

    # Enviar la solicitud POST
    response = requests.post(url, json=datos)

    # Verificar la respuesta del servidor
    if response.status_code == 201:
        print("Usuario creado con éxito.")
    else:
        print(f"Error al crear el usuario. Código de estado: {response.status_code}")

# Llamar a la función con los datos proporcionados por el usuario
if __name__ == '__main__':
    nombre_usuario = input("Introduce el nombre del usuario: ")
    correo_usuario = input("Introduce el correo del usuario: ")
    contra_usuario = input("Introduce la contraseña: ")

    # Crear usuario con los datos del formulario
    crear_usuario(nombre_usuario, correo_usuario, contra_usuario)