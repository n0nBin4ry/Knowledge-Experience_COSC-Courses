from random import randint # imports randint func from the module random
n = raw_input("How long do you want the list of arbitrary numbers? Please input an integer.")
n = int(n) # user inputs length of list
list = [0] # inititializes list
for i in range(1,n): # makes list as long as the user's requested amount
    list.append(0)
for i in range(len(list)): # makes each element of list a random integer from 1 to 100
    list[i] = randint(0,100)
print "The list generated is:", list
for j in range(len(list)):  # runs loop as many times as the number of elements
    for k in range(len(list) - 1):
        if list[k] > list[k + 1]:  # compares every two numbers along list
            place = list[k]
            list[k] = list[k + 1]
            list[k + 1] = place  # switches a smaller on left with greater number on right if the conditions are met
            place = 0
print "This is now the same list sorted in order from least to greatest:", list