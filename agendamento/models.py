from pydantic import BaseModel
from datetime import date

class Compromisso(BaseModel):
    titulo: str
    descricao: str = ""
    contato: str
    data: date
