#!/usr/bin/env python
# coding: utf-8
import cv2 as cv
import numpy as np  

# 色に関する定義
class Color():
    # 色コード
    def __init__(self,threshold,coordinates):
        self.dictionary = {
            0:"UNKNOWN",
            1:"RED",
            2:"GREEN",
            3:"BLUE",
            4:"BLACK",
            5:"YELLOW",
        }
        self.threshold = threshold
        self.coordinates = coordinates
    # 色コードから表示用文字列への変換メソッド
    def toColorName(self,code):
        return self.dictionary[code]
    # HSV値から色コードへの変換メソッド(閾値は環境に合わせて調整下さい)
    def get_color(self,BGR):
        count = {}
        for color in  self.threshold:
            # print(self.threshold[color])
            ranged = cv.inRange(BGR,self.threshold[color]['min'],self.threshold[color]['max'])
            count[color] = np.count_nonzero(ranged == 255)
            cv.imshow(str(color),ranged)
            if  count[color] >= 1:
                return color

        return count

# settings = {'number': {},
#  'color': {
#       'threshold': {
#           'black': {'min': np.array([0, 0, 0], dtype=np.uint8), 'max': np.array([42, 36, 31], dtype=np.uint8)}, 
#           'red': {'min': np.array([ 0,  0, 42], dtype=np.uint8), 'max': np.array([ 42,  36, 255], dtype=np.uint8)},
#           'blue': {'min': np.array([47,  0,  0], dtype=np.uint8), 'max': np.array([255, 255,  29], dtype=np.uint8)},
#           'yellow': {'min': np.array([ 0, 62, 36], dtype=np.uint8), 'max': np.array([ 31, 128, 143], dtype=np.uint8)}, 
#           'green': {'min': np.array([ 0, 36,  0], dtype=np.uint8), 'max': np.array([ 47, 255,  39], dtype=np.uint8)}}, 
#       'pers_M': np.array([[ 4.82884196e-01, -1.51283340e+00,  1.74904934e+02],
#        [ 1.05398686e+00,  2.09055244e+00, -3.57022804e+02],
#        [ 1.63995858e-04,  7.62417460e-03,  1.00000000e+00]]), 'coordinates': [[17, 18], [81, 20], [146, 22], [205, 28], [19, 92], [86, 85], [151, 87], [221, 97], [16, 163], [84, 161], [148, 163], [216, 169], [18, 239], [85, 236], [149, 235], [218, 242]]}}

# image = cv.imread("../develop/picture/et001.PNG")
# coordinates = settings['color']['coordinates']
# threshold = settings['color']['threshold']
# color_filter = Color(threshold,coordinates)
# for coord in coordinates:
#     x,y = coord
#     print(color_filter.get_color(image[x,y]))
