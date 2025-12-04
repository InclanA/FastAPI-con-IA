from fastapi import APIRouter, Depends
from models.models import cliente
from managers.cliente_manager import clientemanager
from managers.conexion import get_cursor

router = APIRouter(prefix="/clientes", tags=["Clientes"])
manager = clientemanager()

@router.post("/")
def crear(cliente: cliente, cursor=Depends(get_cursor)):
    return manager.crear(cliente, cursor)

@router.get("/{id_cliente}")
def obtener(id_cliente: int, cursor=Depends(get_cursor)):
    return manager.obtener(id_cliente, cursor)

@router.put("/{id_cliente}")
def actualizar(id_cliente: int, cliente: cliente, cursor=Depends(get_cursor)):
    return manager.actualizar(id_cliente, cliente, cursor)

@router.delete("/{id_cliente}")
def eliminar(id_cliente: int, cursor=Depends(get_cursor)):
    return manager.eliminar(id_cliente, cursor)
