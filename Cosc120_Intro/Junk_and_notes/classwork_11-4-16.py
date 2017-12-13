#tying up loose ends
import sys # method to have python exit a script

# keyword arguments and default values

# posisitonal --> first formal param is bound to first actual param, second formal to second actual..
'''
# blah blah idk
def printName(firstName,lastName, reverse):
    if reverse: # if only runs if conditon is true, so if reverse = False then it will go to else
        print lastName + ',', firstName
    else:
        print firstName, lastName

# all equivelent invocations of prtintName
printName('Richard','Flores', False)
printName('Richard','Flores',reverse = False)
printName('Richard', lastName = 'Flores', reverse = False)
printName(firstName= 'Richard', lastName = 'Flores', reverse = False)
printName(lastName = 'Flores', reverse = False, firstName = 'Richard')
sys.exit()
'''

'''
def printname(firstname, lastname, reverse = False): # if nothing is inputted for reverse then it equals False by default
    if reverse:
        print lastname + ',', firstname
    else:
        print firstname + ',', lastname
printname('Richard','Flores')
printname('Richard', 'Flores', True)
'''
'''
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def testfib(n):
    for i in range(n+1):
        print 'fibonaci number of', i, '=', fib(i)
print fib(5)
testfib(5)
'''
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
print fact(5)