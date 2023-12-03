import re
from functools import reduce

def generate_boards(engine_schematic):
    with open(engine_schematic, 'r') as f:
        engin_board = []
        ref_board = []
        for line in f:
            items = list(line.strip())
            engin_board.append(items)
            ref_board.append([0]*len(items))
    
    for irow,row in enumerate(engin_board):
        for icol,col in enumerate(row):
            if not col.isnumeric() and col != '.':
                ref_board[irow][icol] = 1

    return engin_board, ref_board

def print_board(board):
    for row in board:
        print(row)

def tag_adjacent_cell(board, irow, icol):
    if board[irow][icol] != 1:
        return
    
    cells_to_tag = ((-1,-1), (-1,0), (-1,1),
                    (0,-1) ,         (0,1) ,
                    (1,-1)  , (1,0) , (1,1))

    for check_cell in cells_to_tag:
        ccr = check_cell_row = irow + check_cell[0]
        ccc = check_cell_col = icol + check_cell[1]

        if ccr < 0 or ccc < 0:
            continue
        elif ccr >= len(board) or ccc >= len(board[0]):
            continue
        else:
            if board[ccr][ccc] != 1:
                board[ccr][ccc]=2


def tag_adjacent_cells(board):
    for irow,row in enumerate(board):
        for icol,col in enumerate(row):
            if col == 1:
                tag_adjacent_cell(board, irow, icol)

def not_symbol(board, irow, iicol):
    return board[irow][iicol] != 1

def not_dot(board, irow, iicol):
    return board[irow][iicol] != '.'

def tag_number(engin_board, ref_board, irow, icol):
    if engin_board[irow][icol].isnumeric():
        iicol = icol
        while iicol>=0 and not_symbol(ref_board, irow, iicol) and not_dot(engin_board, irow, iicol):
            if engin_board[irow][iicol].isnumeric():
                ref_board[irow][iicol]=3
                iicol-=1
                
        iicol = icol    
        while iicol<len(engin_board) and not_symbol(ref_board, irow, iicol) and not_dot(engin_board, irow, iicol):
            if engin_board[irow][iicol].isnumeric():
                ref_board[irow][iicol]=3
                iicol+=1

def tag_begining_of_numbers(engin_board, ref_board):
    for irow,row in enumerate(ref_board):
        for icol,col in enumerate(row):
            if ref_board[irow][icol] == 2:
                tag_number(engin_board, ref_board, irow, icol)


def extract_engine_numbers(engin_board, ref_board):
    for irow,row in enumerate(ref_board):
        for icol,col in enumerate(row):
            if ref_board[irow][icol]==3:
                ref_board[irow][icol]=engin_board[irow][icol]
            else:
                ref_board[irow][icol]=' '
    
    all_engine_numbers=[]
    for row in ref_board:
        line = ''.join(row)
        all_engine_numbers+= [int(x) for x in line.split()]
    return all_engine_numbers

def calc_engine_part(engine_schematic):
    engin_board, ref_board =  generate_boards(engine_schematic)
    tag_adjacent_cells(ref_board)
    tag_begining_of_numbers(engin_board, ref_board)
    engine_parts_numbers = extract_engine_numbers(engin_board, ref_board)
    print(sum(engine_parts_numbers))
    
if __name__ == "__main__":
    pass