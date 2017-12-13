from random import randint #imports the randint function from the random module
n = raw_input("How many numbers should be on the list?")
n = int(n)
lt = [0] #initialized list
for i in range(1,n): # creates list of lengt n
    lt.append(0)
for i in range(len(lt)): #randomizes each element in list
    lt[i] = randint(0,20)
print lt
for j in range(len(lt)):  # runs loop as many times as the number of elements
    for k in range(len(lt) - 1):
        if lt[k] > lt[k + 1]:  # compares every two numbers along vector
            place = lt[k]
            lt[k] = lt[k + 1]
            lt[k + 1] = place  # switches a smaller on left with greater number on right if the conditions are met
            place = 0
print lt # the list is now sorted to find the median
print "The mean of the list is:", float(sum(lt))/len(lt) # once everything's sorted, the take calculate the mean by taking the average
if len(lt) % 2 == 0: # if theres an even number of elements then the median can be..
    if lt[len(lt)/2] == lt[(len(lt)/2) - 1]: # one of the two middle numbers if they are equal
        print "The median of the list is:", lt[len(lt)/2]
    else: # or the average of the two middle numbers
        print "The median of the list is:", (lt[len(lt) / 2] + lt[(len(lt)/2) - 1]) / 2.0
else: # if it's an odd number of elements then the median is just the middle number of the sprted list
    print "The median of the list is:", lt[len(lt)/2]