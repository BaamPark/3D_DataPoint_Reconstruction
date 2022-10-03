import cv2
import numpy as np

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

if __name__ == "__main__":
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

    print(points_img1)
    points1 = np.array(points_img1)
    print(points1)