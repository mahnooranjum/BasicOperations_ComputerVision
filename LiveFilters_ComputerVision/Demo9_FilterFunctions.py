##==============================================================================
##   Demo By: Mahnoor Anjum
##   Date: 31/03/2019
##   Codes inspired by:
##   Rajeev Ratab
##   Official Documentation
##==============================================================================

import cv2
import numpy as np


def sketch(image):
    low=10
    size=5
    high=70
    image_BW = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mblur = cv2.medianBlur(image_BW,size)
    Canny = cv2.Canny(mblur, low, high)
    ret2,th4 = cv2.threshold(Canny,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    return th4

def inverse(image):
    return abs(255-image)

def dilate(image):
    size=(5,5)
    kernel = np.ones(size,np.uint8)
    dilation=cv2.dilate(image,kernel, iterations=1)
    return dilation

def erode(image):
    size=(10,10)
    kernel = np.ones(size,np.uint8)
    erosion=cv2.erode(image,kernel, iterations=1)
    return erosion

def blue(image):
    B = image[:,:,0]
    zeros = np.zeros(image.shape[:2],dtype="uint8")
    image = cv2.merge([B, zeros, zeros])
    return image


def green(image):
    G = image[:,:,1]
    zeros = np.zeros(image.shape[:2],dtype="uint8")
    image = cv2.merge([zeros, G, zeros])
    return image


def red(image):
    R = image[:,:,2]
    zeros = np.zeros(image.shape[:2],dtype="uint8")
    image = cv2.merge([zeros, zeros, R])
    return image

def brighten(image):
    value = np.ones(image.shape,dtype="uint8")*150
    return cv2.add(image, value)

def darken(image):
    value = np.ones(image.shape,dtype="uint8")*150
    return cv2.subtract(image, value)
#The following loop is used for live webcam capture
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('Darken', darken(frame))
    cv2.imshow('Brighten', brighten(frame))
    cv2.imshow('Blue', blue(frame))
    cv2.imshow('Red', red(frame))
    cv2.imshow('Green', green(frame))
    cv2.imshow('Sketch', sketch(frame))
    cv2.imshow('Inverse', inverse(frame))
    cv2.imshow('Dilate', dilate(frame))
    cv2.imshow('Dilate', erode(frame))
    if cv2.waitKey(1) == 32: 
        break
cap.release()  
cv2.destroyAllWindows()