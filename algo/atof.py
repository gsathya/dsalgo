def atof(ip):
    negative = False
    start_pos = 0
    
    if ip[0] == '-':
        negative = True
        start_pos = 1
    
    multiply = 10
    ans = 0.0
    decimal_place = 0
    
    for pos in range(start_pos, len(ip)):
        if ip[pos] == '.':
            decimal_place = len(ip) - pos - 1
        else:
            ans = ans*multiply + ord(ip[pos]) - ord('0')

    if negative:
        ans *= -1
        
    for i in range(decimal_place):
        ans = ans/10    

    return ans

print atof("54.22")
print atof("0.22")
print atof("54")
print atof("-54.22")
