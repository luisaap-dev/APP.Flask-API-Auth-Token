# Flask API para Gestión de Clientes con autenticación básica y token de acceso

Esta es una API desarrollada en Python utilizando el framework Flask para la gestión de clientes. Permite registrar usuarios, iniciar sesión, generar tokens de acceso, y realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en una base de datos MySQL para administrar información de clientes.

## Requisitos

- Python 3.7 o superior
- Flask
- MySQL Server
- Flask-HTTPAuth
- Flask-JWT-Extended
- Flask-CORS
- Conexión a una base de datos MySQL (consulte `config.py` para configuración de la base de datos)

## Instalación

1. Clona este repositorio: `git clone https://github.com/tu_usuario/tu_repositorio.git`
2. Instala las dependencias: `pip install -r requirements.txt`
3. Configura la base de datos en `config.py`.
4. Ejecuta la aplicación: `python app.py`

## Rutas / ## Endpoints

### Registro de Usuario

Registra un nuevo usuario en el sistema.

- **URL:** `/api/register`
- **Método:** `POST`
- **Datos de entrada:**
  ```json
  {
    "username": "nombre_usuario",
    "password": "contraseña"
  }
  ```
- **Respuesta exitosa:**
  - Código: 201 (Created)
  - Contenido:
    ```json
    {
      "Mensaje": "Usuario registrado correctamente"
    }
    ```
- **Respuesta de error:**
  - Código: 400 (Bad Request)
  - Contenido:
    ```json
    {
      "error": "El usuario ya existe"
    }
    ```

### Inicio de Sesión

Inicia sesión de un usuario registrado y devuelve un token de acceso.

- **URL:** `/api/login`
- **Método:** `POST`
- **Datos de entrada:**
  ```json
  {
    "username": "nombre_usuario",
    "password": "contraseña"
  }
  ```
- **Respuesta exitosa:**
  - Código: 200 (OK)
  - Contenido:
    ```json
    {
      "Mensaje": "Inicio de sesión exitoso",
      "Token_acceso": "JWT_token"
    }
    ```
- **Respuesta de error:**
  - Código: 401 (Unauthorized)
  - Contenido:
    ```json
    {
      "error": "Credenciales inválidas"
    }
    ```

### Generar Token de Acceso

Genera un token de acceso utilizando autenticación básica.

- **URL:** `/api/token`
- **Método:** `POST`
- **Autenticación:** Básica (usuario y contraseña)
- **Respuesta exitosa:**
  - Código: 200 (OK)
  - Contenido:
    ```json
    {
      "access_token": "JWT_token"
    }
    ```

### Obtener Lista de Clientes

Obtiene la lista de clientes, con opción de filtrar según parámetros de búsqueda.

- **URL:** `/api/clientes`
- **Método:** `GET`
- **Autenticación:** Token JWT requerido
- **Parámetros de búsqueda:** Opcionales, ej. `/api/clientes?Ciudad=Nueva+York&Pais=EE.UU.`
- **Respuesta exitosa:**
  - Código: 200 (OK)
  - Contenido: Lista de clientes en formato JSON

### Obtener Cliente por ID

Obtiene información detallada de un cliente por su ID.

- **URL:** `/api/clientes/<int:id>`
- **Método:** `GET`
- **Autenticación:** Token JWT requerido
- **Respuesta exitosa:**
  - Código: 200 (OK)
  - Contenido: Información del cliente en formato JSON
- **Respuesta de error:**
  - Código: 404 (Not Found)
  - Contenido:
    ```json
    {
      "error": "Cliente no encontrado"
    }
    ```

### Crear Cliente

Crea un nuevo cliente en la base de datos.

- **URL:** `/api/clientes`
- **Método:** `POST`
- **Autenticación:** Token JWT requerido
- **Datos de entrada:**
  ```json
  {
    "Nombre": "Nombre del Cliente",
    "Direccion": "Dirección del Cliente",
    "Ciudad": "Ciudad del Cliente",
    "Pais": "País del Cliente",
    "Telefono": "Número de Teléfono",
    "Email": "Correo Electrónico"
  }
  ```
- **Respuesta exitosa:**
  - Código: 201 (Created)
  - Contenido:
    ```json
    {
      "Mensaje": "Cliente creado correctamente"
    }
    ```

### Actualizar Cliente por ID

Actualiza la información de un cliente por su ID.

- **URL:** `/api/clientes/<int:id>`
- **Método:** `PUT`
- **Autenticación:** Token JWT requerido
- **Datos de entrada:**
  ```json
  {
    "Nombre": "Nuevo Nombre",
    "Direccion": "Nueva Dirección",
    "Ciudad": "Nueva Ciudad",
    "Pais": "Nuevo País",
    "Telefono": "Nuevo Número de Teléfono",
    "Email": "Nuevo Correo Electrónico"
  }
  ```
- **Respuesta exitosa:**
  - Código: 200 (OK)
  - Contenido:
    ```json
    {
      "Mensaje": "Cliente con ID <id> actualizado correctamente"
    }
    ```

### Eliminar Cliente por ID

Elimina un cliente de la base de datos por su ID.

- **URL:** `/api/clientes/<int:id>`
- **Método:** `DELETE`
- **Autenticación:** Token JWT requerido
- **Respuesta exitosa:**
  - Código: 200 (OK)
  - Contenido:
    ```json
    {
      "Mensaje": "Cliente con ID <id> eliminado correctamente"
    }
    ```

## Ejecución

Ejecuta la aplicación Flask con el siguiente comando:

```bash
python app_token.py
```

La API estará disponible en `http://localhost:5000`.

**Nota:** Asegúrate de haber configurado correctamente la conexión a la base de datos en `config.py`.

## Autor

Luis Ares - [Perfil de GitHub](https://github.com/luisaap-dev)

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.
