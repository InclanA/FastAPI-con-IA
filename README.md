# API componentes - FastAPI + POO + IA


![](foto/fondoxd.jpg)


# Descripción general del proyecto.
esta es una  api hecho co n Python FastAPI Postgres sirve para manejar clientes, productos y pedidos Permite crear, ver, actualizar y borrar datos de manera rápida

# Endpoints

### Clientes
**POST /clientes/**  Crear un cliente  
**GET /clientes/{id}**  Obtener datos de un cliente  
**PUT /clientes/{id}**  Actualizar un cliente  
**DELETE /clientes/{id}** Eliminar un cliente  

### Productos
**POST /productos/** Crear un producto  
**GET /productos/{id}**  Obtener un producto  
**PUT /productos/{id}** Actualizar un producto  
**DELETE /productos/{id}** Eliminar un producto  
### Pedidos
**POST /pedidos/** rear un pedido  
**GET /pedidos/{id}**  Obtener un pedido  
**PUT /pedidos/{id}**  Actualizar un pedido  
**DELETE /pedidos/{id}** Eliminar un pedido  

## Estructura del proyecto

La estructura real del proyecto

```
FASTAPI-IA/
│
├── foto/
│   └── foto.png
│
├── managers/
│   ├── cliente_manager.py
│   ├── conexion.py
│   ├── pedido_manager.py
│   └── producto_manager.py
│
├── models/
│   └── models.py
│
├── routes/
│   ├── cliente_router.py
│   ├── pedido_router.py
│   └── producto_router.py
│
├── .env
├── .gitignore
├── main.py
├── README.md
├── requirements.txt
└── vercel.json
```


## Ejemplos de uso

```
Crear un cliente
{
  "nombre": "axel",
  "apellido": "aguiñar",
  "email": "judw34dsf@gmail.com",
  "telefono": "2215554444",
  "direccion": "Calle 10 Nº 123"
}
Crear un producto
{
  "nombre": "Mouse Gamer",
  "marca": "Redragon",
  "precio": 199993435344359,
  "cantidad": 5
}
Crear un pedido
{
  "cliente_id": 1,
  "producto_id": 2,
  "cantidad": 1,
  "estado": "pendiente"
}
```
