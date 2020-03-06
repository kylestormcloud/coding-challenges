# Kyle Cloud
# March 5, 2020
# Testing module for check_size


from sudoku import check_size
from random import sample


def test_9x9():
    """
    Checks to ensure that the check_size function return True for 9x9 boards.

    This function creates 2000 random 9x9 sudoku boards
    and prints Passed or Failed for each, depending on whether
    the check_size function returns True or False respectively.
    """
    
    digit_list = list(range(1, 10))
    space_list = [' '] * 9
    big_list = digit_list + space_list

    # Create 2000 correctly sized boards.
    # For each board,
    for i in range(2000):

        # start with an empty list.
        board = []

        # Give each board 9 rows of 9.
        for j in range(9):
            i, j =  i, j
            board.append(sample(big_list, 9))

        assert check_size(board)

def test_9x8():
    """
    check_size should return False for boards with too few columns.

    This function creates 2000 random 9x8 sudoku boards one at a time,
    calls the check_size function on each board,
    and asserts that the check_size function returns False.
    """
    
    # Create a list from which to sample
    # Each cell could be empty or contain a digit 1 through 9.
    digit_list = list(range(1, 10))      # Digits 1 through 9
    space_list = [' '] * 9               # 9 spaces
    big_list = digit_list + space_list  

    # Create 2000 boards with too few columns
    for i in range(2000):

        # start with an empty list.
        board = []

        # Give each board 9 rows of 8.
        for j in range(9):
            i, j = i, j
            board.append(sample(big_list, 8))

        # check_size should return False
        assert not check_size(board)

def test_8x9():
    """
    check_size should return False for boards with too few rows.

    This function creates 2000 random 8x9 sudoku boards one at a time,
    calls the check_size function on each board,
    and asserts that the check_size function returns False.
    """
    
    # Create a list from which to sample
    # Each cell could be empty or contain a digit 1 through 9.
    digit_list = list(range(1, 10))      # Digits 1 through 9
    space_list = [' '] * 9               # 9 spaces
    big_list = digit_list + space_list  

    # Create 2000 boards with too few rows
    for i in range(2000):

        # start with empty board
        board = []

        # Give each board 8 rows of 9.
        for j in range(8):
            i, j = i, j
            board.append(sample(big_list, 9))

        # check_size should return False
        assert not check_size(board)

def test_9x10():
    """
    check_size should return False for boards with too many columns.

    This function creates 2000 random 9x10 sudoku boards one at a time,
    calls the check_size function on each board,
    and asserts that the check_size function returns False.
    """
    
    # Create a list from which to sample
    # Each cell could be empty or contain a digit 1 through 9.
    digit_list = list(range(1, 10))      # Digits 1 through 9
    space_list = [' '] * 9               # 9 spaces
    big_list = digit_list + space_list  

    # Create 2000 boards with too few columns
    for i in range(2000):

        # start with an empty list.
        board = []

        # Give each board 9 rows of 8.
        for j in range(9):
            i, j = i, j
            board.append(sample(big_list, 10))

        # check_size should return False
        assert not check_size(board)

def test_10x9():
    """
    The check_size function should return False for boards with too many rows.

    This function creates 2000 random 10x9 sudoku boards one at a time,
    calls the check_size function on each board,
    and asserts that the check_size function returns False.
    """
    
    # Create a list from which to sample
    # Each cell could be empty or contain a digit 1 through 9.
    digit_list = list(range(1, 10))      # Digits 1 through 9
    space_list = [' '] * 9               # 9 spaces
    big_list = digit_list + space_list  

    # Create 2000 boards with too few rows
    for i in range(2000):

        # start with empty board
        board = []

        # Give each board 8 rows of 9.
        for j in range(10):
            i, j = i, j
            board.append(sample(big_list, 9))

        # check_size should return False
        assert not check_size(board)
