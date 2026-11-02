import numpy as np

from board import Board

def empty_cells_check(board_matrix, check_if_valid=False):
    naked_sngl_pos = []# append tuples for x,y pos
    empty_cells = 0

    for row in range(9):
        for col in range(9):
            if board_matrix[row,col] == 0:
                naked_sngl_pos.append((row,col))
                empty_cells += 1
    
    return empty_cells,naked_sngl_pos
    
#TODO:Make a func for each tech used to sovle a soduku ranging from easy - hard
#TODO:Naked single

def naked_single(matrix_board,positions):
    numbers_09 = [1,2,3,4,5,6,7,8,9]

    for pos in positions:
        p_row = []
        for col in range(9):
            p_row.append(matrix_board[pos[0], col])
    
            




b1 = Board("4",r"data/easy.json",get_solved_or_unsolved=1)
board = b1.load()
BM1 = b1.convert_to_matrix()

empty_cells, empty_naked_sngl = empty_cells_check(BM1)
a = naked_single(BM1,empty_naked_sngl)
print(a)
print(empty_cells) 
print(empty_naked_sngl)