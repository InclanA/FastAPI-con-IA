import psycopg
from models.models import pedido

class pedidomanager:
    def crear(self, pedido: pedido, cursor: psycopg.Cursor):
        cursor.execute(
            "INSERT INTO pedido (cliente_id, producto_id, cantidad, estado) VALUES (%s, %s, %s, %s)",
            (pedido.cliente_id, pedido.producto_id, pedido.cantidad, pedido.estado)
        )
        return {"Pedido creado"}

    def obtener(self, id: int, cursor: psycopg.Cursor):
        cursor.execute(
            "SELECT id, cliente_id, producto_id, cantidad, estado FROM pedido WHERE id = %s",
            (id,)
        )
        return cursor.fetchone()

    def actualizar(self, id: int, pedido: pedido, cursor: psycopg.Cursor):
        cursor.execute(
            "UPDATE pedido SET cliente_id = %s, producto_id = %s, cantidad = %s, estado = %s WHERE id = %s",
            (pedido.cliente_id, pedido.producto_id, pedido.cantidad, pedido.estado, id)
        )
        return {"Pedido actualizado"}

    def eliminar(self, id: int, cursor: psycopg.Cursor):
        cursor.execute(
            "DELETE FROM pedido WHERE id = %s",
            (id,)
        )
        return {"Pedido eliminado"}
