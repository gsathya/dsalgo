def braces(input_str):
    stack = []
    open_brackets = set(['(','{','['])
    mapping = {')':'(', '}':'{', ']':'['}

    for i in input_str:
        if i in open_brackets:
            stack.append(i)
        else:
            if len(stack) == 0:
                return False

            top = stack.pop()
            if mapping[i] != top:
                return False

    if len(stack) > 0:
        return False

    return True

print braces('()[]{}(([])){[()][]}')
print braces('())[]{}')
print braces('[(])')
