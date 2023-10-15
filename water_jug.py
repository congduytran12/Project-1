#PYTHON 
a, b, c = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def can_measure(a, b, c):
    if c > max(a, b) or c % gcd(a, b) != 0:
        return -1    
    visited = set()
    queue = [(0, 0, 0)]                 
    while queue:
        x, y, steps = queue.pop(0)
        if x == c or y == c:
            return steps
        if (x, y) in visited:
            continue
        visited.add((x, y))
        queue.append((a, y, steps + 1))
        queue.append((x, b, steps + 1))
        queue.append((0, y, steps + 1))
        queue.append((x, 0, steps + 1))
        pour = min(x, b - y)
        queue.append((x - pour, y + pour, steps + 1))
        pour = min(a - x, y)
        queue.append((x + pour, y - pour, steps + 1))
    return -1

print(can_measure(a, b, c))
