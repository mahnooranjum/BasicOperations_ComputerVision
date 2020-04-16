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

#RESIZING

#INTERPOLATION
#LINEAR UPSAMPLING DEFAULT
image = cv2.imread(path)
cv2.imshow('Original', image)
linear = cv2.resize(image, None, fx=1.75, fy=1.75, interpolation=cv2.INTER_LINEAR)
cv2.imshow('Linear Interpolation',linear)

#AREA DOWNSAMPLING
image = cv2.imread(path)
cv2.imshow('Original', image)
area = cv2.resize(image, None, fx=0.75, fy=0.75, interpolation=cv2.INTER_AREA)
cv2.imshow('Area Interpolation',area)

#NEAREST FASTEST
image = cv2.imread(path)
cv2.imshow('Original', image)
nearest = cv2.resize(image, None, fx=0.75, fy=0.75, interpolation=cv2.INTER_NEAREST)
cv2.imshow('Nearest Interpolation',nearest)

#CUBIC BETTER THAN LINEAR
image = cv2.imread(path)
cv2.imshow('Original', image)
cubic = cv2.resize(image, None, fx=1.75, fy=1.75, interpolation=cv2.INTER_CUBIC)
cv2.imshow('Cubic Interpolation',cubic)

#LANSOZ4 THE BEST INTERPOLATION
image = cv2.imread(path)
width, height = image.shape[:2]
cv2.imshow('Original', image)
lanczos = cv2.resize(image, (int(width*3),int(height/2)), interpolation=cv2.INTER_LANCZOS4)
cv2.imshow('LANCZOS Interpolation',lanczos)

#PYRAMIDING
image = cv2.imread(path)
cv2.imshow('Original', image)
upscale=cv2.pyrUp(image)
downscale=cv2.pyrDown(image)
cv2.imshow('Upscale Pyramid', upscale)
cv2.imshow('Downscale Pyramid', downscale)


cv2.waitKey()
cv2.destroyAllWindows()


