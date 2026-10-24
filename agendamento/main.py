
from fastapi import FastAPI, HTTPException
from database import conectar
from models import Compromisso

app = FastAPI()


@app.post("/compromissos")
def criar_compromisso(compromisso: Compromisso):
    banco = conectar()
    cursor = banco.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO compromissos
            (titulo, descricao, contato, data)
            VALUES (%s, %s, %s, %s)
            """,
            (
                compromisso.titulo,
                compromisso.descricao,
                compromisso.contato,
                compromisso.data
            )
        )

        banco.commit()

        return {
            "id": cursor.lastrowid,
            "mensagem": "Compromisso cadastrado"
        }
    finally:
        cursor.close()
        banco.close()


@app.get("/compromissos")
def listar_compromissos():
    banco = conectar()
    cursor = banco.cursor(dictionary=True)

    try:
        cursor.execute(
            "SELECT * FROM compromissos ORDER BY data"
        )
        return cursor.fetchall()
    finally:
        cursor.close()
        banco.close()


@app.get("/compromissos/hoje")
def compromissos_hoje():
    banco = conectar()
    cursor = banco.cursor(dictionary=True)

    try:
        cursor.execute(
            "SELECT * FROM compromissos WHERE data = CURDATE()"
        )
        return cursor.fetchall()
    finally:
        cursor.close()
        banco.close()


@app.delete("/compromissos/{id_compromisso}")
def excluir_compromisso(id_compromisso: int):
    banco = conectar()
    cursor = banco.cursor()

    try:
        cursor.execute(
            "DELETE FROM compromissos WHERE id = %s",
            (id_compromisso,)
        )

        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail="Compromisso não encontrado"
            )

        banco.commit()

        return {"mensagem": "Compromisso excluído"}
    finally:
        cursor.close()
        banco.close()
