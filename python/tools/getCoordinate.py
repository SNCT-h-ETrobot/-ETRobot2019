import cv2 as cv 
import numpy as np 

moving = False
ix,iy = -1,-1
shift_x,shift_y = 0,0
src = np.array([[0.0,0.0],[0.0,1.0],[1.0,0.0]],np.float32)
dst = src.copy

coordinate_circle_layer = np.zeros((512,512,3),np.uint8)

cv.namedWindow("circle")
h,w = cv.getWindowImageRect('circle')[2:4]

def circle_callback(e,x,y,flags,param):
    global src,dst,moving,coordinate_circle_layer
    if e==cv.EVENT_LBUTTONDBLCLK:
        cv.circle(coordinate_circle_layer,(x,y),5,(0,0,255),-1)
    elif e == cv.EVENT_RBUTTONDOWN:
        moving = True
        src = np.float32([[x,y],[x+10,y],[x,y+10]])
    elif e == cv.EVENT_MOUSEMOVE:
        if moving == True:
            dst = np.float32([[x,y],[x+10,y],[x,y+10]])
            affine = cv.getAffineTransform(src,dst)
            coordinate_circle_layer = cv.warpAffine(coordinate_circle_layer,affine,(w,h))
            src = dst
            print (" x:",x," y:",y)
            print ("src: \n",src)
            print ("dst: \n",dst)
    elif e == cv.EVENT_RBUTTONUP:
        if moving == True:
            moving = False
    
cv.setMouseCallback('circle',circle_callback)

while(1):
    cv.imshow("circle",coordinate_circle_layer)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
