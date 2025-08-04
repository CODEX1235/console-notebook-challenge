# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.
from datetime import datetime
class Note:
    HIGH : str = "HIGH"
    MEDIUM : str = "MEDIUM"
    LOW: str = "LOW"

    def __init__(self,code:str,title:str,text:str,importance:str,create_datetime: datetime, tags : list):
        self.code = code
        self.title = title
        self.text = text
        self.importance = importance
        self.create_datetime = datetime.now()
        self.tags = list[str]

    def add_tag(self,tag:str):
        self.tags.append(tag)

    def __str__(self)->str:
        return f"Date: {self.create_datetime} , {self.title}: {self.text}"
















