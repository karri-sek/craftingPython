#Empty Tuple
my_tuple=()
print(my_tuple)

my_tuple = (1,2,3)
print(my_tuple)

my_tuple = (1, " Sdkhar", 3.4)
print(my_tuple)

my_tuple = ("sekhar", [3,4,5], (3,6,7))
print(my_tuple)


myTuple = 3 ,4 ,5 , "sekhar"
print(myTuple)

# un packing
a , b, c, d  = myTuple
print(a, b, c, d)

myTuple = ("hello",)
print(type(myTuple))

myTuple = "hello",
print(type(myTuple))

n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(n_tuple[1])
print(n_tuple[1][2])

# Negative indexing for accessing tuple elements
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_tuple[-1])
print(my_tuple[-4])