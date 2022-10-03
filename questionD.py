import cv2
import numpy as np
from matplotlib import pyplot as plt

def linear_triangulation(p1, p2, m1, m2):
    num_points = p1.shape[1]
    res = np.ones((4, num_points))

    for i in range(num_points):
        A = np.asarray([
            (p1[0, i] * m1[2, :] - m1[0, :]),
            (p1[1, i] * m1[2, :] - m1[1, :]),
            (p2[0, i] * m2[2, :] - m2[0, :]),
            (p2[1, i] * m2[2, :] - m2[1, :])
        ])

        _, _, V = np.linalg.svd(A)
        X = V[-1, :4]
        res[:, i] = X / X[3]

    return res

def click_event1(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,' ', y)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img1,str(x)+ ',' + str(y),(x,y),font,0.5,(0,255,0),1)
        cv2.circle(img1, (x, y), radius=2, color=(0, 0, 255), thickness=-1)
        cv2.imshow('image1', img1)
        points_img1.append([[x],[y]])

def click_event2(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,' ', y)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img2,str(x)+ ',' + str(y),(x,y),font,0.5,(0,255,0),1)
        cv2.circle(img2, (x, y), radius=2, color=(0, 0, 255), thickness=-1)
        cv2.imshow('image', img2)
        points_img2.append([[x], [y]])


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
points_img1_container = []
for point in points_img1:
    point = np.array(point)
    point = np.vstack((point, 1))
    points_img1_container.append(point)

points_img1_container = np.array(points_img1_container)

points_img2_container = []
for point in points_img2:
    point = np.array(point)
    point = np.vstack((point, 1))
    points_img2_container.append(point)

points_img2_container = np.array(points_img2_container)


    # points_img1container = np.append(point, [1], axis=1)

p1 = np.array([[307], [245], [1]])
p2 = np.array([[342], [247], [1]])

r = np.identity(3)
t = np.zeros((3,1))
projection_matrix_img1 = np.append(r, t, axis=1)

#rotation obtrained from questionB.py (used 1st rotation)
rotation = np.array([[-0.99297141, -0.01085732, -0.11785538],
                     [ 0.00627642, -0.99921283,  0.03917054],
                     [-0.1181879,   0.03815552,  0.99225792]])
#translation obtained from questionB.py
translation =  np.array([[ 0.07972497],
                         [-0.02157647],
                         [-0.99658336]])

projection_matrix_img2 = np.append(rotation, translation, axis=1)

# print(projection_matrix_img1)
# print(projection_matrix_img2)
x_list = []
y_list = []
z_list = []



for i in range(2):
    reval = linear_triangulation(points_img1_container[i], points_img2_container[i], projection_matrix_img1, projection_matrix_img2)
    x_list.append(reval[0][0])
    y_list.append(reval[1][0])
    z_list.append(reval[2][0])
    print(reval.shape)
    print(reval)


# reval_list = np.array(reval_list)
# print(reval_list)
# print(reval_list.shape)

# for i in range(2):
#     x_list.append[i][0][0]
#     y_list.append[i][1][0]
#     z_list.append[i][2][0]

print(x_list)
# reval = linear_triangulation(p1, p2, projection_matrix_img1, projection_matrix_img2)
# print(reval)

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# x = reval[0][0]
# y = reval[1][0]
# z = reval[2][0]
x = x_list
y = y_list
z = z_list
ax.scatter(x, y, z, c=z, alpha=1)
plt.show()

# print(reval)