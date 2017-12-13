# From edwin, LATE

# Pylab Plotting
# in console I think

import pylab

pylab.figure(1)  # creating figure 1
# pylab.plot([1,2,3,4],[1,4,9,16])  # plot in figure 1
# pylab.show() # show figure on screen

pylab.clf()  # clear current window
#pylab.close()  # close current window



# pylab.figure(1)
# pylab.plot([1,2,3,4],[1,2,3,4])
# pylab.figure(2)
# pylab.plot([1,4,2,3],[5,6,7,8])
# pylab.savefig('Figure-2')
# pylab.figure(1)
# pylab.plot([5,6,10,3])
# pylab.savefig('Figure-1')
#
#

# c_pop = 100  #current population, also, now = initial pop'n
# g_rate = 0.10 #growth rate 10%
# p = [] # empty list to store current poplulation
# years = 50 #number of years
#
# for i in range(years+1): # years +1 to account for initial population
#     p.append(c_pop) # append current population to p
#     c_pop += g_rate*c_pop # update subsequent population
# pylab.plot(p)
#
# pylab.title('10% growth of poplution per year')
# pylab.xlabel('years')
# pylab.ylabel('popluation at year n')
# pylab.plot(p, 'mo') # default is b- = blue line