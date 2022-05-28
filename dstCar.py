import cv2
import os
import glob
import time
import shutil

if __name__ == '__main__':
    srcDir = 'srcCar'
    dstDir = 'dstDir'
    width = 320
    height = 240

    if os.path.isdir(dstDir):
        shutil.rmtree(dstDir)
        time.sleep(3)
    os.mkdir(dstDir)
    cars = glob.glob(srcDir + '/*.jpg')
    print(f'Resize files in {srcDir}....')
    for index, car in enumerate(cars, 1):
        img_car = cv2.imread(car, cv2.IMREAD_COLOR)
        img_cat_resize = cv2.resize(img_car, (width, height))
        car_name = 'car' + str(index) + '.jpg'
        fullpath = dstDir + '/' + car_name
        cv2.imwrite(fullpath, img_cat_resize)
    print(f'Save files in {dstDir}....')