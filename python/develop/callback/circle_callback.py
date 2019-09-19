import sys 
sys.path.append("../layer")

import Circle_Layer
import cv2 as cv 

def cirle_callback(e,x,y,flag,param):
    if e == cv.EVENT_LBUTTONDBLCLK:
        
    elif e == cv.EVENT_RBUTTONDOWN:
        pass # 円を掴む
    elif e == cv.EVENT_MOUSEMOVE:
        pass # 円を動かす
    elif e == cv.EVENT_MBUTTONUP:
        pass # 円を離す

class callback_param:
    def ___init__(self):
        self.name = 0
        self.image = 0
        
    
    