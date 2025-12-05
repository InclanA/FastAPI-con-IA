from fastapi import APIRouter, Depends
from models.models import producto
from managers.producto_manager import productomanager
from managers.conexion import cursorxd

router = APIRouter(prefix="/productos", tags=["Productos"])
manager = productomanager()

@router.post("/")
def crear(producto: producto, cursor=Depends(cursorxd)):
    return manager.crear(producto, cursor)

@router.get("/{id_producto}")
def obtener(id_producto: int, cursor=Depends(cursorxd)):
    return manager.obtener(id_producto, cursor)

@router.put("/{id_producto}")
def actualizar(id_producto: int, producto: producto, cursor=Depends(cursorxd)):
    return manager.actualizar(id_producto, producto, cursor)

@router.delete("/{id_producto}")
def eliminar(id_producto: int, cursor=Depends(cursorxd)):
    return manager.eliminar(id_producto, cursor)
