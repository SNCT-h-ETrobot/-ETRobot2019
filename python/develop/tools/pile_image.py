import cv2 as cv 
import numpy as np 

image1 = cv.imread("picture/et001.PNG")
image2 = cv.imread("picture/sample.PNG")

# cv.imshow("image1",image1)
# cv.imshow("image2",image2)
# cv.waitKey(0)

x,y = 0,0

h,w = image2.shape[:2]
image1[y:y+h,x:x+w] = image2

cv.imshow("image1",image1)
cv.waitKey(0)
