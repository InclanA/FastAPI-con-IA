#models/models.py
from pydantic import BaseModel

class cliente(BaseModel):
    nombre: str
    apellido: str
    email: str
    telefono: str
    direccion: str

class producto(BaseModel):
    nombre: str
    marca: str
    precio: float
    cantidad: int
    
class pedido(BaseModel):
    cliente_id: int
    producto_id: int
    cantidad: int
    estado: str

