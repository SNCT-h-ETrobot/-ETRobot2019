import cv2 as cv

file_path_01 = "./picture/src/silas-baisch-1696770-unsplash.jpg"
img = cv.imread(file_path_01)
for min in range(0,300,20):
    for max in range(0,300,20):
        print(str(min)+'-'+str(max))
        dst = './picture/dst/'+str(min)+'-'+str(max)+'-001.jpg'
        cannied_img = cv.Canny(img,min,max)
        cv.imwrite(dst,cannied_img)
print("done")