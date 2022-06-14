# pylint: disable=missing-docstring
# $DELETE_BEGIN
VALID_SET = list(range(1, 10))

def valid_rows(grid):
    for row in grid:
        if sorted(row) != VALID_SET:
            return False
    return True

def valid_columns(grid):
    for j in range(0, 9):
        col = []
        for i in range(0, 9):
            col.append(grid[i][j])
        if sorted(col) != VALID_SET:
            return False
    return True

def valid_boxes(grid):
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            square = []
            for i in range(0, 3):
                i += box_row
                for j in range(0, 3):
                    j += box_col
                    square.append(grid[i][j])
            if sorted(square) != VALID_SET:
                return False
    return True
# $DELETE_END

def sudoku_validator(grid):
    # $CHALLENGIFY_BEGIN
    return valid_rows(grid) and valid_columns(grid) and valid_boxes(grid)
    # $CHALLENGIFY_END

print("hello world!")
grid = [
            [7,8,4,  1,5,9,  3,2,6],
            [5,3,9,  6,7,2,  8,4,1],
            [6,1,2,  4,3,8,  7,5,9],

            [9,2,8,  7,1,5,  4,6,3],
            [3,5,7,  8,4,6,  1,9,2],
            [4,6,1,  9,2,3,  5,8,7],

            [8,7,6,  3,9,4,  2,1,5],
            [2,4,3,  5,6,1,  9,7,8],
            [1,9,5,  2,8,7,  6,3,4]
        ]
print(sudoku_validator(grid))
