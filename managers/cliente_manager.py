import psycopg
from models.models import cliente

class clientemanager:
    def crear(self, cliente: cliente, cursor: psycopg.Cursor):
        cursor.execute(
            """
            INSERT INTO cliente (nombre,apellido,email,telefono,direccion) VALUES (%s,%s,%s,%s,%s)
            """,
            (cliente.nombre,cliente.apellido,cliente.email,cliente.telefono,cliente.direccion)
        )
        return {"cliente creado"}

    def obtener(self, id_cliente: int, cursor: psycopg.Cursor):
        cursor.execute(
            "SELECT id, nombre,apellido,email,telefono,direccion FROM cliente WHERE id = %s",
            (id_cliente,)
        )
        return cursor.fetchone()

    def actualizar(self, id_cliente: int, cliente: cliente, cursor: psycopg.Cursor):
        cursor.execute(
           """UPDATE cliente SET nombre = %s, apellido = %s,email=%s,telefono=%s,direccion=%s 
           WHERE id = %s""",
            (cliente.nombre,cliente.apellido,cliente.email,cliente.telefono,cliente.direccion ,id_cliente)
        )
        return {"cliente actualizado"}

    def eliminar(self, id_cliente: int, cursor: psycopg.Cursor):
        cursor.execute(
            "DELETE FROM cliente WHERE id = %s",
            (id_cliente,)
        )
        return {"cliente eliminado"}
