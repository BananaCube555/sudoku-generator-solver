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

            for num in curr_row:
                curr_row_without_zeros = []
                if num != 0:
                    curr_row_without_zeros.append(num)
            

            if len(curr_row_without_zeros) != len(set(curr_row_without_zeros)):
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
        valid_boxes = True

        for Row in range(3):
            
            for Colum in range(3):
                box = []

                for row in range(3):
                    for colum in range(3):
                        Rr = row + (Row * 3)
                        Cc = colum + (Colum * 3)

                        box.append(self.board_matrix[Rr, Cc])

                if len(box) != len(set(box)):
                    valid_boxes = False

        return valid_boxes


# test validation class
# from board import Board

# b1 = Board("2",r"data/easy.json",get_solved_or_unsolved=0)
# board = b1.load()
# BM1 = b1.convert_to_matrix()

# vb_BM1 = Validate_board(BM1)
# valid_length = vb_BM1.length_check()
# valid_rows = vb_BM1.row_check()
# valid_cols = vb_BM1.colum_check()
# valid_boxes = vb_BM1.box_check()


# print(valid_rows)
# print(valid_cols)
# print(valid_boxes)
