import numpy as np
import json


class Board:
    def __init__(self,object_id,file__name,get_solved_or_unsolved): 
        self.object_id = object_id
        self.file_name = file__name
        self.board_flattened = None
        self.get_solved_or_unsolved = get_solved_or_unsolved # 1 for unsolve 0 for the solved puzzle

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
            
            board_matrix[i] = numbers
            

        return board_matrix





#TODO Make a func that finds the most best id for a new object


def add_board(board_string, solution_string, id, file_name, overwrite_or_not=False):
        if (board_string == None and solution_string == None):
            print("board_string or solution_string be equal to None")
            return
        
        
        if overwrite_or_not == True:
            object = {
                "id": id,
                "board": board_string,
                "solution": solution_string
            }

            with open(file_name) as file:
                records = json.load(file)

            for i, record in enumerate(records): #we use enumerate bc we need to index 
                if record["id"] == id:  
                    records[i] = object

            with open(file_name, "w") as file:
                json.dump(records, file, indent=4)

        else:
            # with open(file_name) as file:
            #     records = json.load(file)

            # id_counter = 0

            # for record in records:
            #     if "id" in record:
            #         id_counter += 1

            # id_counter += 1 #so the id is new 
            with open(file_name) as file:
                    records = json.load(file)

            object = {
                        "id": id,
                        "board": board_string,
                        "solution": solution_string
                    }
            
            records.append(object)

            with open(file_name, "w") as file:
                json.dump(records,file, indent=4)
            
        



# create a board so we can test other funcs
b1 = Board("3",r"data/easy.json",get_solved_or_unsolved=0)
board = b1.load()
BM1 = b1.convert_to_matrix()

