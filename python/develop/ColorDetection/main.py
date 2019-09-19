import cv2 as cv
import numpy as np
import colorsys
from matplotlib import pyplot as plt
import copy
import Color
import ColorSet

show_image_list=[]

count = 0
file_path_01 = "picture/et001.PNG"
img = cv.imread(file_path_01)
key = ['red','green','blue','yellow']
each_color_image = Color.get_each_color_image(key,img,"")
cv.imshow('origin',img)
cv.waitKey(0)
cv.destroyAllWindows()
