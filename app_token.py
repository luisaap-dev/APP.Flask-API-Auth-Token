from flask import Flask, jsonify, request,session
import mysql.connector
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from config import db_config
from flask_cors import CORS


app = Flask(__name__)
auth_basic = HTTPBasicAuth()
jwt = JWTManager(app)

app.config['JWT_SECRET_KEY'] = 'tokencOx1Ii0C#q#viAW$JgU4x79T#f0CADO0W4@hL6WbM*MQd4dxe'
CORS(app)


# Función para establecer la conexión a la base de datos
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Ruta para registrar un nuevo usuario
@app.route("/api/register", methods=["POST"])
def register_user():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    # Verificar si el usuario ya existe en la base de datos
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT Usuario FROM usuarios WHERE Usuario = %s", (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            return jsonify({"error": "El usuario ya existe"}), 400

        # Insertar nuevo usuario en la base de datos (sin hashear la contraseña)
        cursor.execute("INSERT INTO usuarios (Usuario, Password) VALUES (%s, %s)", (username, password))
        connection.commit()

    return jsonify({"Mensaje": "Usuario registrado correctamente"}), 201


# Ruta para iniciar sesión
@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    # Verificar las credenciales del usuario en la base de datos
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT Usuario, Password FROM usuarios WHERE Usuario = %s", (username,))
        user = cursor.fetchone()
        if user and user[1] == password:
            access_token = create_access_token(identity=username)
            response = {
                "Mensaje": "Inicio de sesión exitoso",
                "Token_acceso": access_token
            }
            return jsonify(response), 200
        else:
            response = {
                "error": "Credenciales inválidas"
            }
            return jsonify(response), 401

# Ruta para generar un token de acceso
@app.route("/api/token", methods=["POST"])
@auth_basic.login_required
def generate_token():
    access_token = create_access_token(identity=auth_basic.current_user())
    return jsonify(access_token=access_token)

# Autenticación básica
@auth_basic.verify_password
def verify_password(username, password):
    try:
        with get_db_connection() as connection, connection.cursor(
            dictionary=True
        ) as cursor:
            cursor.execute("SELECT Usuario, Password FROM usuarios WHERE Usuario = %s", (username, ))
            user = cursor.fetchone()

        if user and user["Password"] == password:
            # Si las credenciales son válidas, establece el nombre de usuario en la sesión
            session['username'] = user["Usuario"]
            return user["Usuario"]
    except Exception as e:
        print("Error:", e)

# Ruta para obtener la lista de clientes
@app.route("/api/clientes", methods=["GET"])
@jwt_required()
def get_clientes():
    search_params = {}
    for param, value in request.args.items():
        search_params[param] = value

    with get_db_connection() as connection, connection.cursor(
        dictionary=True
    ) as cursor:
        if search_params:
            conditions = []
            values = []
            for field, value in search_params.items():
                conditions.append(f"{field} = %s")
                values.append(value)
            where_clause = " AND ".join(conditions)
            query = f"SELECT * FROM clientes WHERE {where_clause}"
            cursor.execute(query, tuple(values))
        else:
            cursor.execute("SELECT * FROM clientes")

        clientes = cursor.fetchall()
        return jsonify(clientes)

# Ruta para obtener un cliente por ID
@app.route("/api/clientes/<int:id>", methods=["GET"])
@jwt_required()
def get_cliente(id):
    with get_db_connection() as connection, connection.cursor(
        dictionary=True
    ) as cursor:
        cursor.execute("SELECT * FROM clientes WHERE id = %s", (id,))
        cliente = cursor.fetchone()
        if cliente:
            return jsonify(cliente)
        else:
            return jsonify({"error": "Cliente no encontrado"}), 404

# Ruta para crear un nuevo cliente
@app.route("/api/clientes", methods=["POST"])
@jwt_required()
def crear_cliente():
    new_cliente = request.get_json()
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO clientes (Nombre, Direccion, Ciudad, Pais, Telefono, Email) VALUES (%s, %s, %s, %s, %s, %s)",
            (
                new_cliente["Nombre"],
                new_cliente["Direccion"],
                new_cliente["Ciudad"],
                new_cliente["Pais"],
                new_cliente["Telefono"],
                new_cliente["Email"],
            ),
        )
        connection.commit()
    return jsonify({"Mensaje": "Cliente creado correctamente"}), 201

# Ruta para actualizar un cliente por ID
@app.route("/api/clientes/<int:id>", methods=["PUT"])
@jwt_required()
def actualizar_cliente(id):
    updated_cliente = request.get_json()
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            "UPDATE clientes SET Nombre = %s, Direccion = %s, Ciudad = %s, Pais = %s, Telefono = %s, Email = %s WHERE id = %s",
            (
                updated_cliente["Nombre"],
                updated_cliente["Direccion"],
                updated_cliente["Ciudad"],
                updated_cliente["Pais"],
                updated_cliente["Telefono"],
                updated_cliente["Email"],
                id,
            ),
        )
        connection.commit()
    return jsonify({"Mensaje": f"Cliente con ID {id} actualizado correctamente"})

# Ruta para eliminar un cliente por ID
@app.route("/api/clientes/<int:id>", methods=["DELETE"])
@jwt_required()
def eliminar_cliente(id):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
        connection.commit()
    return jsonify({"Mensaje": f"Cliente con ID {id} eliminado correctamente"})

if __name__ == "__main__":
    app.run(debug=True)
