#https://www.hackerrank.com/challenges/collections-counter/problem
from collections import Counter
noOfShoes = int(input("Enter no of shoes:"))
print("No of shoes:", noOfShoes)
inputShoeSizes = input("Enter shoe sizes:")
shoeSizes = Counter(map(int,inputShoeSizes.split()))
noOfCustomers = int(input("Enter no of customers:"))

totalRevenue=0
for _ in range(noOfCustomers):
    size, price = map(int,input().split())
    if shoeSizes[size]:
        totalRevenue += price
        shoeSizes[size] -= 1
print ("total Revenue", totalRevenue)
