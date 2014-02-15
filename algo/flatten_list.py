def flatten_iteratively(ip):
    ans = []
    
    while len(ip) > 0:
        i = ip.pop()
        if type(i) == type([]):
            for item in i:
                ip.append(item)
        else:
            ans.append(i)

    ans = [i for i in reversed(ans)]
    return ans

def flatten_recursively(ip):
    ans = []
    
    for i in ip:
        if type(i) == type([]):
            for item in flatten_recursively(i):
                ans.append(item)
        else:
            ans.append(i)
    return ans
            
print flatten_iteratively([1, 2, [3, 4], [[[5]]], 6])
print flatten_recursively([1, 2, [3, 4], [[[5]]], 6])
