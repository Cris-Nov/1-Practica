from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de datos simulada
usuarios = [
    {'nombre': 'Juan', 'correo': 'juan@example.com', 'contra': 'Empanada1'},
    {'nombre': 'Maria', 'correo': 'maria@example.com', 'contra': 'Empanada2'},
    {'nombre': 'Pedro', 'correo': 'pedro@example.com', 'contra': 'Empanada3'}
]

# Ruta para obtener usuarios (GET)
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(usuarios)

# Ruta para crear un nuevo usuario (POST)
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    nuevo_usuario = request.get_json()  # Obtener los datos JSON enviados
    usuarios.append(nuevo_usuario)  # Agregar el nuevo usuario
    return jsonify(nuevo_usuario), 201  # Retornar el nuevo usuario con código 201

# Ruta para buscar un usuario por correo (GET)
@app.route('/usuarios/<string:correo>', methods=['GET'])
def buscar_usuario(correo):
    usuario_encontrado = [usuario for usuario in usuarios if usuario['correo'] == correo]
    if usuario_encontrado:
        return jsonify(usuario_encontrado), 200
    else:
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404

# Ruta para eliminar un usuario por correo (DELETE)
@app.route('/usuarios/<string:correo>', methods=['DELETE'])
def eliminar_usuario(correo):
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario['correo'] != correo]
    return jsonify({'mensaje': 'Usuario eliminado correctamente'}), 200

# Ruta para el login (POST)
@app.route('/login', methods=['POST'])
def login():
    # Obtener los datos JSON enviados (correo y contraseña)
    datos = request.get_json()
    correo = datos.get('correo')
    contra = datos.get('contra')

    # Buscar el usuario en la base de datos simulada
    usuario_encontrado = [usuario for usuario in usuarios if usuario['correo'] == correo and usuario['contra'] == contra]

    if usuario_encontrado:
        return jsonify({'mensaje': 'Login correcto', 'usuario': usuario_encontrado[0]}), 200
    else:
        return jsonify({'mensaje': 'Credenciales incorrectas'}), 401

if __name__ == '__main__':
    app.run(debug=True)