import numpy as np # imports numpy module and changes name to 'np'
from random import randint # imports the randint function from the random module
v1 = np.zeros(3) # creates a vector with 3 elements
for i in range(0,3): # fills in each element with a random integer from 0 to 9
    v1[i] = randint(0,9)
print "The numbers in comparison are", v1
sv1 = sorted(v1) # makes another vector with the same elements as first one but in order from smallest to greatest
flag = 0 # index for a condition
for i in range(1,3):
    if flag <= 3: # checks if each number from greatest to smalles is odd. once one is odd the loop stops
        if sv1[-i]%2!=0.0:
            print "%d is the greatest odd number" %sv1[-i]
            flag = 5 #makes flag above condition for loop
        else:
            flag += 2 # increases flag by 2
if flag == 4: # once flag equals 4 then that means the two greatest numbers are even, so it evaluates the smallest
    if sv1[-3]%2 != 0:
        print '%d is the greatest odd number' %sv1[-3]
    else: # only did the above if loop because for some reason the if loop 'if sv1[-i]%2!=0.0:' wont evaluate sv1[-3]
        print 'No odd numbers'