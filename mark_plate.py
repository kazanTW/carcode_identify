import cv2, os, shutil, time

if __name__ == '__main__':
    dstDir = 'plate-mark'
    path = 'Haar-Training-car-plate/training/positive/'

    if os.path.isdir(dstDir):
        shutil.rmtree(dstDir)
        time.sleep(3)
    os.mkdir(dstDir)

    fn = open(path + 'info.txt', 'r')
    row = fn.readline()
    while row:
        msg = row.split(' ')
        img = cv2.imread(path + msg[0])
        n = int(msg[1])
        for i in range(n):
            x = int(msg[2 + i * 4])
            y = int(msg[3 + i * 4])
            w = int(msg[4 + i * 4])
            h = int(msg[5 + i * 4])
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        imgname = (msg[0].split('/'))[-1]
        print(f'{imgname} marked.')
        cv2.imwrite(dstDir + '/' + imgname, img)
        row = fn.readline()
    fn.close()
    print('\nMark done.')