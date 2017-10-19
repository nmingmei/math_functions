#from itertools import combinations_with_replacement
#for c in combinations_with_replacement("TBL", 4):
#    print("".join(c))4


import math
x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))
if y == x:
    print(1)
elif y == 1:         # see georg's comment
    print(x)
elif y > x:          # will be executed only if y != 1 and y != x
    print(0)
else:                # will be executed only if y != 1 and y != x and x <= y
    a = math.factorial(x)
    b = math.factorial(y)
    c = math.factorial(x-y)  # that appears to be useful to get the correct result
    div = a // (b * c)
    print(div)  