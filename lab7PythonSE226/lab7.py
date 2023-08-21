import cv2
myimage = cv2.imread('example.jpg')
blue,green,red=cv2.split(myimage)
cv2.imshow("Blue Channel", blue)
cv2.imshow("Green Channel", green)
cv2.imshow("Red Channel", red)
cv2.waitKey(0)
green[:,:] = 0
image = cv2.merge([blue, green, red])
cv2.imshow('Edited Image', image)
cv2.waitKey(0)