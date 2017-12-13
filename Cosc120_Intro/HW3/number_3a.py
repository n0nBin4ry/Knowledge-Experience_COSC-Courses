import numpy as np
from random import shuffle
marbles = np.zeros(200) # fills "bag" with 200 marbles
i = 0
for n in range(1,41): # evenly distributes marbles into 40 types
    while i < (5 * n):
        marbles[i] = n
        i += 1
#print marbles
print 'How many iterations would you like to run? Please enter an integer.'
while True:
    try:
        N = int(raw_input('> '))
        break
    except ValueError:
        pass
counter = 0 # intitializes
for j in range(N):
    shuffle(marbles) # shuffles marbles every iteration
    #print marbles
    if marbles[0] == marbles[1]: # 'takes out' first two marbles
        counter += 1 # if same type, counter increases
    print 'Iteration #', (j + 1)
    print "Counter =", counter
    prob = ((float(counter)/(j+1)) * 100)
    print "Probability is",prob,"%"