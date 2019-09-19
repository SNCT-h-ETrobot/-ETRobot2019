import numpy as np
import cv2 as cv 

class Circle_Layer:
    def __init__(self,x,y,name):
        self.name = name
        self.image = np.zeros((10,10,3),np.uint8)
        cv.circle(self.image,(5,5),5,(0,0,255),-1)
        self.x = x 
        self.y = y      
    def set_coordinate(self,coordinate):
        self.coordinate = coordinate
    def get_coordinate (self):
        return [self.x,self.y]
    def shift_coordinate(self,shift):
        self.coordinate = self.coordinate + shift
    def show_layer(self):
        cv.imshow(self.name,self.image)

