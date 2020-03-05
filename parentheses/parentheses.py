
def remove_parens(x):

    # Initialize difference in left count and right count to zero.
    diff = 0

    # Initialize a variable to store the output string
    y = ''

    # Is it a left parenthesis? If not, it is a right.
    left = lambda char: char == '('

    # Iterate through the characters in the input string
    for i in range(len(x)):

        # If the character is a left parenthesis,
        if left(x[i]):

            # add one to the difference.
            diff += 1

            # If the difference is now 1, it is an outer parenthesis.
            if diff == 1:
                continue
            else:
                y += x[i] # Otherwise, add the parenthesis to the output.

        # If the character is a right parenthesis,
        else:

            # subtract one from the difference.
            diff -= 1

            # If the difference is now 0, it is an outer parenthesis.
            if diff == 0:
                continue
            else:
                y += x[i] # Otherwise, add the parenthesis to the output.

    return y