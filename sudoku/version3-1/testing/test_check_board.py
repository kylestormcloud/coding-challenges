"""Module for the test_check_board function"""

from sudoku import check_board

def test_check_board():
    """Tests the check_board function."""

    # A test input representing a valid sudoku board
    valid = [[5, ' ', 4, 6, 7, 8, 9, 1, 2],
             [6, ' ', 2, 1, 9, 5, 3, 4, 8],
             [1, 9, 8, 3, 4, 2, 5, 6, 7],
             [8, 5, 9, 7, 6, 1, 4, 2, 3],
             [4, 2, 6, 8, 5, 3, 7, 9, 1],
             [7, 1, 3, 9, 2, 4, 8, 5, 6],
             [9, 6, 1, 5, 3, 7, 2, 8, 4],
             [2, 8, 7, 4, 1, 9, 6, 3, 5],
             [3, 4, 5, 2, 8, 6, 1, 7, 9]]

    # check_board should return True
    assert check_board(valid)

    # A test input representing a board of invalid size
    invalid_size = [[5, ' ', 4, 6, 7, 8, 9, 1, 2],
                    [6, ' ', 2, 1, 9, 5, 3, 4, 8],
                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5]]

    # check_board should return False
    assert not check_board(invalid_size)

    # A test input representing a sudoku board whose rows are invalid.
    invalid_rows = [[2, ' ', 4, 6, 7, 8, 9, 1, 2],
                    [6, ' ', ' ', 1, 9, 5, 3, 4, 8],
                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [' ', 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9]]

    # check_board should return False
    assert not check_board(invalid_rows)

    # A test input representing a sudoku board whose columns are invalid.
    invalid_columns = [[2, ' ', 4, 6, 7, 8, 9, 1, ' '],
                       [6, ' ', ' ', 1, 9, 5, 3, 4, 8],
                       [1, 9, 8, 3, 4, 2, 5, 6, 7],
                       [8, 5, 9, 7, 6, 1, 4, 2, 3],
                       [4, 2, 6, 8, 5, 3, 7, 9, 1],
                       [7, 1, 3, 9, 2, 4, 8, 5, 6],
                       [9, 6, 1, 5, 3, 7, 2, 8, 4],
                       [2, 8, 7, 4, 1, 9, 6, 3, 5],
                       [3, 4, 5, 2, 8, 6, 1, 7, 9]]

    # check_board should return False
    assert not check_board(invalid_columns)

    # A test input representing a sudoku board whose boxes are invalid.
    invalid_boxes = [[2, ' ', 4, 6, 7, 8, 9, 1, ' '],
                     [6, ' ', 2, 1, 9, 5, 3, 4, 8],
                     [1, 9, 8, 3, 4, 2, 5, 6, 7],
                     [8, 5, 9, 7, 6, 1, 4, 2, 3],
                     [4, 2, 6, 8, 5, 3, 7, 9, 1],
                     [7, 1, 3, 9, 2, 4, 8, 5, 6],
                     [9, 6, 1, 5, 3, 7, 2, 8, 4],
                     [' ', 8, 7, 4, 1, 9, 6, 3, 5],
                     [3, 4, 5, 2, 8, 6, 1, 7, 9]]

    # check_board should return False
    assert not check_board(invalid_boxes)
