import cv2
import matplotlib.pyplot as plt
import numpy as np
def rescaleFrame(frame,scale=0.25):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)
image=cv2.imread("Neha.jpeg")
resized=rescaleFrame(image)
blank=np.zeros(resized.shape[:2], dtype='uint8')
# gray=cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray",gray)
circle=cv2.circle(blank,(resized.shape[1]//2,resized.shape[0]//2),100,255,-1)
cv2.imshow("Circle",circle)
mask=cv2.bitwise_and(resized,resized,mask=circle)
cv2.imshow("Mask",mask)
# gray_hist=cv2.calcHist([gray],[0],None,[256],[0,256])
plt.figure()
plt.title("RGB Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

#COLOR HISTOGRAM
colors=('b','g','r')
for i,col in enumerate(colors):
    hist=cv2.calcHist([resized],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])

plt.show()
cv2.waitKey(0)