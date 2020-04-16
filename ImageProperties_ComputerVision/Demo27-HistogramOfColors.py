#==============================================================================
#   Tutorial By: Mahnoor Anjum
#   Date: 4/04/2020
#   Codes inspired by:
#   Github.com/imvinod/
#   Official Documentation
#==============================================================================

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('imgs/demo27.jpg', 0)

B =[0]
G =[1]
R =[2]
# For the histogram of a full image, type None
mask = None
# The number of bins is put in the histsize
histSize = 256
rangeOfValues = [0, 256]
histogram = cv2.calcHist([img], B, mask, [histSize], rangeOfValues)

plt.hist(img.ravel(), histSize, rangeOfValues)
plt.title("Gray components")
plt.show()
plt.cla()
plt.clf()

img = cv2.imread('imgs/demo27.jpg')
for i, color in enumerate(('blue', 'green', 'red')):
    curve = cv2.calcHist([img], [i], mask, [histSize], rangeOfValues)
    plt.plot(curve, color = color)
    plt.xlim(rangeOfValues)
plt.title("Colors in image")
plt.show()
input("press any key...")
