import cv2
import os
import numpy

column = 3
rows = 2

# these are the border that divide each image
horizonttal_margin = 40
vertical_margin = 20

# this list gave us the list of all the images
images = os.listdir('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/09-image-processing/09-Creat-image-Collage/images')
# print(images)
image_object = [cv2.imread(f'/Users/sepehr/Desktop/notes/PracticalLearningOfPython/09-image-processing/09-Creat-image-Collage/images/{filename}') for filename in images] 

# now we need the size of images , since all the images in this example is in 1 size knowing the size of one of them will be enouph 
shape = cv2.imread('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/09-image-processing/09-Creat-image-Collage/images/012 1.jpeg').shape
# print(shape)

# so, now we need to creat an empty Image, note that each image is created from Arrays that members of it represent the pixel colors.

# numpy zeros is a method to creat multi dimensional Array, now we need to calculate the size of images, the first argument is the shape of the blank image, the second is the dType which in this case we enter unit8
big_image = numpy.zeros((shape[0]*rows+shape[0]*(rows+1),shape[1]*column+shape[1]*(column+1),shape[2]),numpy.uint8)
# if you want to see your image in white color (currently it is Black) you run this command:
big_image.fill(255) #this is a numpy method which fill all the numbers in the Array to 255 (we know that if the three values for RGB is 255 the color is white)
# and then we creat the image file
cv2.imwrite('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/09-image-processing/09-Creat-image-Collage/blank.jpeg',big_image)
# now we have to add our images!
# now we need a list of coordinators that give us the coordinate of where we have to put our images.

positions = [(x,y) for x in range(column) for y in range(rows)]
print(positions)

for pos_x , pos_y in zip(positions,images):
    # for now i dont know where I messed up :(
    x = pos_x * (shape[1] + vertical_margin) + vertical_margin
    y = pos_y * (shape[0] + horizonttal_margin) + horizonttal_margin
    big_image[y:y+shape[0], x:x+shape [1]] = images # accessing the portion of the image and 4 margin around it.
