from fastapi import FastAPI
from app.routers.produtos import router as produtos_router
app = FastAPI(
    title="API de Produtos",
    description="API REST com FastAPI, SQLAlchemy e MySQL",
    version="1.0.0")


app.include_router(produtos_router)



@app.get("/")
def inicio():
    return {"mensagem": "API de produtos" }