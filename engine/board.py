import numpy as np
import json


class Board:
    def __init__(self,object_id,file__name,get_solved_or_unsolved):
        self.object_id = object_id
        self.file_name = file__name
        self.board_flattened = None
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
            
            board_matrix[i] = numbers
            

        return board_matrix



class Validate_board:
    def __init__(self,board_matrix):
        self.board_matrix = board_matrix

    def length_check(self):
        valid_length = False
        len_rows = len(self.board_matrix[1])
        len_cols = len(self.board_matrix[0])
        board_len = len_rows * len_cols

        if board_len == 81:
            valid_length = True

        return valid_length


    def row_check(self):
            
        valid_rows = True
        for row in range(9):
            curr_row = []
            for col in range(9):
                curr_row.append(self.board_matrix[row,col])

            if len(curr_row) != len(set(curr_row)):
                valid_rows = False
                

        return valid_rows

    def colum_check(self):
        valid_colums = True

        for col in range(9):
            curr_col = []
            for row in range(9):
                curr_col.append(self.board_matrix[col,row])

        if len(curr_col) != len(set(curr_col)):
            valid_colums = False

        return valid_colums


    def box_check(self):
        pass


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
b1 = Board("2",r"data/easy.json",get_solved_or_unsolved=0)
board = b1.load()
BM1 = b1.convert_to_matrix()

# test validation class
vb_BM1 = Validate_board(BM1)
valid_length = vb_BM1.length_check()
valid_rows = vb_BM1.row_check()
valid_cols = vb_BM1.colum_check()


print(valid_rows)
print(valid_cols)
