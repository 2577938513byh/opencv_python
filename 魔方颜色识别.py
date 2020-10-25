import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def nothing(x):
    pass

each_faces  = np.zeros((6, 200, 200, 3), np.uint8)  #魔方的六个面
str_facenames = ["white", "yellow", "red", "origin", "green", "blue"]
each_faces[0] = cv.imread('red.png')
each_faces[1] = cv.imread('green.png')
each_faces[2] = cv.imread('cube_2.png')
each_faces[3] = cv.imread('cube_3.png')
each_faces[4] = cv.imread('cube_4.png')
each_faces[5] = cv.imread('cube_5.png')

# 拼接图片
img0 = np.zeros((200, 600, 3), np.uint8)
img1 = np.zeros((200, 600, 3), np.uint8)
img = np.zeros((400, 600, 3), np.uint8)
cv.hconcat((each_faces[:3]), img0)
cv.hconcat((each_faces[3:6]), img1)
cv.vconcat((img0, img1), img)

# 去除红色边框线，替换成黑色
img[0,:] = (0,0,0)
img[200,:] = (0,0,0)
img[:,0,:] = (0,0,0)
img[:,200,:] = (0,0,0)
img[:,400,:] = (0,0,0)

img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#plt.hist(img_hsv[:,:,0].ravel(), 180)
#print(max(img_hsv[:,:,0].ravel()))
#plt.imshow(img)
#plt.show()
low = 0
up = 180
cv.namedWindow('img',cv.WINDOW_NORMAL)
cv.createTrackbar('H_low', 'img', 0, 255, nothing)
cv.createTrackbar('H_up', 'img', 0, 255, nothing)
cv.createTrackbar('S_low', 'img', 0, 255, nothing)
cv.createTrackbar('S_up', 'img', 0, 255, nothing)
cv.createTrackbar('V_low', 'img', 0, 255, nothing)
cv.createTrackbar('V_up', 'img', 0, 255, nothing)
print("helle world")

while True:
    H_low = cv.getTrackbarPos('H_low', 'img')
    H_up = cv.getTrackbarPos('H_up', 'img')
    S_low = cv.getTrackbarPos('S_low', 'img')
    S_up = cv.getTrackbarPos('S_up', 'img')
    V_low = cv.getTrackbarPos('V_low', 'img')
    V_up = cv.getTrackbarPos('V_up', 'img')
    lower_white = np.array([H_low, S_low, V_low])
    upper_white = np.array([H_up, S_up, V_up])
#lower_white = np.array([0, 0, 201])
#upper_white = np.array([180, 50, 255])
    white_mask = cv.inRange(img_hsv, lower_white, upper_white)
    cv.imshow('white_mask', white_mask)
    cv.imshow('img', img)
    cv.waitKey(1)

#cv.imshow('hist', hist)
#cv.imshow('img0', img0)
#cv.imshow('img1', img1)
cv.imshow('img', img)
cv.imwrite('img.png', img)
cv.waitKey(0)