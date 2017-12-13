# 1. example of code break
# nested loop with break
for i in range(3): # goes from 0 to 3, so range(n) goes from 0 to (n-1),
    if i==2:
        break
    for j in range (5):
        if j==3:
            break
        else: # don't really need else, but looks pretty to me. could just have print command
            print j # prints whatever j equals in loop

# 2. examples of how to do number 4 from HW1
# did it corectly

# 3. Functions
# function example: max
# def function-name(x,y,...,z)
#   block of code
#       reurn c (c = value you return)
a = 5
b =
def max(a,b):
    if a>b:
        return a
    else:
        return b
def min(a,b):
    if a<b:
        return a
    else:
        return b
print max(3,1)
