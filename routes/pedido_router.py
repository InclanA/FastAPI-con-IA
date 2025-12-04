from fastapi import APIRouter, Depends
from models.models import pedido
from managers.pedido_manager import pedidomanager
from managers.conexion import get_cursor

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])
manager = pedidomanager()

@router.post("/")
def crear(pedido: pedido, cursor=Depends(get_cursor)):
    return manager.crear(pedido, cursor)

@router.get("/{id}")
def obtener(id: int, cursor=Depends(get_cursor)):
    return manager.obtener(id, cursor)

@router.put("/{id}")
def actualizar(id: int, pedido: pedido, cursor=Depends(get_cursor)):
    return manager.actualizar(id, pedido, cursor)

@router.delete("/{id}")
def eliminar(id: int, cursor=Depends(get_cursor)):
    return manager.eliminar(id, cursor)
