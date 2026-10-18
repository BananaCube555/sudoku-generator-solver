import numpy as np
import json

class Board:
    def __init__(self,object_id,file__name,get_solved_or_unsolved):
        self.object_id = object_id
        self.file_name = file__name
        self.board_flattened = get_solved_or_unsolved
        self.get_solved_or_unsolved = get_solved_or_unsolved # 1 for puzzle 0 for the solved puzzle

    def load(self):
        object_to_get = None
        if self.get_solved_or_unsolved == 1:
            object_to_get = "board"
        else:
            object_to_get = "solution"

        with open(self.file_name) as f:
            records = json.load(f)

        for record in records:
            if record["id"] == self.object_id:
                Loaded_board = record[object_to_get]
                self.board_flattened = Loaded_board
                return Loaded_board
            
    def convert_to_matrix(self):
        board_matrix = np.zeros((9, 9), dtype=int)
        brd_flt = self.board_flattened

        for i in range(9):
            start = i * 9
            end = start + 9
            row_chars = brd_flt[start:end]

            numbers = []
            for integer in row_chars:
                numbers.append(int(integer))

            board_matrix[i] = [int(c) for c in row_chars]

        return board_matrix


class Validate_board:
    def length_check(self):
        pass

    def row_check(self):
        pass

    def colum_check(self):
        pass

    def box_check(self):
        pass



def add_board(board_string, solution_string, id, file_name, overwrite_or_not=True):
        if (board_string == None and solution_string == None):
            print("board_string or solution_string be equal to None")

            return
        
        if overwrite_or_not == True:
            object = {
                "id": 1,
                "board": board_string,
                "solution": solution_string
            }

            with open(file_name) as file:
                records = json.load(file)

            for record in records:
                if record["id"] == id:
                    record = object
                        
                    


add_board("530070000600195000080000670800060003400803001700020006060000280000419005000080079",
          "524678912672195348198342567859761423426853791713924856961537284287419635345286179",
          2,r"data\easy.json")

b1 = Board("1",r"data/easy.json",get_solved_or_unsolved=0)
board = b1.load()
board_matrix = b1.convert_to_matrix()
