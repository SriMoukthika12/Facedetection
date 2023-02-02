import cv2
import numpy as np
image=cv2.imread('Naruto.png')
cv2.imshow('HUMAN',image)
blank=np.zeros((300,300,3),dtype='uint8')
cv2.imshow('Blank',blank)
# paint the image a certain colour
blank[:]=0,255,0
cv2.imshow('Green',blank)
blank[:]=0,0,255
cv2.imshow('Red',image)
blank[:]=255,0,0
cv2.imshow('Blue',image)
blank[:]=255,255,255
cv2.imshow('RGB',image)
# image[:]=255,255,255
# cv2.imshow('Red',image)
cv2.waitKey(0)