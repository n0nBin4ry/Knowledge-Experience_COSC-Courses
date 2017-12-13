from numpy import zeros
from random import shuffle
deck = zeros(52) # makes a "deck" of 52 cards
i = 0
for n in range(1, 5): # splits up the deck into it's 5 parts
    while i < (n * 13):
        deck[i] = n
        i += 1
print deck
print 'How many iterations would you like to run? Please enter an integer.'
while True:
    try:
        N = int(raw_input('> '))
        break
    except ValueError:
        pass
counter = 0
for j in range(N):
    shuffle(deck) # shuffles deck
    if deck[0] != deck[1]:# 'picks' 2 first cards from deck
        counter += 1 # if they are 2 different types, the counter goes up
    print 'Iteration #', (j + 1)
    print "Counter =", counter
    prob = ((float(counter) / (j + 1)) * 100)
    print "Probability is", prob, "%"