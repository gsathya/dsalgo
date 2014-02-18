import math

def sqrt(num):
    if num < 0:
        return -1
    if num == 0 or num == 1:
        return 1

    start = 0.0
    end = max(float(num), 1.0)
    
    precision = 0.0001

    while end > start:
        mid = (start+end)/2
        square = mid*mid

        if square - precision <= num <= square + precision:
            return mid
        elif square < num:
            start = mid
        else:
            end = mid

    return (start+end)/2


print sqrt(5)
print sqrt(0.25)
