import cv2
import numpy as np
import os
import glob

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

pattern_size = (6,8) #check boardsize

objp = np.zeros(( pattern_size[0]*pattern_size[1],3), np.float32)
objp[:,:2] = np.mgrid[0:pattern_size[0],0:pattern_size[1]].T.reshape(-1,2)

objPoints = [] # 3d points
imgPoints = [] # 2d points

images = glob.glob('./images/Qb/*.jpg')

for image in images:
    print(image)
    img = cv2.imread(image)
    img = cv2.resize(img, (900, 900))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray, pattern_size, None)  #ret: return of value

    # print(ret)
    # print(corners)

    if ret == True:
        objPoints.append(objp)
        corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
        imgPoints.append(corners)

        cv2.drawChessboardCorners(img, pattern_size, corners2, ret)
        cv2.imshow('img', img)
        cv2.waitKey(1000)

cv2.destroyAllWindows()


#calibration

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objPoints, imgPoints, gray.shape[::-1], None, None)

print("Camera Calibrated: ", ret)
print("\nCamera Matrix: \n", mtx)
print("\nDistortion Parameters: ", dist)
print("\nRotation Vectors:\n", rvecs)
print("\nTranslation Vectors:\n", tvecs)




