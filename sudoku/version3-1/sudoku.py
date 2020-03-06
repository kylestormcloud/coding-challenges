"""
Kyle Cloud
Sudoku Board Checker
Coding Challenge for March 2, 2020
Last Update: March 3, 2020
"""

def check_size(board):
    """
    Verifies that an input contains 9 lists each having 9 values.

    A valid sudoku board has 81 squares: 9 rows and 9 columns.
    It is necessary before any other validation tests are conducted
    to verify that the input is of the right size.

    This function accepts a list of lists and returns False if
    there are more or fewer that nine lists in the list of lists,
    or if any list in the list of lists contains more or fewer
    than nine values.
    Otherwise, the function returns True.
    """

    # If there are not nine rows,
    if len(board) != 9:

        # the input is not valid.
        return False

    # Iterate through the list of rows.
    for row in board:

        # If there are not nine elements in every row,
        if len(row) != 9:

            # the input is not valid.
            return False

    # If the input passes these tests, it is of valid size.
    return True

def remove_empty(row):
    """
    Remove the space characters from a collection

    An empty square on the sudoku board is denoted
    with a string containing a single space.
    It is necessary that these empty squares be removed
    before the uniqueness of the values is verified.
    """

    # Filter out anything that is not an integer type.
    return list(filter(lambda n: isinstance(n, int), row))

def unique(row):
    """
    Check if the digits in a collection are unique.

    If a list contains unique values,
    then it will be the same length when typed as a set.
    """

    # Remove any space characters from the input.
    digits = remove_empty(row)

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

    for col_num in range(9):

        column = []

        for row_num in range(9):

            column.append(board[row_num][col_num])

        if not unique(column):

            return False

    return True

def check_boxes(board):
    """Test each box for uniqueness"""

    for column_start in range(0, 9, 3):

        for row_pointer in range(9):

            if row_pointer % 3 == 0:

                box = []

            box_row = board[row_pointer][column_start:column_start+3]

            box.extend(box_row)

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

    # Is the input a list of 9 lists each containing 9 elements?
    if not check_size(board):

        # If not, the board is invalid.
        return False

    # Are the digits in each row unique?
    if not check_rows(board):

        # If not, the board is invalid.
        return False

    # Are the digits in each column unique?
    if not check_columns(board):

        # If not, the board is invalid.
        return False

    # Are the digits in each box unique?
    if not check_boxes(board):

        # If not, the board is invalid.
        return False

    # If the board passes the above tests, it is deemed valid.
    return True
