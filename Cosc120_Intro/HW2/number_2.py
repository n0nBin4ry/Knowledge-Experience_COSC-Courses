from numpy import zeros as arr # imported zeros function from the numpy module
from random import randint as rt # imported randint function from the random module
n = raw_input("How many iterations? Please input an integer.")
n = int(n) # input number of iterations for loop
switched = 0.0 # initialized number of wins from switching choice every time
stayed = 0.0 # initialized number of wins from staying with choice every time
for j in range(n):
    doors = arr(3) #creates three 'doors'
    a = 0
    b = 1 # sets range of possible random numbers generated in upcoming loop
    for i in range(len(doors)): # this loop assigns one car(0) to the three doors and two goats(1) to the three doors
        doors[i] = rt(a,b) # assigns a random number between 0 and 1
        if doors[i] == 0: # if zero is assigned
            a = 1 # then the random functions range is changed, now 1 to 1
        if doors[i-1] == 1 and doors[i-2] == 1: # if first two numbers are 1, then the third is zero
            doors[i] = 0 # negative indexing doesn't interfere because all numbers in array start at 0
    choice = rt(0,2) # randomly choose door 1, 2, or 3
    if doors[choice - 1] == 1: # this if/else opens one of the goat doors that you didnt choose and selects the door you'd switch to if you chose to switch
        open = choice - 1
        switch = choice - 2
    else:
        open = choice - 2
        switch = choice - 1
    if doors[choice] == 0: # adds one win to staying if your original choice was the car
        stayed += 1
    if doors[switch] == 0: # assd one win to switching if you switched to a winning door
        switched += 1
    print "Wins by switching by trial # %d:" %(j+1), switched
    print "Wins by staying by trial # %d:" %(j+1), stayed
print "Always switching yields a", (switched/n)*100, "% chance of winning the car each time."
print "Always choosing to stay yields a", (stayed/n)*100, "% chance of winning the car each time."
# this matched the probability we concluded in class stating that switchcing means winning 2/3 of the time, while staying means winning 1/3 of the time