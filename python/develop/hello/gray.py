import cv2 as cv
import numpy as np
import colorsys
from matplotlib import pyplot as plt
import copy
import color
import ColorSet

def get_each_color_image(key,img,label):
        image_list = []
        color_range = color.set_color(key,color_dict)
        color_range['black'] = {}
        color_range['black']['min'] = np.array([0,0,0],np.uint8)
        color_range['black']['max'] = np.array([180,80,80],np.uint8)
        key.append('black')

        hsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)

        images = color.get_each_filtered_image(key,hsv_img,color_range)
        cvted_images = color.convert_images(key,copy.deepcopy(images))

        for i in key:
                image_list.append(cvted_images[i]['bgr'])
                cv.imshow(str(label)+i,cvted_images[i]['bgr'])
        # cv.imshow(str(label)+'original',img)
        cv.waitKey(0)
        return image_list

count = 0
file_path_01 = "picture/et001.PNG"
img = cv.imread(file_path_01)

key = ['red','green','blue','yellow']
color_dict = ColorSet.color_dictionary
# gaussian_image_obj = get_gaussian_images(img)

each_color_image = get_each_color_image(key,img,"")


#images = get_gaussian_image(img)
canny_img = cv.Canny(img,100,200)
image,contours,hierarchy = cv.findContours(canny_img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

ext = np.zeros(image.shape)

ext = cv.drawContours(ext,contours,-1,(0,255,0),-1)
cv.imshow('contours',ext)
cv.imshow('canny',canny_img)
cv.imshow('image',img)

cv.waitKey(0)
cv.destroyAllWindows()
