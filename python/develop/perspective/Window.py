import sys
sys.path.append('layer')
import Circle_Layer
import cv2 as cv 
import numpy as np 

class Window:
    def __init__(self,name):
        self.name = name 
        self.layer_list = []
        cv.namedWindow(self.name)

    def set_image(self,image):
        self.src_image = image
        self.image = image.copy()
    def pile_image(self,x,y,back_image,fore_image):
        #background=>b,foreground=>f,start=>s, 
        # reference:https://www.tech-tech.xyz/clip_image.html
        back_h,back_w = back_image.shape[:2]
        fore_h,fore_w = fore_image.shape[:2]
        fore_w = min(fore_w,back_w - x)
        fore_h = min(fore_h,back_h - y)
        start_x = min(max(-x,0),fore_w)
        start_y = min(max(-y,0),fore_h)
        back_image[max(y,0):y+fore_h,max(x,0):x+fore_w] = fore_image[start_y:start_y+fore_h,start_x:start_x + fore_w]
        # print("layer を重ねました")

    def show_image(self):
        for layer in self.layer_list:
                self.pile_image(layer.x,layer.y,self.image,layer.image)
        cv.imshow(self.name,self.image)        

    def get_layers_coordinates(self):
        res = []
        for layer in self.layer_list:
            res.append(layer.get_coordinate())
        return res

    def set_callback(self):
        cv.setMouseCallback(self.name,self.__on_mouse)
        print("コールバック関数を追加しました。")

    def __on_mouse(self,e,x,y,flags,param):
        if e == cv.EVENT_LBUTTONDBLCLK:
            layer_num = len(self.layer_list)
            layer_name = 'circle' + str(layer_num)
            self.__add_circle(x,y,layer_name)
            
    def __add_circle(self,x,y,name):
        circle = Circle_Layer.Circle_Layer(x,y,name)
        self.layer_list.append(circle)
        print("レイヤリストにcircleを追加しました")

    def clear_layer_list(self):
        self.layer_list.clear()
        self.image = self.src_image.copy()
        print("レイヤリストをクリアしました。")

