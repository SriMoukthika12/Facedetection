import cv2
def rescaleFrame(frame,scale=1):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)

capture=cv2.VideoCapture(0)
while True:
    isTrue, frame=capture.read()
    frame_resized=rescaleFrame(frame)
    # cv2.imshow('Video',frame)
    # hsv=cv2.cvtColor(frame_resized,cv2.COLOR_BGR2HSV)
    lab=cv2.cvtColor(frame_resized,cv2.COLOR_BGR2LAB)
    cv2.imshow('Video Resized',lab)
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv2.destroyAllWindows()
# image=cv2.imread("Itachi.PNG")
# resized=rescaleFrame(image)
# # gray=cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
# #BGR to HSV
# hsv=cv2.cvtColor(resized,cv2.COLOR_BGR2HSV)
# cv2.imshow("Hsv",hsv)
# # cv2.imshow("Itachi",gray)
# cv2.waitKey(0)