import cv2 as cv
import numpy as np
import color
import ColorSet


#カメラから画像を取得する
#取得した画像を処理する
#値を返す
#input camera movie
#output list of color

file_path = "picture/et001.PNG"
img = cv.imread(file_path)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
_,contours,hierarchy = cv.findChessboardCorners(gray,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
ext = np.zeros(img.shape)

ext = cv.drawContours(ext,contours,-1,(0,255,0),-1)
cv.imshow("origin",img)
cv.imshow("gray",gray)
cv.waitKey(0)
cv.destroyAllWindows()


