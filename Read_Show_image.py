import cv2 as cv

img = cv.imread('cat.png')


cv.imshow('Cat',img)

def rescaleFrame(frame, scale=0.60):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA )

frame_resized = rescaleFrame(img)
cv.imshow('Resized_Cat',frame_resized)
cv.waitKey(0)