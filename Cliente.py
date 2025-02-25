import requests #importa la biblioteca para optener las peticiones

def obtener_datos_usuarios():
    #aqui se realiza una peticion GET al servidor 
    response = requests.get('http://localhost:5000/usuarios')
    if response.status_code == 200: # Si la peticion es codigo 200
        usuarios = response.json()# Esto convierte el cuerpo de la respuesta json a un objeto de python
        print ("Usuarios encontrados:")
        for usuario in usuarios:
            print(f"Nombre: {usuario['nombre']}, Correo: {usuario['correo']}, Contra: {usuario['contra']}")
        else:
            print("No se encontraron usuarios.")
            
            
            
if __name__ == '__main__':
    obtener_datos_usuarios() #Ejecutar la funcion principal








