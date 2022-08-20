import numpy as np
import cv2

duckpath="C:/Users/Ismail/Pictures/duck.jpg"
duck=cv2.imread(duckpath)
duck2=cv2.cvtColor(duck,cv2.COLOR_BGR2GRAY)
resize_gray=cv2.resize(duck2,(900,700),interpolation=cv2.INTER_AREA)
cv2.imshow("original gray",resize_gray)
cv2.waitKey(0)

#Binarize the image
(T,otsu)=cv2.threshold(resize_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("OTSU",otsu)
cv2.waitKey(0)
#apply canny
canny=cv2.Canny(otsu,0,255)
cv2.imshow("CANNY",canny)
cv2.waitKey(0)
#findcontours
(_,contours,_)=cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
copiedimage = imageO.copy()

#Highlightes the edges in any direction
laplace=cv2.Laplacian(smooth,cv2.CV_64F)
laplace=np.uint8(np.absolute(laplace))

cv2.imshow("LAPLACE",laplace)
cv2.waitKey(0)
#CANNY EDGE DETECTION
canny=cv2.Canny(smooth,30,130)
cv2.imshow("CANNY",canny)
cv2.waitKey(0)
