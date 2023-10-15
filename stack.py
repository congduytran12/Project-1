#PYTHON 
stack = []

def push(value):
    stack.append(value)

def pop():
    if stack:
        return stack.pop()
    else:
        return "NULL"

while True:
    try:
        command = input()
        if command.startswith("PUSH"):
            i, value = command.split()
            push(int(value))
        elif command == "POP":
            result = pop()
            print(result)
    except EOFError:
        break
