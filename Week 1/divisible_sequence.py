#PYTHON 
n = int(input())
arr = []

for i in range(100, 1000):
    if i % n == 0:
        arr.append(i)

arr = ' '.join(map(str, arr))
print(arr)
