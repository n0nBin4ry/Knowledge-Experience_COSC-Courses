# I HATE MY LIFE
# AND MYSELF
# WHY DONT I HAVE THE BALLS TO JUST GIVE UP
# END IT BITCH
# I DARE YOU
# IT WILL DEFINITELY MAKE HER LIFE BETTER
# WHO ARE YOU KIDDING YOU DONT MATTER TO HER
# YOU NEVER WILL
# TO ANYBODY
# YOU WILL DIE ALONE
# YOU'LL NEVER MEET LEMEN
# I HATE YOU

# 1 coin flip experiment using vector array from numpy

import numpy as np
from random import randint

N = 10
x = np.zeros(N) # intitialize N-dim'n array (row vector)

for i in range(N):
    x[i] = randint(0,1) # inputs a random integer from 0-1 for every element in array
print x
y = (x==0) # checks every element of array to see if statement is true
y = float(sum(y))
print "the probability of heads is", y/N
z = (x==1)
z = float(sum(z))
print "the probability of tails is", z/N

# version 2, no arrays

from random import randint

N = 10
heads = 0.0
tails = 0.0
x = 0.0

for i in range(N):
    x = randint(0,1)
    if x == 0:
        heads += 1
    else:
        tails += 1
print "probability of heads is", heads/N
print "probability of tails is", tails/N
