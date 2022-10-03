import cv2
import glob
import numpy as np

img1 = cv2.imread('./images/Qc/img1.jpg',0)  #queryimage # left image
img2 = cv2.imread('./images/Qc/img2.jpg',0) #trainimage # right image

def click_event1(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,' ', y)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img1,str(x)+ ',' + str(y),(x,y),font,0.5,(0,255,0),1)
        cv2.circle(img1, (x, y), radius=2, color=(0, 0, 255), thickness=-1)
        cv2.imshow('image1', img1)
        points_img1.append([x,y])

def click_event2(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,' ', y)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img2,str(x)+ ',' + str(y),(x,y),font,0.5,(0,255,0),1)
        cv2.circle(img2, (x, y), radius=2, color=(0, 0, 255), thickness=-1)
        cv2.imshow('image', img2)
        points_img2.append([x, y])


img1 = cv2.imread('./images/Qc/img1.jpg')
img2 = cv2.imread('./images/Qc/img2.jpg')

points_img1 = []
points_img2 = []

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)


cv2.setMouseCallback('img1', click_event1)
cv2.setMouseCallback('img2', click_event2)


cv2.waitKey(0)
cv2.destroyAllWindows()

points1 = np.array(points_img1)
points2 = np.array(points_img2)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

pattern_size = (6,8) #check boardsize

objp = np.zeros(( pattern_size[0]*pattern_size[1],3), np.float32)
objp[:,:2] = np.mgrid[0:pattern_size[0],0:pattern_size[1]].T.reshape(-1,2)

objPoints = [] # 3d points
imgPoints = [] # 2d points

images = glob.glob('./images/Qb/*.jpg')

#the below intrinsic matrix can be found questionB.py output
intrinsic_mtx = np.array([[887.68446239, 0, 444.96221361],
                [0, 888.57426661, 455.886891],
                [0, 0, 1]])

E, mask = cv2.findEssentialMat(points1,points2,intrinsic_mtx)

print("intrinsic matrix: \n", E)

R1, R2, t = cv2.decomposeEssentialMat(E)

print("\n1st possible Rotation Matrix\n:", R1)
print("\n2nd possible Rotation Matrix\n", R2)
print("\nTranslation Matrix\n", t)