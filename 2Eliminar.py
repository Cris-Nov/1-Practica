import requests

def Eliminar_Usuario(correo):
    url = f'http://localhost:5000/usuarios/{correo}'
    response = requests.delete(url)
    if response.status_code == 200:
        print(response.json()['mensaje'])
    else:
        print('No se pudo eliminar el usuario. Verifica el correo.')

if __name__ == '__main__':
    correo = input('Ingresa el correo del usuario a eliminar: ')
    Eliminar_Usuario(correo)