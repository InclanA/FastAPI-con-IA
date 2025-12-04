import psycopg
from models.models import producto

class productomanager:
    def crear(self, producto: producto, cursor: psycopg.Cursor):
        cursor.execute(
            "INSERT INTO producto (nombre, marca, precio, cantidad) VALUES (%s, %s, %s, %s)",
            (producto.nombre, producto.marca, producto.precio, producto.cantidad)
        )
        return {"Producto creado"}

    def obtener(self, id: int, cursor: psycopg.Cursor):
        cursor.execute(
            "SELECT id, nombre, marca, precio, cantidad FROM producto WHERE id = %s",
            (id,)
        )
        return cursor.fetchone()

    def actualizar(self, id: int, producto: producto, cursor: psycopg.Cursor):
        cursor.execute(
            "UPDATE producto SET nombre = %s, marca = %s, precio = %s, cantidad = %s WHERE id = %s",
            (producto.nombre, producto.marca, producto.precio, producto.cantidad, id)
        )
        return {"Producto actualizado"}

    def eliminar(self, id: int, cursor: psycopg.Cursor):
        cursor.execute(
            "DELETE FROM producto WHERE id = %s",
            (id,)
        )
        return {"Producto eliminado"}
