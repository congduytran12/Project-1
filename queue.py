#PYTHON 
class Queue:
    def __init__(self):
        self.queue = []

    def push(self, value):
        self.queue.append(value)

    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        return None

queue = Queue()
while True:
    try:
        command = input().strip()
        if command == '#':
            break
        elif command.startswith("PUSH"):
            i, value = command.split()
            value = int(value)
            queue.push(value)
        elif command == "POP":
            result = queue.pop()
            if result is not None:
                print(result)
            else:
                print("NULL")
    except EOFError:
        break
