# for hw, try to achieve max stack depth for the fibonaci function defined in last class

# def sumnum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sumnum(n-1)

# n = 1000
# print 'sum of numbers from 1 to %d is %d' %(n, sumnum(n))
# this crashes because the stack is too big
# loops are preffered

def sumnumlp(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
n = 1000
print sumnumlp(n)

def fib(n):
    global numfibcalls
    numfibcalls += 1
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n - 2)
def testfib(n):
    for i in range(n + 1):
        global numfibcalls
        numfibcalls = 0
        print 'fib of', i, '=', fib(i)
        print 'fib called', numfibcalls, 'times'

testfib(5)

###############################################################################################
# L = [1,2,3,4,5]
# print L
# M = L
# print M[0]
# M[0] = 'hi'
# print M
# print L
# # changes in M appear in L
#
# L = [1,2,3,4,5]
# M = L[:]
# M[0] = 'hi'
# print M
# print L
#
# import copy
# L = [1,2,3,4,5]
# M = copy.deepcopy(L)
# M[0] = 'hi'
# print 'L =', L
# print 'M =', M
# methods to change
################################################
# MAKING MODULES BITCHES
# made a seperate file called circle.py, in same directory as this file

import circle as circ
print circ.pi
print circ.area(5)
