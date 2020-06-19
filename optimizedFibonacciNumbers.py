from functools import lru_cache

@lru_cache(maxsize=None)
def compute_fabonacci(n):
    print("Calculating F", "(", n, ")", sep="", end=",")
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return compute_fabonacci(n-1) + compute_fabonacci(n-2)

print(" fibnoacciNumber (6) ",compute_fabonacci(6))
