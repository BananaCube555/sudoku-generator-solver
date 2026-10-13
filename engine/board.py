import numpy as np
import json

class Board:
    def __init__(self,object_id,file__name):
        self.object_id = object_id
        self.file_name = file__name

    def load(self):
        with open(self.file_name) as f:
            records = json.load(f)
        for record in records:
            if record["id"] == self.object_id:
                board = record["board"]
                return board
    

b1 = Board("easy-1",r"data/easy.json")
board = b1.load()
print(board)