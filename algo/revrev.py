# http://problemotd.com/problem/reverse-reverse/

def rev(s):
    start = 0
    end = len(s) - 1
    s = list(s)
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    return ''.join(s)

def revrev(string, delim):
    string = string.split(delim)
    op = []
    for id, s in enumerate(string):
        if id % 2 != 0:
            op.append(rev(s))
        else:
            op.append(s)

    print str(delim).join(op)

revrev('hello world mom', ' ')
