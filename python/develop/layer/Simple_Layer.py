import numpy as np
import cv2 as cv 

class Simple_Layer:
    def __init__(self,path):
        self.name = path
        self.image = cv.imread(path)
    def show_layer(self):
        cv.imshow(self.name,self.image)