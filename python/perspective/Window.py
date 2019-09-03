import sys
sys.path.append('layer')
import Circle_Layer
import cv2 as cv 
import numpy as np 

class Window:
    def __init__(self,name,image):
        self.name = name 
        self.image = image
        self.layer_list = []
        cv.namedWindow(self.name)
    
    def pile_image(self,x,y,image):
        #background=>b,foreground=>f,start=>s, 
        # reference:https://www.tech-tech.xyz/clip_image.html
        back_h,back_w = self.image.shape[:2]
        fore_h,fore_w = image.shape[:2]
        fore_w = min(fore_w,back_w - x)
        fore_h = min(fore_h,back_h - y)
        start_x = min(max(-x,0),fore_w)
        start_y = min(max(-y,0),fore_h)
        self.image[max(y,0):y+fore_h,max(x,0):x+fore_w] = image[start_y:start_y+fore_h,start_x:start_x + fore_w]
        print("layer を重ねました")

    def show_image(self):
        cv.imshow(self.name,self.image)

    def set_callback(self):
        cv.setMouseCallback(self.name,self.__on_mouse)
        print("コールバック関数を追加しました。")

    def __on_mouse(self,e,x,y,flags,param):
        if e == cv.EVENT_LBUTTONDBLCLK:
            layer_num = len(self.layer_list)
            layer_name = 'circle' + str(layer_num)
            self.__add_circle(x,y,layer_name)
            self.pile_image(x,y,self.layer_list[layer_num].image)  
            
    def __add_circle(self,x,y,name):
            circle = Circle_Layer.Circle_Layer(x,y,name)
            self.layer_list.append(circle)
            print("circleを追加しました。\n 表示します....")
