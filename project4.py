import cv2
import numpy as np
blank=np.zeros((300,300,3),dtype='uint8')
blank[50:60 ,60:70]=255,0,0
blank[80:90 ,90:100]=0,255,0
blank[110:150 ,150:300]=0,0,255
cv2.imshow('RGB',blank)
cv2.rectangle(blank,(0,0),(100,300),(0,0,255),thickness=cv2.FILLED)
cv2.imshow('Rectangle',blank)
cv2.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,0,255),thickness=cv2.FILLED)
cv2.circle(blank,(150,150),40,(255,0,0),thickness=cv2.FILLED)
cv2.line(blank,(0,0),(150,150),(255,255,255),thickness=3)
cv2.imshow('Geometry',blank)
cv2.putText(blank,'Hello World',(0,150),cv2.FONT_HERSHEY_TRIPLEX,1.0,(255,255,0),2)
cv2.imshow('Text',blank)
cv2.waitKey(0)