x , y , z = 0, 1, 0
if x == 1 or y == 1 or z == 1:
    print("passed")

if x == 1 or y ==1 or z == 1: 
    print("passed")
else:
    print("fail")

if 1 in (x, y, z):
    print("1 is present in either x , y , z")

if x or y or z:
    print('passed')

if any((x, y, z)):
    print("passed")



x , y , z = 0, 0, 0
if x == 1 or y == 1 or z == 1:
    print("2.passed")

if x == 1 or y ==1 or z == 1: 
    print("2.passed")
else:
    print("2.fail")

if 1 in (x, y, z):
    print("2.1 is present in either x , y , z")

if x or y or z:
    print('2.passed')

if any((x, y, z)):
    print("2.passed")