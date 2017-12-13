# number 1: smallest of three
a=7
b=10
c=3
#variables set
if a<b and a<c:
    print "%d is the smallest of the three" %a
elif b<a and b<c:
    print "%d is the smallest of the three" %b
elif c<a and c<b:
    print "%d is the smallest of the three" %c
else:
    print "you're fucked"

#number 2: largest odd number

if a%2!=0: # (!=) means not equal to
    if a>c:
        print "%d is the greatest odd number"%a
elif c%2!=0:
    if c>a:
        print "%d is the greatest odd number"%c
else:
    print "There are no odd numbers"

#now try largest odd out of 3

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