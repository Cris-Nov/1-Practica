import requests

def Buscar_Usuarios(correo):
    url = f'http://localhost:5000/usuarios/{correo}'
    response = requests.get(url)
    if response.status_code == 200:
        print('Los usuarios con el correo buscado fueron encontrados:')
        usuarios = response.json()
        for usuario in usuarios:
            print(f'Nombre: {usuario["nombre"]}, Correo: {usuario["correo"]} Contra: {usuario["contra"]}')
    elif response.status_code == 404:
        print('No se encontraron usuarios con el correo buscado.')

if __name__ == '__main__':
    correo = input('Ingrese el correo: ')
    Buscar_Usuarios(correo)