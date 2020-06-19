def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)

print(" Result of Factorial ", factorial(6))