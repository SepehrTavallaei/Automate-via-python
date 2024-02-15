# this is how we import the library:
import cv2
# print(dir(cv2))all the methods in the cv2
# now we want to see the colors inside the image, so we use cv2,imread('the file name',the flag in this case flag 1 means load the image in colors)
color = cv2.imread('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/09-image-processing/01-convert-toGrayscale/001 galaxy.jpeg',1)
print(color)
# the above reault is numpy array and its a 3 dimensional array.
color2 = cv2.imread('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/09-image-processing/01-convert-toGrayscale/001 galaxy.jpeg',0)
# and if we want to grayscale the image we do this:
cv2.imwrite('09-image-processing/01-convert-toGrayscale/001 galaxy.jpeg',color2)