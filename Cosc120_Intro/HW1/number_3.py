import numpy as np
from random import randint as ri
N = raw_input('Input amount of trials:')
N = int(N)
# when I input 10000000 my console says that there are too many outputs to compute. But if I choose a smaller number
# ie. 100, it works
numbers = np.zeros(3) # creates vector to fill with random numbers
x = np.zeros(N) # creates vector to store value of every loop
for i in range(N): # does the loop N amount of times
    for yo in range(3):
        numbers[yo] = ri(0, 9) # fills in vector with random numbers from 1 to 9
    op1 = 0 # create a variable to store output of script 1
    op2 = 0 # create a variable to store output of script 2
    a = numbers[0] #assigns numbers from vector into appropriate variables for script 1
    b = numbers[1]
    c = numbers[2]
    snumbers = sorted(numbers)  # makes another vector with the same elements as first one but in order from smallest to greatest
    flag = 0  # index for a condition
    if a % 2 != 0:  # checks if a is odd
        if a > c and a > b:  # checks if a is greater than other variables
            #print "%d is the greatest odd number" % a
            op1 = a #stores value into op1 if a is greatest 0dd
        elif c > a and a > b:  # if another variable is greater then then checks if greater variable is even
            if c % 2 == 0:
                #print "%d is the greatest odd number" % a
                op1 = a
        elif b > a and a > c:
            if b % 2 == 0:
                #print "%d is the greatest odd number" % a
                op1 = a
        elif b > a and c > a:  # if both the other variables are greater then checks if they are both even
            if b % 2 == 0:
                if c % 2 == 0:
                    #print "%d is the only odd number, therefore it's the greatest" % a
                    op1 = a
        elif a == b and a > c:  # checks if variable a is greater than one variable while being equal to the other variable
            #print "%d and %d are the greatest odd numbers" % a % b
            op1 = a
        elif a == c and a > b:
            #print "%d and %d are the greatest odd numbers" % a % b
            op1 = a
    # the last two conditional functions above work out when I do a prototype in the console
    # but when in the .py file it doesnt work, the else conditional won't even run
    elif b % 2 != 0:
        if b > a and b > c:
            #print "%d is the greatest odd number" % b
            op1 = b
        elif c > b and b > a:
            if c % 2 == 0:
                #print "%d is the greatest odd number" % b
                op1 = b
        elif a > b and b > c:
            if a % 2 == 0:
                #print "%d is the greatest odd number" % b
                op1 = b
        elif a > b and c > b:
            if a % 2 == 0:
                if c % 2 == 0:
                    #print "%d is the only odd number, therefore it's the greatest" % b
                    op1 = b
    elif c % 2 != 0:
        if c > a and c > b:
            #print "%d is the greatest odd number" % c
            op1 = c
        elif a > c and c > b:
            if a % 2 == 0:
                #print "%d is the greatest odd number" % c
                op1 = c
        elif b > c and c > a:
            if b % 2 == 0:
                #print "%d is the greatest odd number" % c
                op1 = c
        elif a > c and b > c:
            if b % 2 == 0:
                if a % 2 == 0:
                    #print "%d is the only odd number, therefore it's the greatest" % c
                    op1 = c
    else:
        #print "There are no odd numbers"
        op1 = 0 # my bug is right here. basically whenever i==3, this loop goes to the else command
                # even if already found the hghest odd

    for i in range(1, 3):
        if flag <= 3:  # checks if each number from greatest to smalles is odd. once one is odd the loop stops
            if snumbers[-i] % 2 != 0.0:
                #print "%d is the greatest odd number" % snumbers[-i]
                op2 = snumbers[-i]
                flag = 5  # makes flag above condition for loop
            else:
                flag += 2  # increases flag by 2
    if flag == 4:  # once flag equals 4 then that means the two greatest numbers are even, so it evaluates the smallest
        if snumbers[-3] % 2 != 0:
            #print '%d is the greatest odd number' % snumbers[-3]
            op2 = snumbers[-3]
        else:  # only did the above if loop because for some reason the if loop 'if sv1[-i]%2!=0.0:' wont evaluate sv1[-3]
            #print 'No odd numbers'
            op2 = 0
    x[i] = (op1 - op2)
print x # the sum of vector x won't equal 0 unless I print x first, I'm not sure why
if sum(x)==0:
    print "It all checks out!"
else:
    print "Yikes! Houston, we have a problem."

