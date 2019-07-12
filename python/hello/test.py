import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

file_path_01 = "../picture/et001.PNG"

def show_image_with_cv(file_path):
    img = cv.imread(file_path,1)
    cv.imshow(file_path,img)    
    cv.waitKey(0)
    cv.destroyAllWindows()
def show_image_with_matplotlib(file_path):
    src_img = cv.imread(file_path,1)
    img = src_img[:,:,::-1]
    plt.imshow(img,cmap='rgb',interpolation='bicubic')
    plt.xticks([]),plt.yticks([])
    plt.show()
#show_image_with_matplotlib(full_path)

img = cv.imread(file_path_01)
print(img)

