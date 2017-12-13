#examples for learning of tuples
# t1 = ()
# t2 = (1,2,'3')
# t3 = (1,2,'hello',3.14)
# print t1
# print t2
# print t3
# print "t3[2] =", t3[2]
# # can slice and index tuples like strings and arrays
# print "t3 is a ", type(t3)
# x = (1)
# print "x is a", type(x) # if theres just a number then it isnt a tuple itll just be an integer or float
# x = (1,)
# print "x is now a", type(x) # to just have one tupple there has to be acomma after the number so that it isnt just a number

# # concatination of tuples
# x = (1, 'hello', 5)
# print "tuple x is", x
# y = (x, 3.14) # inputs the x tuple into y tuple: ((1,'hello',5),3.14))
# print "tuple y is", y
# print x + y
# #EX
# x = ()
# for i in range(100):
#     x += (i + 1, )
# print x
# print sum(x)
#
# #non-mutability
# x = (1, 'hello', 5)
# x[0] = 3 # ERROR
# y = '123'
# y[0] = 5 # ERROR
# # strings and tuples cannot be mutated

# Is there a native data structure in python that is mutable? YES
# LIST: ordered sewuence of values with each value ID'd by an index
# lists are mutable, but CAN ONLY BE DONE IN PYTHON

x = [] # empty list
print type(x)
z = ['I did it all',4,'love']
print z # shows brakets and all
for i in range(len(z)):
    print z[i] # lists each element vertically

# lists are mutable
L = [1,2,3]
print "L =", L
L[0] = 5
print "L now =", L