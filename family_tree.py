#PYTHON 
family_tree = {}

def count_descendants(name):
    if name not in family_tree:
        return 0
    descendants = 0
    for child in family_tree[name]:
        descendants += 1 + count_descendants(child)
    return descendants

def count_generations(name):
    if name not in family_tree:
        return 0
    max_generation = 0
    for child in family_tree[name]:
        max_generation = max(max_generation, 1 + count_generations(child))
    return max_generation

while True:
    line = input().strip()
    if line == '***':
        break
    child, *rest = line.split()  
    parent = rest[0] if rest else None
    if parent:
        if parent not in family_tree:
            family_tree[parent] = []
        family_tree[parent].append(child)

try:
    while True:
        line = input().strip()
        if not line:
            continue
        cmd, *rest = line.split() 
        param = rest[0] if rest else None
        if cmd == "descendants" and param:
            print(count_descendants(param))
        elif cmd == "generation" and param:
            print(count_generations(param))
except EOFError:
    pass
