import cv2
import numpy as np
def rescaleFrame(frame,scale=0.25):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)
img=cv2.imread("Neha.jpeg")
resized=rescaleFrame(img)
cv2.imshow("Neha",resized)
blank=np.zeros(resized.shape[:2],dtype='uint8')
b,g,r=cv2.split(resized)
blue=cv2.merge([b,blank,blank])
green=cv2.merge([blank,g,blank])
red=cv2.merge([blank,blank,r])

cv2.imshow("Blue",blue)
cv2.imshow("Green",green)
cv2.imshow("Red",red)

# print(resized.shape)
# print(b.shape)
# print(g.shape)
# print(r.shape)
# merged=cv2.merge([b,g,r])
# cv2.imshow("Merged",merged)
cv2.waitKey(0)