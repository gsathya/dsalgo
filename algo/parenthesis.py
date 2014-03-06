output = []

def printParenthis(n):
    global output
    output = [0]*(2*n)
    _print(0,n ,0 ,0)

def _print(pos, n, open, close):
    global output
    if close == n:
        print ''.join(output)
        return
        
    if open > close:
        output[pos] = '}'
        _print(pos+1, n, open, close+1)
        
    if open < n:
        output[pos] = '{'
        _print(pos+1, n, open+1, close)

printParenthis(2)
