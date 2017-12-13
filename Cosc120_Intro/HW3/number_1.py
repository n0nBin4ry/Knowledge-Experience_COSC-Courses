print 'Please enter a word, phrase,and/ or series of integers.'
# while True:
#     inp = raw_input('> ')
#     try:
#         float(inp)
#         pass
#     except ValueError:
#         break
# turns out numbers can be palindromes
inp = raw_input('> ') # user input
inp = inp.lower() # makes all letters lower case
placeH = ''
reverseinp = ''
for i in inp:
    if i in 'abcdefghijklmnopqrstuvwxyz1234567890':
        placeH += i # eliminates symbols
#print placeH
for i in range(1,len(placeH) + 1):
    reverseinp += placeH[-i] # reverses the lower case string that had it's symbols removed
#print reverseinp
if placeH == reverseinp: # tests if string is the same forward and back
    print '"%s" is a palindrome.' %inp
else:
    print '"%s" is not a palindrome.' %inp
