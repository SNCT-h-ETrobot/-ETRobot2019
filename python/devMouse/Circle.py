import cv2 as cv 
import numpy as np 
class Circle:
    def __init__ (self,name,x,y):
        self.name = name
        self.x = x
        self.y = y 
        self.image = np.zeros((10,10,3),np.uint8)
        cv.circle(self.image,(5,5),5,(0,255,0),-1)

    def create(self,x,y):
        self.x = x 
        self.y = y
    def update(self,x,y):
        self.x = x
        self.y = y 
    def get_x(self):
        return self.x 
    def get_y(self):
        return self.y 
    def get(self):
        return (self.x,self.y)    
    def show_image(self):
        cv.imshow(self.name,self.image)

class Circle_List:
    def __init__ (self):
        self.list = []
    def __len__(self):
        return len(self.list)
    def add_circle(self,x,y):
        self.list.append(Circle(str(len(self.list)),x,y))
    def get_circle(self,num):
        return self.list[num]
    def move_circle(self,num,x,y):
        self.list[num].update(x,y)
    def get_coordinates(self):
        coordinates= []
        for circle in self.list:
            coordinates.append((circle.get_x(),circle.get_y()))
        return coordinates
    def remove_circle(self,num):
        self.list.pop(num)
    def clear(self):
        self.list.clear()

circle_list = Circle_List()
circle_list.add_circle(5,5)
print(vars(circle_list))
circle_list.clear()
print(vars(circle_list))

