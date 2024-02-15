import cv2
import numpy as np
# we have two file in the directory named giraffe & safari .jpeg and we want to put giraph on top of the safari and change the backgroud.

forground = cv2.imread('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/09-image-processing/08-ChangeBackGround/011 giraffe.jpeg')
background = cv2.imread('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/09-image-processing/08-ChangeBackGround/011 safari.jpeg')

# the software has to remove those green background,
print(forground[40,40]) # this line will return the value (color) of one of the pixels in the picture

width = forground.shape[1] # this is the width of the picture
height = forground.shape[0] # this is the height of the giraff picture
resized_back = cv2.resize(background,(width,height))
# in the nested loop below we are iteration thro all the pixels of the picture
for i in range(width):
    for j in range(height):
        pixel = forground[j,i]
        # this command will check if any pixel is like the color that we give it to that:
        if np.any(pixel==[1,255,0]):
            # and in here we replace the pixel colors with the resized version of the background because these two pictures are not the same sized!
            forground[j,i] = resized_back[j,i]

cv2.imwrite('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/09-image-processing/08-ChangeBackGround/output.jpeg',forground)
