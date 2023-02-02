#AND OR XOR NOT
import cv2
import numpy as np
blank=np.zeros((400,400), dtype='uint8')
rectangle=cv2.rectangle(blank.copy(),(30,30),(370,370),100,-1)
circle=cv2.circle(blank.copy(),(200,200),200,100,-1)
# cv2.imshow("Rectangle",rectangle)
# cv2.imshow("Circle",circle)

#Bitwise AND
bitwise_and=cv2.bitwise_and(rectangle,circle)
cv2.imshow("AND",bitwise_and)

#Bitwise OR
bitwise_or=cv2.bitwise_or(rectangle,circle)
cv2.imshow("OR",bitwise_or)

#Bitwise XOR
bitwise_xor=cv2.bitwise_xor(rectangle,circle)
cv2.imshow("XOR",bitwise_xor)

#Bitwise NOT
bitwise_not=cv2.bitwise_not(rectangle)
cv2.imshow("Not rectangle",bitwise_not)
cv2.waitKey(0)