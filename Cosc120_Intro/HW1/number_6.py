import numpy as np # import numpy module as 'np'
from random import randint # imports randint function from random module
print "Part one:"
N = 2 # number of coins
M = np.zeros(7) # creates vector for the M values we want to test out
for i in range(0,6): # will run loop making i equal every integer between 0 and 5 in order
    # when testing I recommend making the array 6 elements and only going 0,5.
    # what I have will work but it took my computer minutes for M = 10000000
    M[i] = 10**(2+i) # assigns an amount for the selected element of vector M
    K = int(M[i]) # takes new amount of selected element and assigns it to variable K
    heads = 0 # initialize counter for amount of heads in this loop
    tails = 0 # initialize counter for amount of tails in this loop
    for j in range(0, N): # will run loop making j equal every integer between 0 and N in order
        x = np.zeros(K)  # makes vector x with K elements
        for w in range(0, K): # will run loop making w equal every integer between 0 and K in order
            x[w] = randint(0, 1)  # inputs a random integer from 0-1 for every element in array
        y = (x == 0)  # checks every element of array to see if statement is true, x=0->heads
        y = float(sum(y))
        heads = heads + y # saves the total heads for every loop from 0 to N
        z = (x == 1) # checks every element of array to see if statement is true, x=1->tails
        z = float(sum(z))
        tails = tails + z # saves the total tails for every loop from 0 to N
    print "For M = %d, probability of heads:" %K, (heads / (N * K)) * 100, '%'
    print "For M = %d, probability of tails:" %K, (tails / (N * K)) * 100, '%'
# AGAIN: # when testing I recommend making the array M 6 elements and only going 0,5.
    # what I have will work but it took my computer minutes for M = 10000000
print "Part two:"
N = 4 # number of coins is now 4
M = np.zeros(7)
for i in range(0,6):
    M[i] = 10**(2+i)
    K = int(M[i])
    heads = 0
    tails = 0
    for j in range(0, N):
        x = np.zeros(K)  # initialize N-dim'n array (row vector)
        for w in range(K):
            x[w] = randint(0, 1)  # inputs a random integer from 0-1 for every element in array
        y = (x == 0)  # checks every element of array to see if statement is true
        y = float(sum(y))
        heads = heads + y
        z = (x == 1)
        z = float(sum(z))
        tails = tails + z
    print "For M = %d, probability of heads:" %K, (heads / (N * K)) * 100, '%'
    print "For M = %d, probability of tails:" %K, (tails / (N * K)) * 100, '%'
# Same important note I put on part 1
print "Part three:"
heads = 0 # initialize counter of heads
tails = 0 # initialize counter of tails
N = raw_input('How many coins?') # User inputs number of coins
N = int(N)
M = raw_input('How many trials?') # User inputs number of trials
M = int(M)
for i in range(0,N):
    x = np.zeros(M)
    for i in range(M):
        x[i] = randint(0,1)
    print x
    y = (x==0)
    y = float(sum(y))
    heads = heads + y
    z = (x==1)
    z = float(sum(z))
    tails = tails + z
print "Probability of heads:", (heads/(N*M))*100,'%'
print "Probability of tails:", (tails/(N*M))*100,'%'