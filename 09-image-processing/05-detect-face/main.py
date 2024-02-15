import cv2

# the first thing we need to do is to load the image
image = cv2.imread('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/09-image-processing/05-detect-face/007 humans.jpeg')

# after that we need to load the xml file, to do that we write this command: Cascadeclassifier gets as input the path to xml file
face_cascade = cv2.CascadeClassifier('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/09-image-processing/05-detect-face/007 faces.xml')
# what we do now is that we detect faces using detectMultiScale method which means that we want to detect faces in diffrent scalse
# as the input we give the image file and also it is good to put these as well: 
# after the image is scale factor usually its good to put 1.05 or 1.1
# the next factor is minimum neighbors ... basically we are saying to how much to check diffrent scales in order to find faces ... if python is checking a certain pixel we say to it to also check 4 pixels aroud of that as well.


faces = face_cascade.detectMultiScale(image,1.1,4)
# this is a 2 dimensional numpy array and its coordinates of the rectangles that covers the faces:
print(faces)
# what we shoud do now is to iterate thro the numpy array:

for (x,y,w,h) in faces:
    # rectangle method expect two coordinate of two non neighbor vertices of a rectangle and then it draw a rextagle for us
    # the next parameter is for color if we want to name a color we have to give it in format of RGB like (255,255,255) stands for color white
    # an then we say the size of the rectangle (width)
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,255),4)
    # remember that we dont need to save the rectangled object faces and only save that we only need to run the rectangle method and thats it!
    cv2.imwrite('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/09-image-processing/05-detect-face/humanFaces.jpeg',image)
