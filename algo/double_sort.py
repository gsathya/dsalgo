# Given a 2 dimensional array, sort the arrays by a chosen column number.

arr = [[12, 'AAA'], [18, 'DDD'], [28, "CCC"], [58, "BBB"]]
col = 1

print sorted(arr, key=lambda x:x[col])
