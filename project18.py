import cv2
import matplotlib.pyplot as plt
def rescaleFrame(frame,scale=0.25):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)
image=cv2.imread("Itachi.PNG")
resized=rescaleFrame(image)
gray=cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray)
gray_hist=cv2.calcHist([gray],[0],None,[256],[0,256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
cv2.waitKey(0)