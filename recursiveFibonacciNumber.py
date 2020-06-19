def fibnoacciNumber(n):
    print("Calculating F", "(", n, ")", sep="", end=",")
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
       return fibnoacciNumber(n-1) + fibnoacciNumber(n-2)

print(" fibnoacciNumber (5) ",fibnoacciNumber(6))