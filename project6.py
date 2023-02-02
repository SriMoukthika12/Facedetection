import cv2
import numpy as np
image=cv2.imread('Itachi.PNG')
resized=cv2.resize(image,(500,500),interpolation=cv2.INTER_AREA)
# -x--> left
# -y--> up
# x--> right
# y--> down
def translate(img,x,y):
    transMat=np.float32([[1,0,-x],[1,0,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv2.warpAffine(img,transMat,dimensions)

translated=translate(resized,100,100)
cv2.imshow('TRANSLATE',translated)
cv2.imshow('RESIZED',resized)
cropped=resized[50:200,200:400]
cv2.imshow('CROPPED',cropped)
# cv2.imshow('HUMAN',image)
cv2.waitKey(0)