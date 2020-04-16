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

#IMAGE BRIGHTENING AND DARKENING
image = cv2.imread(path)
cv2.imshow('Original', image)
A = np.ones(image.shape,np.uint8)*80
Bright = cv2.add(image,A)
Dark = cv2.subtract(image,A)
cv2.imshow('Bright', Bright)
cv2.imshow('Dark', Dark)

cv2.waitKey()
cv2.destroyAllWindows()


