import cv2 as cv 
import numpy as np 
from keras.models import load_model

from layer import Simple_Layer,Circle_Layer 
from perspective import Window 
from NumDetect import NumFilter

def nothing(x):
    pass


origin = cv.imread("picture/et001.PNG") 
model = load_model("./NumDetect/MNIST.h5")
num_filter = NumFilter.NumFilter(model)
main_window = Window.Window("main")
main_window.set_image(origin)
main_window.set_callback() 
num_window = Window.Window("num threshold")
cv.createTrackbar('threshold',num_window.name,0,255,nothing)
    

while(1): 
    main_window.show_image() 
    k = cv.waitKey(1) 
    if k == 27:# shutdown # ascii 27 => "Esc" key 
        print("プログラムを終了します")
        break
    elif k == ord('a'):# perspective transform 
        print("変換を行います")
        # get coordinate of circles 
        coordinates = main_window.get_layers_coordinates()
        if len(coordinates) != 4:
            print("座標を4つ指定してください") 
            continue
        pts1 = np.float32(coordinates)
        pts2 = np.float32([[0,0],[255,0],[0,255],[255,255]])
        M = cv.getPerspectiveTransform(pts1,pts2)
        dst = cv.warpPerspective(main_window.src_image,M,(255,255))
        num_window.set_image(dst.copy())
        num_window.show_image()
    elif k == ord('s'):#number detecting 
        image = cv.cvtColor(num_window.src_image,cv.COLOR_BGR2GRAY)
        num_window.set_image(image)
        while(1):
            threshold = cv.getTrackbarPos('threshold',num_window.name)
            _,num_window.image = cv.threshold(num_window.src_image,threshold,255,cv.INTER_CUBIC)
            num_window.show_image()
            k= cv.waitKey(10)
            if k == ord('s'):
                num_filter.set_image(num_window.image)
                num_filter.set_threshold(threshold)
                print("画像をフィルタにセットしました")
                break
    elif k == ord('d'):
        print(num_filter.detect_number())        
    elif k == ord('r'):# reset layer 
        print("座標をリセットします")
        main_window.clear_layer_list()
