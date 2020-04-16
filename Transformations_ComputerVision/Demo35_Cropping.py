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

#CROPPING
image = cv2.imread(path)
cv2.imshow('Original', image)
width, height = image.shape[:2]
start_x, start_y = int(width*0.25),int(height*0.25)
end_x, end_y = int(width*0.75),int(height*0.75)
cropped_image=image[start_x:end_x,start_y:end_y]
cv2.imshow('Cropped Image', cropped_image)


cv2.waitKey()
cv2.destroyAllWindows()


