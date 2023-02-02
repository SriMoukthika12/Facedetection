import cv2
img=cv2.imread("Neha.jpeg",0)
def rescaleFrame(frame,scale=0.5):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)
resized_image=rescaleFrame(img)
a,b=resized_image.shape
for i in range(a):
    for j in range(b):
        if img[i,j]>125:
            img[i,j]
        else:
            img[i,j]
cv2.imshow("",resized_image)
cv2.waitKey(0)