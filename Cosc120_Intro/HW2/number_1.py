import numpy as np #imported the numpy module
from random import randint as rt #importedd randint operator from the random module
place = 0 #empty placeholder for switching variables
n = raw_input("How many iterations would you like to run? Enter an integer.") #prompt for user input of iterations
n = int(n) # makes the string input a an integer
diff = np.zeros(n) # makes a difference vector to test out the output from each iteration
for i in range(n):
    vran =  np.zeros(10)
    for j in range(10):
        vran[j] = rt(0,9) # randomizes numbers in vector
    vran2 = vran # makes copy of unsorted vector to test my program at end
    print "Vector at iteration # %d" %(i+1), vran
    for j in range(len(vran)): # runs loop as many times as the number of elements
        for k in range(len(vran)-1):
            if vran[k] > vran[k+1]: # compares every two numbers along vector
                place = vran[k]
                vran[k] = vran[k+1]
                vran[k+1] = place # switches a smaller on left with greater number on right if the conditions are met
                place = 0
    print "Sorted vetor, iteration # %d" %(i+1), vran
    diff[n-1] = sum(vran - sorted(vran2)) #inputs into the difference vector the difference between the vector sorted by my loop and the vector sorted by sort function
print diff
print sum(diff) #prints sum of difference vector to show zero, meaning my loop works just as well as the sorted function