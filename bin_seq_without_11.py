#PYTHON 
n = int(input())

def binary_sequence(n, current_sequence=""):
    if n == 0:
        print(current_sequence)
    else:
        if len(current_sequence) == 0 or current_sequence[-1] == "0":
            binary_sequence(n - 1, current_sequence + "0")
            binary_sequence(n - 1, current_sequence + "1")
        else:
            binary_sequence(n - 1, current_sequence + "0")

binary_sequence(n)
