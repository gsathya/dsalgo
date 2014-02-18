def atof(ip):
    negative = False
    i = 0
    
    if ip[0] == '-':
        negative = True
        i = 1

    
    multiply = 10
    ans = 0.0
    dec = 0
    
    while i < len(ip):
        if ip[i] == '.':
            dec = len(ip) - i - 1
        else:
            ans = ans*multiply + ord(ip[i]) - ord('0')
        i +=1

    if negative:
        ans *= -1
        
    for i in range(dec):
        ans = ans/10    

    return ans

print atof("54.22")
print atof("0.22")
print atof("54")
print atof("-54.22")
