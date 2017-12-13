# Number 1

a=7
b=10
c=3

if a%2!=0:
    if a>c and a>b:
        print "%d is the greatest odd number" %a
    elif c>a and a>b:
        if c%2==0:
            print "%d is the greatest odd number" %a
    elif b>a and a>c:
        if b%2==0:
            print "%d is the greatest odd number" %a
elif b%2!=0:
    if b>a and b>c:
        print "%d is the greatest odd number" %b
    elif c>b and b>a:
        if c%2==0:
            print "%d is the greatest odd number" %b
    elif a>b and b>c:
        if a%2==0:
            print "%d is the greatest odd number" %b
elif c%2!=0:
    if c>a and c>b:
        print "%d is the greatest odd number" %c
    elif a>c and c>b:
        if a%2==0:
            print "%d is the greatest odd number" %c
    elif b>c and c>a:
        if b%2==0:
            print "%d is the greatest odd number" %c
else:
    print "There are no odd numbers"

# Number 2

if a%2!=0:
    while a>b and a>c:
        print "%d is greatest odd number" %a
elif b % 2 != 0:
    while b>a and b>c:
        print "%d is greatest odd number" % b
elif c%2 != 0:
    while c>a and c>b:
        print "%d is greatest odd number" % c
else:
    print "There are no odd numbers"

# Infinite Loop?
# Number 3
# ?

# Number 4

# s = '1.23, 2.4, 3.123'
# x = s[0:4]
# x = float(x)
# y = s[6:9]
# y = float(y)
# z = s[11:17]
# z = float(z)
# print "Sum of s is", x+y+z

#doesn't work but followed slicing notes
# this error message:  x = s[0,4]
# TypeError: string indices must be integers, not tuple

# Number 5

n = raw_input('Please input an integer to sum up')
i = 1
S = 0
n = int(n)
while i<=n:
    S = i + S
    i = i + 1
print 'The sum is', S

import numpy as np
v1 = np.zeros(100)
up = 1.0
for count in range(0,100):
   v1[count] = up
   up = up + 1
print v1
print sum(v1)

v2 = np.zeros(50)
v3 = np.zeros(50)
up = 1.0
while up <= 50.0:
    for count in range(0,50):
        v2[count] = up
        up = up + 1
    break
while up > 50.0 <= 100.0:
    for count in range(0,50):
        v3[count] = up
        up = up + 1
    break
print v2
print v3
print sum(v2 + v3)


