import cv2 as cv 
import numpy as np 

origin = cv.imread("../develop/picture/et001.PNG")

cv.imshow("origin",origin)

dst = cv.cvtColor(origin,cv.COLOR_BGR2HSV)

for y in dst:
    for x in y:
        x[2] = 100


cv.imshow("dst",cv.cvtColor(dst,cv.COLOR_HSV2BGR))

cv.waitKey(0)

cv.destroyAllWindows()