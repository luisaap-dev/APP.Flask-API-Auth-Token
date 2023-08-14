### Ejemplo 1: Registro de Usuario

#### Solicitud:
```http
POST /api/register
Content-Type: application/json

{
  "username": "usuario_nuevo",
  "password": "contraseña_segura"
}
```

#### Respuesta exitosa:
```http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "Mensaje": "Usuario registrado correctamente"
}
```

#### Respuesta de error (usuario existente):
```http
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
  "error": "El usuario ya existe"
}
```

### Ejemplo 2: Inicio de Sesión

#### Solicitud:
```http
POST /api/login
Content-Type: application/json

{
  "username": "usuario_nuevo",
  "password": "contraseña_segura"
}
```

#### Respuesta exitosa:
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "Mensaje": "Inicio de sesión exitoso",
  "Token_acceso": "JWT_token"
}
```

#### Respuesta de error (credenciales incorrectas):
```http
HTTP/1.1 401 Unauthorized
Content-Type: application/json

{
  "error": "Credenciales inválidas"
}
```

### Ejemplo 3: Generar Token de Acceso

#### Solicitud:
```http
POST /api/token
Authorization: Basic base64(usuario_nuevo:contraseña_segura)
```

#### Respuesta exitosa:
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "access_token": "JWT_token"
}
```

### Ejemplo 4: Obtener Lista de Clientes

#### Solicitud:
```http
GET /api/clientes
Authorization: Bearer JWT_token
```

#### Respuesta exitosa:
```http
HTTP/1.1 200 OK
Content-Type: application/json

[
  {
    "id": 1,
    "Nombre": "Cliente 1",
    "Direccion": "Dirección Cliente 1",
    "Ciudad": "Ciudad Cliente 1",
    "Pais": "País Cliente 1",
    "Telefono": "123456789",
    "Email": "cliente1@example.com"
  },
  {
    "id": 2,
    "Nombre": "Cliente 2",
    "Direccion": "Dirección Cliente 2",
    "Ciudad": "Ciudad Cliente 2",
    "Pais": "País Cliente 2",
    "Telefono": "987654321",
    "Email": "cliente2@example.com"
  }
  // ... otros clientes
]
```

### Ejemplo 5: Obtener Cliente por ID

#### Solicitud:
```http
GET /api/clientes/1
Authorization: Bearer JWT_token
```

#### Respuesta exitosa:
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 1,
  "Nombre": "Cliente 1",
  "Direccion": "Dirección Cliente 1",
  "Ciudad": "Ciudad Cliente 1",
  "Pais": "País Cliente 1",
  "Telefono": "123456789",
  "Email": "cliente1@example.com"
}
```

#### Respuesta de error (cliente no encontrado):
```http
HTTP/1.1 404 Not Found
Content-Type: application/json

{
  "error": "Cliente no encontrado"
}
```

### Ejemplo 6: Crear Cliente

#### Solicitud:
```http
POST /api/clientes
Authorization: Bearer JWT_token
Content-Type: application/json

{
  "Nombre": "Nuevo Cliente",
  "Direccion": "Nueva Dirección",
  "Ciudad": "Nueva Ciudad",
  "Pais": "Nuevo País",
  "Telefono": "555555555",
  "Email": "nuevo_cliente@example.com"
}
```

#### Respuesta exitosa:
```http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "Mensaje": "Cliente creado correctamente"
}
```

### Ejemplo 7: Actualizar Cliente por ID

#### Solicitud:
```http
PUT /api/clientes/1
Authorization: Bearer JWT_token
Content-Type: application/json

{
  "Nombre": "Cliente Modificado",
  "Direccion": "Nueva Dirección Modificada",
  "Ciudad": "Nueva Ciudad Modificada",
  "Pais": "Nuevo País Modificado",
  "Telefono": "999999999",
  "Email": "cliente_modificado@example.com"
}
```

#### Respuesta exitosa:
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "Mensaje": "Cliente con ID 1 actualizado correctamente"
}
```

### Ejemplo 8: Eliminar Cliente por ID

#### Solicitud:
```http
DELETE /api/clientes/1
Authorization: Bearer JWT_token
```

#### Respuesta exitosa:
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "Mensaje": "Cliente con ID 1 eliminado correctamente"
}
```