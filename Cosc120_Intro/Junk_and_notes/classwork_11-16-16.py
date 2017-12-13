s = 'Yoooo, Whats up'
sl = s.lower() # makes all letters in string 's' lower case
a = ''
for c in sl:
    print c
    if c in 'acdefghijklmnopqrstuvwxyz':
        print 1 # just an example of checking if the sting element is from the alphabet
        a += c
print a
b = ''
for c in range(len(sl)+1):
    b += sl[-c]
print b
# n = 100
# j = 2
# pm = [2]
# tpm = []
v = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4]
from random import shuffle as sh
print v
sh(v)
print v
