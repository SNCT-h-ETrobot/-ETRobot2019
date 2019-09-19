#プログラムの流れ
# 座標を取得する
## カメラからフレームを取得する
## 
## 
## 

# サーバを立ち上げる
# リクエストコードによって処理を分岐する
# レスポンスを返す
import cv2 as cv 
import numpy as np
from Window import Window
from SerialInterface import SerialInterface
from Color import Color
# class Window:
#     pass
# class Server:
#     pass
# class Service:
#     pass
# class Request:
#     pass
# class Response:
#     pass

# class caribrator():
#     def __init__(self):
#         pass 
def doNothing(any):
    pass


print("start")
origin = cv.imread ("../develop/picture/et001.PNG")
main_window = Window("caribration")
main_window.set_image(origin)
main_window.set_callback()

settings = {
    "number":{},
    "color":{
        "threshold":{
            'black': {'min': np.array([0, 0, 0], dtype=np.uint8), 'max': np.array([31, 39, 31], dtype=np.uint8)}, 
            'red': {'min': np.array([ 0,  0, 52], dtype=np.uint8), 'max': np.array([ 31,  39, 255], dtype=np.uint8)
            }
            }
        ,
        "coordinates": [[187, 59], [222, 94], [216, 168], [130, 201]]
        ,'pers_M': np.array([[ 5.49765138e-01, -1.52853775e+00,  1.64570446e+02],
       [ 1.10134587e+00,  2.18402486e+00, -3.78545642e+02],
       [ 2.52677525e-04,  7.85198130e-03,  1.00000000e+00]])
        }
}
 
# settings = {
    #   number:{
    #       pers_M:x,
    #       threshold:n
    #   },
    #   color:{
    #       pers_M:x,  
    #       threshold:{
    #           "black":n,
    #           "red":n,
    #           "yellow":n,
    #           "green":n,
    #           "blue":n,
    #       },
    #       coordinates:[[n,n,n,n],
    #                    [n,n,n,n],
    #                    [n,n,n,n],
    #                    [n,n,n,n]]
    #   }
    # }



