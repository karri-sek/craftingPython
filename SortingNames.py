import operator

names = ["Rishikesh", "aman", "Ajay", "Hemkesh", "sandeep", "Darshan", "Virendra", "Shwetabh"];
namesSorted = sorted(names, key=lambda name:name.lower());
print("Names Sorted ", namesSorted)

#Sorting dictinaries
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
sortedDic = sorted(xs.items(), key=lambda x:x[1])
print("Sorted dictonaries ", sortedDic)
sortedOperator = sorted(xs.items(), key=operator.itemgetter(1))
print(" Sorted using operator ", sortedOperator)