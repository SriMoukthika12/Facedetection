import cv2
import matplotlib.pyplot as plt
def rescaleFrame(frame,scale=0.25):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)
image=cv2.imread("Itachi.PNG")
resized=rescaleFrame(image)
bgr=cv2.cvtColor(resized,cv2.COLOR_RGB2BGR)
cv2.imshow("Itachi",bgr)
plt.imshow(bgr)
plt.show()
# cv2.waitKey(0)
#we cannot convert Grayscale to LAB