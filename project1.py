import cv2
def rescaleFrame(frame,scale=2):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)

image=cv2.imread('world.png')
resized_image=rescaleFrame(image)
# cv2.imshow('HUMAN',image)
cv2.imshow('HUMAN',resized_image)
cv2.waitKey(0)