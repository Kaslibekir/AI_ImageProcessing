import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

blank[200:300, 100:150] = 0,0,255
cv.imshow('Red',blank)

cv.waitKey(0)