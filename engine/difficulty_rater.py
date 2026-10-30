import numpy

from board import Board

def rater(board_matrix, check_if_valid=False):
    empty_cells = 0


    #Rate based on techniques needed to solve
    #Number of unsolved cells


b1 = Board("2",r"data/easy.json",get_solved_or_unsolved=0)
board = b1.load()
BM1 = b1.convert_to_matrix()

rater(BM1)