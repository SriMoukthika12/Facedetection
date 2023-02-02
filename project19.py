import cv2
import matplotlib.pyplot as plt
def rescaleFrame(frame,scale=0.25):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)
capture=cv2.VideoCapture(0)
while True:
    isTrue, frame=capture.read()
    frame_resized=rescaleFrame(frame)
    gray=cv2.cvtColor(frame_resized,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray",gray)
    gray_hist=cv2.calcHist([gray],[0],None,[256],[0,256])
    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of pixels")
    plt.plot(gray_hist)
    plt.xlim([0,256])
    plt.show()
    if cv2.waitKey(0) & 0xFF==ord('d'):
        break
capture.release()
cv2.destroyAllWindows()