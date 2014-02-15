def gen(n):
    s1 = ""
    s2 = ""

    for i in range(n):
        s1 += "("
        s2 += ")"

    _gen("", s1, s2)

def _gen(str, s1, s2):
    if len(s1) == 0:
        print str

    for i in range(1, len(s1)+1):
        temp = str + s1[:i] + s2[:i]
        _gen(temp, s1[i:], s2[i:])
        
gen(3)
