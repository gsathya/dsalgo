def add(ip1, ip2):
    len1 = len(ip1)
    len2 = len(ip2)
    
    if len1 > len2:
        diff = len1-len2
        ip2 = "0"*diff+ip2
    elif len2 > len1:
        diff = len2-len1
        ip1 = "0"*diff+ip1

    ans = []
    res = 0
    carry = 0
    pos = len(ip1)-1

    while pos > -1:
        if ip1[pos] == '0' and ip2[pos] == '0':
            res = carry
            carry = 0
        elif ip1[pos] == '1':
            if ip2[pos] == '0':
                if carry == 0:
                    res = 1
                elif carry == 1:
                    res = 0
            elif ip2[pos] == '1':
                if carry == 0:
                    res = 0
                elif carry == 1:
                    res = 1
                carry = 1
        elif ip2[pos] == '1':
            if ip1[pos] == '0':
                if carry == 0:
                    res = 1
                elif carry == 1:
                    res = 0
            elif ip1[pos] == '1':
                if carry == 0:
                    res = 0
                elif carry == 1:
                    res = 1
                carry = 1
        ans.append(res)
        pos -=1
        
    ans.append(carry)
    return ''.join([str(i) for i in reversed(ans)])

