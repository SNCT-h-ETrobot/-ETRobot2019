import cv2 as cv 
import numpy as np 
from keras.models import load_model

class NumFilter:
    def __init__(self,model):
        self.model = model
    def set_image(self,image):
        self.image = image.copy()
    def set_threshold(self,threshold):
        self.threshold = threshold
    def change_image_size(self):
        self.image = cv.resize(self.image,dsize=(28,28))
    def image2binary(self):
        _,bin_image = cv.threshold(self.image,self.threshold,255,cv.INTER_CUBIC)
        self.image = cv.bitwise_not(bin_image)
    def gaussian_transform(self):
        self.image = cv.GaussianBlur(self.image,(3,3),0)
    def detect_number(self):
        self.image2binary()
        self.change_image_size()
        self.gaussian_transform()
        xt = []
        xt.append(self.image)
        xt = np.array(xt)/255
        return self.model.predict_classes(xt)