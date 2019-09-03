import numpy as np
import cv2 as cv 

class Circle_Layer:
    def __init__(self,x,y,name):
        self.name = name
        self.image = np.zeros((512,512,3),np.uint8)
        cv.circle(self.image,(x,y),5,(0,0,255),-1)
        self.coordinate = np.array([x,y])
    def get_coordinate(self):
        return self.coordinate
    def set_coordinate(self,coordinate):
        self.coordinate = coordinate
    def shift_coordinate(self,shift):
        self.coordinate = self.coordinate + shift
    def show_layer(self):
        cv.imshow(self.name,self.image)
