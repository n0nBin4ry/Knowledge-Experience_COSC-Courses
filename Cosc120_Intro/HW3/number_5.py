import math as mat
def pos(time): # made a function using function given and the parameters given
    return 300 - (((.25 * 32.17)/.1) * time) + (((.25**2)* 32.17) * (.1**2)) - ((((.25**2)* 32.17) * (.1**2)) * mat.exp((-0.1/.25) * time))
TOL = 10**-4
a = 0 # pos # t = 0
b = 4 # neg # t = 4, found to be negative by testing numbers in the defined function above
i = 1 #initializes number of iterations
while True:
    c = float(b - a)/2 #  bisectional method
    print 'c is', c, 'at iteration', i
    if abs(pos(c)) <= TOL: # if f(c) is in TOL then we have our answer
        print 'At iteration', i + ', it is discovered that time is', c + 'seconds.'
        break
    elif pos(c) < 0: # makes c new b if f(c) is negative
        b = c
    else: # makes c new a if f(c) is positive
        a = c
    if i == 10000: # end bisection method after 10,000 iterations
        print "Couldn't find time after 10,000 iterations"
        break
    i += 1