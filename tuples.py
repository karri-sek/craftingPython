
# Advantages of Tuple over List
# Since tuples are quite similar to lists, both of them are used in similar situations. However, there are certain advantages of implementing a tuple over a list. Below listed are some of the main advantages:

# We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
# Since tuples are immutable, iterating through a tuple is faster than with list. So there is a slight performance boost.
# Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
# If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.
# Empty Tuple
my_tuple = ()
print(my_tuple)

my_tuple = (1, 2, 3)
print(my_tuple)

my_tuple = (1, " Sdkhar", 3.4)
print(my_tuple)

my_tuple = ("sekhar", [3, 4, 5], (3, 6, 7))
print(my_tuple)


myTuple = 3, 4, 5, "sekhar"
print(myTuple)

# un packing
a, b, c, d = myTuple
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

# Accessing tuple elements using slicing
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

print(my_tuple[1:5])
# from 0 to 3 remember 4 is exclusive here
print(my_tuple[:4])
# here 4 is inclusive
print(my_tuple[4:])

print("from zero -2 means i", my_tuple[:-2])

print("from back ward", my_tuple[-2:])

print("complete ", my_tuple[:])

print(" last element ", my_tuple[-1])

# Changing tuple values
my_tuple = (4, 2, 3, [6, 5])
# we cannot assign the values in the tuple they are immutable
# my_tuple[0]=6
# but if the element itself is mutable we can change
my_tuple[3][0] = 9
print(" after change ", my_tuple)

tuple1 = 1, 2
tuple2 = 3, 4
sumTuple = tuple1 + tuple2
print(sumTuple)

tuple3 = (1, 2) * 4
print(tuple3)

print(2 in tuple1)

print(5 not in tuple2)

print(5 in tuple2)
