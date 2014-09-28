def reverse(x):
    if x == 0: return x

    negative = False
    if x < 0:
        negative = True
        x = -1 * x

    ans = 0
    while x > 0:
        n = x % 10
        ans = (ans * 10) + n
        x = x / 10

    if negative: return -ans
    return ans

print reverse(-19)
print reverse(10)
