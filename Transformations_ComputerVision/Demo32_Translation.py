#==============================================================================
#   By: Mahnoor Anjum
#   Date: 8/12/2018
#   Codes inspired by:
#   Github.com/imvinod/
#   Official Documentation
#==============================================================================
import cv2
import numpy as np

path = "imgs\demo32.jpg"
#TRANSLATION
image = cv2.imread(path)
cv2.imshow('Original', image)
height, width, = image.shape[:2]
x, y = height/5, width/5
# T = || 1     0    Tx ||
#     || 0     1    Ty ||
#T is our transformation matrix
T = np.float32([[1,0,x],[0,1,y]]) 
translated_image = cv2.warpAffine(image,T,(width,height))
cv2.imshow('Translated image',translated_image)


cv2.waitKey()
cv2.destroyAllWindows()


