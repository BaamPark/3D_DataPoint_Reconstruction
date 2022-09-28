import cv2

def click_event1(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,' ', y)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img1,str(x)+ ',' + str(y),(x,y),font,0.5,(0,255,0),1)
        cv2.circle(img1, (x, y), radius=2, color=(0, 0, 255), thickness=-1)
        cv2.imshow('image1', img1)

def click_event2(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,' ', y)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img2,str(x)+ ',' + str(y),(x,y),font,0.5,(0,255,0),1)
        cv2.circle(img2, (x, y), radius=2, color=(0, 0, 255), thickness=-1)
        cv2.imshow('image', img2)

if __name__ == "__main__":
    img1 = cv2.imread('img1.jpg')
    img2 = cv2.imread('img2.jpg')
    width = 500
    height = 500
    dim = (width, height)
    img1 = cv2.resize(img1, dim)
    img2 = cv2.resize(img2, dim)
    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)


    cv2.setMouseCallback('img1', click_event1)
    cv2.setMouseCallback('img2', click_event2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

