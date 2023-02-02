import cv2
image=cv2.imread('Itachi.PNG')
resized=cv2.resize(image,(1000,500),interpolation=cv2.INTER_AREA)
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]
    if rotPoint is None:
        rotPoint=(width//2,height//2)
    rotMat=cv2.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)
    return cv2.warpAffine(img,rotMat,dimensions)

rotated=rotate(resized,45)
cv2.imshow('Rotated',rotated)
rotated_rotated=rotate(rotated,-45)
cv2.imshow('Rotated_Rotated',rotated_rotated)
flip=cv2.flip(resized,0)
cv2.imshow('Flip',flip)
cv2.waitKey(0)