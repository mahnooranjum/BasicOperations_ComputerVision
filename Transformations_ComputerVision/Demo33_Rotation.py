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

#ROTATION
image = cv2.imread(path)
cv2.imshow('Original', image)
height, width, = image.shape[:2]
# M = || cos    -sin ||
#     || sin     cos ||
M = cv2.getRotationMatrix2D((width/2, height/2),50,1)
rotated_image = cv2.warpAffine(image, M,(width, height))
cv2.imshow('Rotated image',rotated_image)

#TRANSPOSE ROTATION BY 90
image = cv2.imread(path)
cv2.imshow('Original', image)
transposed_image = cv2.transpose(image)
cv2.imshow('Transposed',transposed_image)


cv2.waitKey()
cv2.destroyAllWindows()


