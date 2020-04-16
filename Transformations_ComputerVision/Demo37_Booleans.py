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

#MASKING 
x0 = 200
y0 = 100
width = 200
height = 100
stroke = -1
color = (255,255,255)
rectangle =np.zeros((512,512,3),np.uint8)
cv2.rectangle(rectangle, (x0,y0),(x0+width,y0+height),color,stroke)
cv2.imshow("Rectange",rectangle)

x0 = 200
y0 = 200
radius = 100
color=(255,255,255)
stroke=-1
circle =  np.zeros((512,512,3),np.uint8)
cv2.circle(circle,(x0,y0),radius,color,stroke)
cv2.imshow("Circle",circle)

#AND
And = cv2.bitwise_and(rectangle, circle)
cv2.imshow('AND',And)
#OR
Or = cv2.bitwise_or(rectangle, circle)
cv2.imshow('OR',Or)
#XOR
Xor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow('XOR',Xor)
#NOT
Not = cv2.bitwise_not(rectangle)
cv2.imshow('NOT',Not)

cv2.waitKey()
cv2.destroyAllWindows()


