import cv2
import os
import glob
import time
import shutil

if __name__ == '__main__':
    dstDir = 'dstCar'
    bmpDir = 'bmpCar'

    if os.path.isdir(bmpDir):
        shutil.rmtree(bmpDir)
        time.sleep(3)
    os.mkdir(bmpDir)

    allcars = dstDir + '/*.jpg'
    cars = glob.glob(allcars)
    for car in cars:
        carname = car.split('/')
        car_img = cv2.imread(car, cv2.IMREAD_COLOR)
        outname = carname[1].replace('.jpg', '.bmp')
        fullpath = bmpDir + '/' + outname
        cv2.imwrite(fullpath, car_img)
    print('...Done.')