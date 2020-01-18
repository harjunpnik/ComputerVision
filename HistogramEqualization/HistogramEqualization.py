import numpy as np
import cv2 as cv 
from matplotlib import pyplot as plt

#img = cv.imread('foggy.jpg', 0)
#img = cv.imread('highContrast.jpg', 0)
#img = cv.imread('poorContrast1.jpg', 0)
#img = cv.imread('thumbnail_Fridge in a tree at Warmun_Bright.jpg', 0)
#img = cv.imread('thumbnail_Fridge in a tree at Warmun_Dark.jpg', 0)
#img = cv.imread('thumbnail_Helsinki_Over-Exposed.jpg', 0)
#img = cv.imread('thumbnail_Helsinki_Under-Exposed.jpg', 0)
#img = cv.imread('thumbnail_Russian Cathedral_Over_Exposed.jpg', 0)
#img = cv.imread('thumbnail_Russian Cathedral_Under_Exposed.jpg', 0)

equ = cv.equalizeHist(img)
res = np.hstack((img,equ))


cv.imshow('image window' ,img)
cv.imshow('image window' ,res)


plt.hist(equ.flatten(),256,[0,256], color = 'r')
plt.show()

cv.waitKey(0)


