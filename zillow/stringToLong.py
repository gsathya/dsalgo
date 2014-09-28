#!/usr/bin/env python

def convert(num):
    """Convert a number in string format to a long

    Keyword arguments:
    num -- number to be converted (string)

    Exception:
    raise ValueError - if no input is given
    raises TypeError - if input is not a string or has fractional part
    """

    if not num:
        raise ValueError("No input given")

    # return if number is already in long format
    if isinstance(num, long):
        return num

    if type(num) != str:
        raise TypeError("Input should be a string: %s" %(num))

    if '.' in num:
        raise TypeError("Input should not have any fractional part: %s" %(num))

    negative = False
    start_pos = 0

    # check if number is negative
    if num[0] == '-':
        negative = True
        start_pos = 1
    
    multiply = 10
    ans = 0
    
    for pos in range(start_pos, len(num)):
        # subtract from '0' to get normalize ascii and get the value
        ans = ans*multiply + ord(num[pos]) - ord('0')

    if negative:
        ans *= -1
        
    return ans
