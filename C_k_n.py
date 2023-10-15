#PYTHON 
k, n = map(int, input().split())
mod = 10 ** 9 + 7

def mod_inverse(x):
    return pow(x, mod - 2, mod)

def C(k, n):
    fact_n = 1
    fact_k = 1
    fact_n_minus_k = 1
    for i in range(1, n + 1):
        fact_n = (fact_n * i) % mod
        if i == k:
            fact_k = fact_n
        if i == (n - k):
            fact_n_minus_k = fact_n
    return (fact_n * mod_inverse(fact_k) * mod_inverse(fact_n_minus_k)) % mod

print(C(k, n))
