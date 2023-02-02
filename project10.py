import cv2
capture=cv2.VideoCapture(0)
while True:
    isTrue, frame=capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('Video',frame)
    cv2.imshow('Video',gray)
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv2.destroyAllWindows()