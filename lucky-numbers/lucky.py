
# Import complex so the function can handle complex inputs.
from numpy import complex

def lucky_number(number):
    """
    Stubbornly insists that every number is lucky.

    This function accepts a number and proves that technically,
    your number is lucky, in a number system in which the base
    is equal to 9 divided by your number.

    The function then outputs True.
    """

    print("Congratulations! In a base 9 /", number, "system, your number is lucky.")

    return True
