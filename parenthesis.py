#PYTHON 
input_str = input()

def match(a, b):
    if a == '(' and b == ')':
        return 1
    if a == '[' and b == ']':
        return 1
    if a == '{' and b == '}':
        return 1
    return 0

def check_parenthesis(input_str):
    stack = []
    for i in input_str:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
        else:
            if len(stack) == 0:
                return 0
            else:
                c = stack.pop()
                if not match(c, i):
                    return 0
    return 1 if len(stack) == 0 else 0

print(check_parenthesis(input_str))
