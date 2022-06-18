import cv2, os, glob, shutil, time

if __name__ == '__main__':
    srcDir = 'notCar'
    dstDir = 'notCarGray'

    width = 500
    height = 400
    
    if os.path.isdir(dstDir):
        shutil.rmtree(dstDir)
        time.sleep(3)
    os.mkdir(dstDir)

    allcars = srcDir + '/*.jpg'
    cars = glob.glob(allcars)
    for index, car in enumerate(cars, 1):
        img = cv2.imread(car, cv2.IMREAD_GRAYSCALE)
        img_resize = cv2.resize(img, (width, height))
        imgname = 'notCar' + str(index)
        fullpath = dstDir + '/' + imgname + '.jpg'
        cv2.imwrite(fullpath, img_resize)
    print('....Done.')