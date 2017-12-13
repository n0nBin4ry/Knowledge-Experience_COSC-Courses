# scoping
def f(x):
    y = 1
    x = x + y
    print 'x =', x
    return x
x = 3
y = 2
z = f(x) # even if I don't print z, x = 4 will be outputted because the function is still called in the code
print 'z=', z
print 'x =', x
print 'y = ', y
# what's going on here?
# the variables in the function are only assigned locally to the function
# any variables assigned in a function are no longer assigned out of the function
# x can = 3 in a function, but outside the function it can equal anything, even a string or a data structure