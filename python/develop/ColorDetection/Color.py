import numpy as np
import cv2 as cv
import copy
import ColorSet
min_s = 50
max_s = 250
min_v = 50
max_v = 250

def set_color(keys,c_dict):
    output = {}
    for i in keys:
        output[i] = {}
        output[i]['min'] = np.array([c_dict[i]['min'],min_s,min_v],np.uint8)
        output[i]['max'] = np.array([c_dict[i]['max'],max_s,max_v],np.uint8)
    return copy.deepcopy(output)

def get_each_filtered_image(keys,src_img,color_range):
    output = {}
    for i in keys:
        output[i] = {}
        output[i]['gray'] = cv.inRange(src_img,color_range[i]['min'],color_range[i]['max'])
    return copy.deepcopy(output)

def convert_images(keys,src_images_copy):
    for i in keys:
        src_images_copy[i]['bgr'] = cv.cvtColor(src_images_copy[i]['gray'],cv.COLOR_GRAY2BGR)
    return  copy.deepcopy(src_images_copy)

def get_each_color_image(key,img,label):
        
        image_list = []
        color_range = set_color(key,ColorSet.color_range_set)
        color_range['black'] = {}
        color_range['black']['min'] = np.array([0,0,0],np.uint8)
        color_range['black']['max'] = np.array([180,80,80],np.uint8)
        key.append('black')

        hsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)

        images = get_each_filtered_image(key,hsv_img,color_range)
        cvted_images = convert_images(key,copy.deepcopy(images))

        for i in key:
                image_list.append(cvted_images[i]['bgr'])
                cv.imshow(str(label)+i,cvted_images[i]['bgr'])
        cv.waitKey(0)
        return image_list