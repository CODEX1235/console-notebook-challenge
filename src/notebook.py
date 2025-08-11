
from datetime import datetime
from symtable import Class


class Note:
    HIGH : str = "HIGH"
    MEDIUM : str = "MEDIUM"
    LOW: str = "LOW"

    def __init__(self, code: int, title: str, text: str,importance: str):
        self.code = code
        self.title = title
        self.text = text
        self.importance = importance
        self.create_datetime: datetime = datetime.now()
        self.tags = list[str] = [ ]

    def add_tag(self,tag:str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self)->str:
        return f"Date: {self.create_datetime} , {self.title}: {self.text}"

class Notebook:
    def __init__(self):
        self.notes: list[Note] = []

    def add_note(self,title: str, text: str, importance: str) ->int:
        code : str = str(len(self.notes))+ 1
        note : Note = (code, title, text, importance)
        self.notes.append(note)
























