import cv2

if __name__ == '__main__':
    imgPath = 'haar_carplate.xml'
    img = cv2.imread('testCar/cartest3.jpg')
    car_cascade = cv2.CascadeClassifier(imgPath)

    plates = car_cascade.detectMultiScale(img, scaleFactor=1.05, minNeighbors=3, minSize=(20, 20), maxSize=(155,50))
    if len(plates) > 0:
        for(x, y, w, h) in plates:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            print(plates)
    else:
        print('Detect failed.')

    cv2.imshow('Plate Detected', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()