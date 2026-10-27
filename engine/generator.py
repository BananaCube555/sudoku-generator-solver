import numpy as np

from board import Validate_board

class generate_board:
    def __init__(self,matrix_board=None):
        self.matrix_board = matrix_board

    def generate_solved(self): # Using the validate board class in engine\board.py script
        if self.matrix_board != None: 
            vb_BM1 = Validate_board(self.matrix_board)


        board_matrix = np.zeros((9,9))
        

        for row in range(9):
            curr_row = []
            
            
            for colum in range(9):
                random_int = np.random.randint(0, 10)

                if random_int not in curr_row:
                    curr_row.append(random_int)


                

    def generate_unsolved(self):
        pass 
