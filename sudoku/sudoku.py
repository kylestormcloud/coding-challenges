from numpy import zeros, arange

def remove_empty(x):
    """
    Remove the space characters from a collection

    An empty square on the sudoku board is denoted
    with a string containing a single space.
    It is necessary that these empty squares be removed
    before the uniqueness of the values is verified.
    """

    # Filter out anything that is not an integer type.
    return list(filter(lambda n: type(n) == int, x))

def unique(x):
    """
    Check if the digits in a collection are unique.

    If a list contains unique values,
    then it will be the same length when typed as a set.
    """

    # Remove any space characters from the input.
    digits = remove_empty(x)

    # Uniqueness test: is the list's length equal to the set's length?
    return len(digits) == len(set(digits))

def check_rows(board):
    """Test each row for uniqueness."""

    for i in range(9):

        if not unique(board[i]):

            return False

    return True

def check_columns(board):
    """Test each column for uniqueness."""

    for j in range(9):

        if not unique(board[:][j]):

            return False

    return True

def check_boxes(board):
    """Test each box for uniqueness"""

    for l in range(0, 9, 3):

        for k in range(9):

            if k % 3 == 0:

                box = []

            boxrow = board[k][l:l+3]

            box.extend(boxrow)

            if len(box) == 9:
               
                if not unique(box):

                    return False

    return True

def check_board(board):
    """
    Verifies the validity of a sudoku board

    This is done by calling the functions to check
    the rows, columns, and boxes for duplicate values.

    This function accepts a list of lists representing a sudoku board 
    and returns a boolean value representing whether the board is valid.
    """

    return check_rows(board) and check_columns(board) and check_boxes(board)
