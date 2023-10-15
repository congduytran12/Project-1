#PYTHON 
n = int(input())

def binary_sequence(n, current_sequence=""):
    if n == 0:
        print(current_sequence)
    else:
        binary_sequence(n - 1, current_sequence + "0")
        binary_sequence(n - 1, current_sequence + "1")

binary_sequence(n)
