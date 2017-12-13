yo1 = open('Image_Process/three_kids.txt','r')
for line in yo1:
    print line[:-1]
yo1.close()
from matplotlib import pyplot as plot, image
import numpy as np
img = image.imread('Image_Process/marbles.jpg')
imgplot = plot.imshow(img) # all this image stuff is for console, doesn't work in script