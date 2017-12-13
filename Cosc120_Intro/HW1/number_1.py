import numpy as np
from random import randint as ri
rand = np.zeros(3)
for i in range(3):
    rand[i] = ri(0,9)
print rand
a=rand[0]
b=rand[1]
c=rand[2]
# assigning variables
if a%2!=0: # checks if a is odd
    if a>c and a>b: # checks if a is greater than other variables
        print "%d is the greatest odd number" %a
    elif c>a and a>b: # if another variable is greater then then checks if greater variable is even
        if c%2==0:
            print "%d is the greatest odd number" %a
    elif b>a and a>c:
        if b%2==0:
            print "%d is the greatest odd number" %a
    elif b>a and c>a: # if both the other variables are greater then checks if they are both even
        if b%2==0:
            if c%2==0:
                print "%d is the only odd number, therefore it's the greatest" %a
    elif a==b and a>c: # checks if variable a is greater than one variable while being equal to the other variable
        print "%d and %d are the greatest odd numbers" %a %b
    elif a==c and a>b:
        print "%d and %d are the greatest odd numbers" %a %b
# the last two conditional functions above work out when I do a prototype in the console but when in the .py file
# it doesnt work, the else conditional won't even run
elif b%2!=0:
    if b>a and b>c:
        print "%d is the greatest odd number" %b
    elif c>b and b>a:
        if c%2==0:
            print "%d is the greatest odd number" %b
    elif a>b and b>c:
        if a%2==0:
            print "%d is the greatest odd number" %b
    elif a>b and c>b:
        if a % 2 == 0:
            if c % 2 == 0:
                print "%d is the only odd number, therefore it's the greatest" %b
elif c%2!=0:
    if c>a and c>b:
        print "%d is the greatest odd number" %c
    elif a>c and c>b:
        if a%2==0:
            print "%d is the greatest odd number" %c
    elif b>c and c>a:
        if b%2==0:
            print "%d is the greatest odd number" %c
    elif a>c and b>c:
        if b % 2 == 0:
            if a % 2 == 0:
                print "%d is the only odd number, therefore it's the greatest" %c
else:
    print "There are no odd numbers"
