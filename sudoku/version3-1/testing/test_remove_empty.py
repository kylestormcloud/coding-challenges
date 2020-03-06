from sudoku import remove_empty

def test_remove_empty():

    # A test input representing a sudoku board
    test = [5, ' ', 4, 6, 7, 8, 9, 1, 2]

    # Call remove_empty on the test input
    no_empties = remove_empty(test)

    # Assert that there are no spaces in the resulting list
    assert ' ' not in no_empties

test_remove_empty()