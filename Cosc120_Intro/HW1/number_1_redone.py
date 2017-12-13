import numpy as np
from random import randint as ri
rand = np.zeros(3)
for i in range(3):
    rand[i] = ri(0,9)
print rand
a=rand[0]
b=rand[1]
c=rand[2]
if a%2 != 0:
    if a > b and a > c:
        print "%d is the largest odd number" %a
    elif b > a and a > c:
        if b%2 == 0:
            print "%d is the largest odd number" %a
    elif a > b and c > a:
        if c%2 == 0:
            print "%d is the largest odd number" %a
    elif b%2 == 0 and c%2 == 0:
        print "%d is the largest odd number" %a
