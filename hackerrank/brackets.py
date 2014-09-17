input_str = "[][(])"

def braces(input_str):
    stack = []
    open_brackets = set(['(','{','['])
    mapping = {')':'(', '}':'{', ']':'['}

    for i in input_str:
        if i in open_brackets:
            stack.append(i)
        else:
            if len(stack) == 0:
                return "NO"

            top = stack.pop()
            if mapping[i] != top:
                return "NO"

    if len(stack) > 0:
        return "NO"

    return "YES"

print braces(input_str)
