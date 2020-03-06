from sudoku import check_columns

def test_check_columns():
    """A test for the check_columns function."""

    # A test input representing a sudoku board whose columns are valid.
    valid = [[5, ' ', 4, 6, 7, 8, 9, 1, 2],
            [6, ' ', 2, 1, 9, 5, 3, 4, 8],
            [1,   9, 8, 3, 4, 2, 5, 6, 7],
            [8,   5, 9, 7, 6, 1, 4, 2, 3],
            [4,   2, 6, 8, 5, 3, 7, 9, 1],
            [7,   1, 3, 9, 2, 4, 8, 5, 6],
            [9,   6, 1, 5, 3, 7, 2, 8, 4],
            [2,   8, 7, 4, 1, 9, 6, 3, 5],
            [3,   4, 5, 2, 8, 6, 1, 7, 9]]

    # check_columns should return True
    assert check_columns(valid)

    # A test input representing a sudoku board whose columns are invalid.
    invalid = [[2, ' ', 4, 6, 7, 8, 9, 1, 2],
               [6, ' ', 2, 1, 9, 5, 3, 4, 8],
               [1,   9, 8, 3, 4, 2, 5, 6, 7],
               [8,   5, 9, 7, 6, 1, 4, 2, 3],
               [4,   2, 6, 8, 5, 3, 7, 9, 1],
               [7,   1, 3, 9, 2, 4, 8, 5, 6],
               [9,   6, 1, 5, 3, 7, 2, 8, 4],
               [2,   8, 7, 4, 1, 9, 6, 3, 5],
               [3,   4, 5, 2, 8, 6, 1, 7, 9]]

    # check_columns should return False
    assert not check_columns(invalid)