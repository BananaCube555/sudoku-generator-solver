import numpy

from board import Board

def empty_cells_check(board_matrix, check_if_valid=False):
    empty_cells = 0

    for row in range(9):
        for col in range(9):
            if board_matrix[row,col] == 0:
                empty_cells += 1
    
    return empty_cells
    


b1 = Board("2",r"data/easy.json",get_solved_or_unsolved=1)
board = b1.load()
BM1 = b1.convert_to_matrix()

empty_cells = empty_cells_check(BM1)
