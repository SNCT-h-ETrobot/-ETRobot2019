import cv2 as cv 
from layer import Simple_Layer,Circle_Layer
from perspective import Window

def callback(e,x,y,flags,param):
    if e == cv.EVENT_LBUTTONDOWN:
        return "Left button pushed"


origin = Simple_Layer.Simple_Layer("picture/et001.PNG")
window = Window.Window("origin",origin.image)
x,y = origin.image.shape[:2]
layer = Simple_Layer.Simple_Layer("picture/sample.PNG")
window.pile_image(255,255,layer.image)
window.get_circle()
#print(window.layer_list[0].show_image()
window.layer_list[0].show_layer()
window.set_callback()



while(1):
    window.show_image()
    k = cv.waitKey(1)
    if k == 27:
        break