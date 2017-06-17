#Uses python2
s = raw_input()
def pairedParenthesis(s):
    stack = []
    for x in s:
        if x == '[' or x == '{' or x == '(':
            stack.append(x)
        else:
            if len(stack) == 0 : return False
            else:
                top = stack.pop()
                if top == '[' and x != ']' or top == '{' and x != '}' or top == '(' and x != ')':
                    return False
    return len(stack) == 0

print pairedParenthesis(s)
