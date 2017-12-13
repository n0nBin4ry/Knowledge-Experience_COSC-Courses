# FILES
'''
nameHandle = open('kids','w') # file handle
# creates file "kids"; w indicates that the file is for writing
for i in range(2):
    name = raw_input('Enter name: ')
    nameHandle.write(name + '\n') # writes name to file
nameHandle.close()
# if you want to read the file then you create the file
nameHandle = open('kids','r') # r in stead of w to read
for line in nameHandle:
    print line[:-1] # won't print '\n'
nameHandle.close()
'''
'''
nameHandle = open('kids','w')
nameHandle.write('Micheal\n')
nameHandle.write('Mark\n')
nameHandle.close()
nameHandle = open('kids','r')
for line in nameHandle:
    print line[:-1]
nameHandle.close()
# overwrites previous content of file
# now to append
nameHandle = open('kids','a') # a now and it stands for append, appends name to file
nameHandle.write('Noah\n')
nameHandle.write('Jake\n')
nameHandle.close()
nameHandle = open('kids','r')
for line in nameHandle:
    print line[:-1]
nameHandle.close()
'''

# PLOTTING AND IMAGES
# put in console for now
import matplotlib.pyplot as plot
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('pinkcalc.jpg')
imgplot = plot.imshow(img)
