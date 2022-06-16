import cv2
import os
import glob
import time
import shutil

if __name__ == '__main__':
    srcDir = 'srcCar'
    dstDir = 'dstCar'
    width = 320
    height = 240

    if os.path.isdir(dstDir):
        shutil.rmtree(dstDir)
        time.sleep(3)
    os.mkdir(dstDir)
    cars = glob.glob(srcDir + '/*.png')
    print(f'Resize files in {srcDir}....')
    for index, car in enumerate(cars, 1):
        img_car = cv2.imread(car, cv2.IMREAD_COLOR)
        car_name = 'car' + str(index) + '.jpg'
        fullpath = dstDir + '/' + car_name
        cv2.imwrite(fullpath, img_car)
    print(f'Save files in {dstDir}....')