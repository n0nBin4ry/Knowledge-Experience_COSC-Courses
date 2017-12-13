print "Part one:"
i = 1 # index
S = 0 # placeholder for Sum
n = raw_input('Please input an integer to sum up:') # asks for user to input a number
flag = 1 # sets flag to 1
try:
    n = int(n) # tries to convert n to an integer since its a float
except ValueError: # if there's an error then...
    print "Error. The input has to be an integer." # error message is printed
    flag = 0 #changes flag to 0 if there was an error
if n <= 0: # checks if input is positive
    print "Error. The input has to be positive." # error message is printed
    flag = 0 # changes the flag to 0
if flag != 0: # if flag wasn't changed to zero then there was no error, so the loop can begin
    while i<=n: # while i is less than or greater than
        S = i + S # adds i to S every time loop runs
        i = i + 1 # adds 1 to i every time loop runs, causing the loop to continue until i = n
    print 'The sum is', S #prints sum

print "Part two:"
import numpy as np # imports numpy package as 'np'
v1 = np.zeros(100) # creates a vector with 100 elements
up = 1.0 # indexing
for count in range(0,100): # for every loop, count will increase by one from 0 to 100
   v1[count] = up # loop inputs value of up in selected element of v1
   up = up + 1 # increses up by 1 in every loop
print "Vector 1 =", v1
print "the sum of Vector 1 is", sum(v1) #sums up every element in vector

print "Part three:"
v2 = np.zeros(50) # creates vector v2, has 50 elements
v3 = np.zeros(50) # creates vector v3, has 50 elements as well
up = 1.0 # restarting index up
while up <= 50.0: # run loop until up = 50
    for count in range(0,50): # for every loop, count will increase by one from 0 to 50
        v2[count] = up # loop inputs value of up in selected element of v2
        up = up + 1 # increses up by 1
    break # force stops loop
while up > 50.0 <= 100.0: # run loop once up = 51 and until up = 100
    for count in range(0,50): # for every loop, count will increase by one from 0 to 50
        v3[count] = up # loop inputs value of up in selected element of v3
        up = up + 1 # up increases by 1
    break # force stops loop
print "Vector 2 =", v2
print "Vector 3 =", v3
print "The sum of Vector 2 and Vector 3 is", sum(v2 + v3) # prints sum of v2 and v3