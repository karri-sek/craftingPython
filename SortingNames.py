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

# assert in python

def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <=product['price']
    return price

shoes = {'name': 'reebok', 'price': 1400}

print(" discounted price",apply_discount(shoes, .70));