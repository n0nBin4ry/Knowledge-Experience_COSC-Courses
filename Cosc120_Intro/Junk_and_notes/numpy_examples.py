import numpy as np # imports numpy module in the name of np
x = np.zeros(5) # makes a zero array of 1 row and 5 columns
print x
x[0] = 1 # assigns 1 to the left most number in array
print x
x[1] = 2
x[2] = 3
x[3] = 4
x[4] = 5
print x
print sum(x) # sums all numbers in array x

import math as mt
print mt.fsum(x) # also sums all numbers in array x

from random import randint # imports the 'randint' function from the 'random' module
y = randint(0,9) # produces a random intiger between 0 and 9
print y
