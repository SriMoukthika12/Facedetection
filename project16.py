import cv2
import numpy as np
def rescaleFrame(frame,scale=0.1):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)
img=cv2.imread("Itachi.PNG")
resized=rescaleFrame(img)
cv2.imshow("Normal",resized)
blank = np.zeros(resized.shape[:2],dtype='uint8')
cv2.imshow("Blank",blank)
mask=cv2.circle(blank,(resized.shape[1]//2,resized.shape[0]//2 - 45),50,255,-1)
cv2.imshow("Mask",mask)
masked=cv2.bitwise_and(resized,resized,mask=mask)
cv2.imshow("Focused",masked)
cv2.waitKey(0)