import cv2 as cv

img = cv.imread('jc2.jpg')

cv.imshow('qwe',img)
cv.waitKey(1600)
img = cv.resize(img,(480,480))

cv.imshow('qwe',img)
cv.waitKey(600)