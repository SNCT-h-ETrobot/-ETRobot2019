import cv2 as cv
import numpy as np
import colorsys
from matplotlib import pyplot as plt
import copy

file_path_01 = "picture/et001.PNG"

def get_hsv_colors():
    color_upper = []
    color_lower = []
    for i in range (60,80,1):
        color_lower.append(np.array([i,50,50]))
        color_upper.append(np.array([i+10,250,250]))
    return (color_lower,color_upper)
color_data = get_hsv_colors()
debug_data = copy.deepcopy(color_data)
img = cv.imread(file_path_01)

hsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)
for i in range(0,len(color_data[0])):
    print(str(i)+": upper: " + str(debug_data[1].pop()))
    print(str(i)+": lower: " + str(debug_data[0].pop()))
    got_image = cv.inRange(hsv_img,color_data[0].pop(),color_data[1].pop())
    show_image = cv.cvtColor(got_image,cv.COLOR_GRAY2BGR)
    cv.imshow('got_image'+str(i),show_image)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()