print("キャリブレーションを開始します")
while(1):
    main_window.show_image()
    # カメラから画像を取得するように変更する必要がある
    k = cv.waitKey(1)
    if k == 27 :# キャリブレーションを終了する Esc
        print("キャリブレーションを終了します")
        # ここに設定値を表示するプログラムを追加する
        print(settings)
        break
    elif k == ord('a'):#座標指定プログラム
        coordinates = main_window.get_layers_coordinates()
        if len(coordinates) != 4:
            print("座標を4つ指定してください") 
            continue
        print("座標をセットしました")
    elif k == ord('s'):# 数字検出の設定
        num_window = Window("num_window")
        # 視点の変換
        pts1 = np.float32(coordinates)
        pts2 = np.float32([[0,0],[255,0],[0,255],[255,255]])
        M = cv.getPerspectiveTransform(pts1,pts2)
        settings["number"]["pers_M"] = M 
        dst = cv.warpPerspective(main_window.src_image,M,(255,255))
        num_window.set_image(dst)
        
        print("数字を選択しました")
        num_window.show_image()
        # 切り出し
        print("数字認識のための、前処理を開始します\n"\
        "threshold ウィンドウのトラックバーを動かして、しきい値を設定してください")
        cv.createTrackbar('threshold',num_window.name,0,255,doNothing)
        while (1):
            k = cv.waitKey(1) 
            threshold = cv.getTrackbarPos('threshold',num_window.name)
            _,num_window.image = cv.threshold(num_window.src_image,threshold,255,cv.INTER_CUBIC)
            num_window.show_image()
            if k == ord('s') :
                settings["number"]["threshold"] = cv.getTrackbarPos('threshold',num_window.name)                
                print("しきい値の設定を終了します")
                print("threshold : " + str(settings["number"]["threshold"]))
                cv.destroyWindow(num_window.name)
                break
    elif k == ord('x'):# カラー検出の設定
        color_window = Window("color_window")
        # 視点の変換
        pts1 = np.float32(coordinates)
        pts2 = np.float32([[0,0],[255,0],[0,255],[255,255]])
        M = cv.getPerspectiveTransform(pts1,pts2)
        settings['color']['pers_M'] = M
        dst = cv.warpPerspective(main_window.src_image,M,(255,255))

        color_window.set_image(dst)
        color_window.show_image()
        print("ビンゴ区間を選択しました")

        print ("色のしきい値の設定を開始してください")
        cv.createTrackbar('maxB',color_window.name,0,255,doNothing)
        cv.createTrackbar('minB',color_window.name,0,255,doNothing)
        cv.createTrackbar('maxG',color_window.name,0,255,doNothing)
        cv.createTrackbar('minG',color_window.name,0,255,doNothing)
        cv.createTrackbar('maxR',color_window.name,0,255,doNothing)
        cv.createTrackbar('minR',color_window.name,0,255,doNothing)
        while(1):# しきい値の設定
            k = cv.waitKey(1)           
            color_window.show_image()
            max_h = cv.getTrackbarPos('maxB',color_window.name)
            min_h = cv.getTrackbarPos('minB',color_window.name)
            max_s = cv.getTrackbarPos('maxG',color_window.name)
            min_s = cv.getTrackbarPos('minG',color_window.name)
            max_v = cv.getTrackbarPos('maxR',color_window.name)
            min_v = cv.getTrackbarPos('minR',color_window.name)
            min_range = np.array([min_h,min_s,min_v],np.uint8)
            max_range = np.array([max_h,max_s,max_v],np.uint8)
            ranged = cv.inRange(color_window.src_image,min_range,max_range)
            color_window.image = ranged
          
            if k == ord('c'):# 黒
                settings['color']['threshold']['black'] = {}
                settings['color']['threshold']['black']['min'] = min_range
                settings['color']['threshold']['black']['max'] = max_range
                print("黒のしきい値を設定しました")
                print("black:"+str(settings['color']['threshold']['black']))
            elif k == ord('v'):# 赤
                settings['color']['threshold']['red'] = {}
                settings['color']['threshold']['red']['min'] = min_range
                settings['color']['threshold']['red']['max'] = max_range
                print("赤のしきい値を設定しました")
                print("red:"+str(settings['color']['threshold']['red']))
            elif k == ord('b'):# 青
                settings['color']['threshold']['blue'] = {}
                settings['color']['threshold']['blue']['min'] = min_range
                settings['color']['threshold']['blue']['max'] = max_range
                print("青のしきい値を設定しました")
                print("blue:"+str(settings['color']['threshold']['blue']))
            elif k == ord('n'):# 黄色
                settings['color']['threshold']['yellow'] = {}
                settings['color']['threshold']['yellow']['min'] = min_range
                settings['color']['threshold']['yellow']['max'] = max_range
                print("黄のしきい値を設定しました")
                print("yellow:"+str(settings['color']['threshold']['yellow']))
            elif k == ord('m'):# 緑
                settings['color']['threshold']['green'] = {}
                settings['color']['threshold']['green']['min'] = min_range
                settings['color']['threshold']['green']['max'] = max_range
                print("緑のしきい値を設定しました")
                print("green:"+str(settings['color']['threshold']['green']))
            elif k == ord('x'):# 終了
                print("しきい値の設定を終了します\n座標の設定を行ってください")
                print("color threshold :" + str (settings['color']['threshold']))
                cv.destroyWindow(color_window.name)
                break

    elif k == ord('c'):# 色を検出する座標の設定
        print("座標の設定を開始します")
        try:
            coordinate_window = Window("coordinate")
        except:
            pass
        dst = cv.warpPerspective(main_window.src_image,settings['color']['pers_M'],(255,255))
        coordinate_window.set_image(dst)
        coordinate_window.set_callback()
        while(1):
            k = cv.waitKey(1)
            coordinate_window.show_image()
            if k == ord('c'):
                settings['color']['coordinates'] = coordinate_window.get_layers_coordinates()
                print('座標の指定を終了します')
                print('coordinates:'+str(settings['color']['coordinates']))
                break
    elif k == ord('t'): # 座標取得テスト
        image = cv.warpPerspective(main_window.src_image,settings['color']['pers_M'],(255,255))
        size= 5
        cv.imshow("test",image)
        color_filter = Color(settings['color']['threshold'],settings['color']['coordinates'])
        for coord in color_filter.coordinates:
            x,y = coord
            
            result = color_filter.get_color(image[y-size:y+size,x-size:x+size])
            cv.imshow(str(coord),cv.resize(image[y-size:y+size,x-size:x+size],(255,255)))

            print("座標:" + str (coord) + "  "+str(result))
    elif k == ord('r'):# 取得している座標をリセット
        print ("設定した座標をリセットします")
        main_window.clear_layer_list()



# port  = "COM6"
# baud = 115200
# si = SerialInterface.SerialInterface()
# si.open(port,baud,None)
# # 競技中のプログラム
# while(1):
#     try:
#         command ,parameter = si.read()
#         print("(command, parameter) = ", (command, parameter))
#         # if command == ???? 数字を読み取って送り返す　とかそんな感じで処理を書いていく
#     except KeyboardInterrupt:
#         si.close()
