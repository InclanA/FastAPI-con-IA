from fastapi import FastAPI
from routes.cliente_router import router as cliente_router
from routes.pedido_router import router as pedido_router
from routes.producto_router import router as producto_router

app = FastAPI(title="componentes de pc")

app.include_router(cliente_router)
app.include_router(pedido_router)
app.include_router(producto_router)

@app.get("/")
def inclan():
    return {"hola :v"}
