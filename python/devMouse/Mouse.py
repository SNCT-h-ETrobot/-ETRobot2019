import cv2 as cv 
import numpy as np
from Circle import Circle_List
windows = ["dev"]
src_image = cv.imread("../develop/picture/et001.PNG")
for window_name in windows:
    cv.namedWindow(window_name)

param = {"circle_moving":False,"circle" : None}
def pile_image(x,y,back_image,fore_image):
    #background=>b,foreground=>f,start=>s, 
    # reference:https://www.tech-tech.xyz/clip_image.html
    back_h,back_w = back_image.shape[:2]
    fore_h,fore_w = fore_image.shape[:2]
    fore_w = min(fore_w,back_w - x)
    fore_h = min(fore_h,back_h - y)
    start_x = min(max(-x,0),fore_w)
    start_y = min(max(-y,0),fore_h)
    back_image[max(y,0):y+fore_h,max(x,0):x+fore_w] = fore_image[start_y:start_y+fore_h,start_x:start_x + fore_w]

circle_list = Circle_List()
selected_circle = 0
moving = False

def callback(e,x,y,flgas,param):
    global circle_list,selected_circle,moving
    if e == cv.EVENT_LBUTTONDBLCLK:
        # 選択できるサークルを増やす
        circle_list.add_circle(x,y)
        print("サークルを追加しました")
    elif e == cv.EVENT_LBUTTONDOWN:
        # サークルの位置変更を許可する
        moving = True
    elif e == cv.EVENT_MOUSEMOVE:
        # 選択しているサークルの位置を変更する
        if moving == True:
            circle_list.move_circle(selected_circle,x,y)
    elif e == cv.EVENT_LBUTTONUP:
        # サークルの位置変更を禁止する
        if moving == True:
            moving = False
            print(vars(circle_list))

cv.setMouseCallback("dev",callback,param)

while(1):
    image = src_image.copy()
    k = cv.waitKey(1)
    if len(circle_list.list) != 0:
        for circle in circle_list.list:
            x = circle.get_x()
            y = circle.get_y()
            pile_image(x,y,image,circle.image)
    cv.imshow("dev",image)
    if k == 27 :
        print("プログラムを終了します")
        break 

