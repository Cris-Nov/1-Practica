import requests

def autenti(Correo, Contra):
    # URL del endpoint de login en el servidor Flask
    url = "http://localhost:5000/login"
    
    # Datos que se enviarán en el cuerpo de la solicitud (en formato JSON)
    datos = {
        "correo": Correo,
        "contra": Contra
    }
    
    try:
        # Enviar la solicitud POST al servidor
        response = requests.post(url, json=datos)
        
        # Verificar el código de estado de la respuesta
        if response.status_code == 200:
            # Si el login es correcto, devolver True
            print("Login exitoso:", response.json())
            return True
        elif response.status_code == 401:
            # Si las credenciales son incorrectas, devolver False
            print("Credenciales incorrectas.")
            return False
        else:
            # Manejar otros códigos de estado (por ejemplo, 404 si el endpoint no existe)
            print("Error en el servidor:", response.status_code)
            return False
    except requests.exceptions.RequestException as e:
        # Manejar errores de conexión (por ejemplo, si el servidor no está en ejecución)
        print("Error de conexión:", e)
        return False

# Ejemplo de uso
if __name__ == "__main__":
    correo = input("Ingrese su correo: ")
    contra = input("Ingrese su contraseña: ")
    
    if autenti(correo, contra):
        print("Acceso concedido.")
    else:
        print("Acceso denegado.")
    