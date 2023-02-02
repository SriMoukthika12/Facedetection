import cv2
import numpy as np
def rescaleFrame(frame,scale=0.1):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)
capture=cv2.VideoCapture(0)
while True:
    isTrue, frame=capture.read()
    frame_resized=rescaleFrame(frame)
    blank = np.zeros(frame.shape[:2],dtype='uint8')
    # cv2.imshow("Blank",blank)
    # mask=cv2.circle(blank,(frame.shape[1]//2,frame.shape[0]//2 - 45),110,255,-1)
    mask=cv2.rectangle(blank,(frame.shape[1]//2,frame.shape[0]//2),(frame.shape[1]//2+150,frame.shape[0]//2+300),255,-1)
    # cv2.imshow("Mask",mask)
    masked=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("Focused",masked)
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv2.destroyAllWindows()


#weird_shape=cv2.bitwise_and(circle,rectangle)
#cv2.imshow("Weird shape",weird_shape)
#masked=cv2.bitwise_and(img,img,mask=weird_shape)
#cv2.imshow("Masked Image",masked)