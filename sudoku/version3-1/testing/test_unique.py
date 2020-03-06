from sudoku import unique

def test_unique():

    # A test input representing a row, column, or box
    test = [5, ' ', 4, 6, 7, 8, 9, 1, 2]

    assert(unique(test))