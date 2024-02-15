import numpy
import cv2

# first we load the vide
video = cv2.VideoCapture('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/10-bluring-video-exercise/videos/002 smile.mp4')

# here are two variables to check if the video is loaded or not, and to get the first frame of the video
success,frame = video.read()

height = frame.shape[0]
width = frame.shape[1]

face_cascade = cv2.CascadeClassifier('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/10-bluring-video-exercise/002 faces.xml')

output = cv2.VideoWriter('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/10-bluring-video-exercise/videos/blurred_face.mp4',cv2.VideoWriter_fourcc(*'DIVX'),30,(width,height))

# a video is created by a lot of frames, so what we are going to do is to proccess each frame with this wile loop
while success:
    # for each frame we detect the face inside it
    faces = face_cascade.detectMultiScale(frame,1.1,4)
    # and we get the coordinates of the rectangle that covers the face in the frame
    for (x,y,w,h) in faces:
        # here we change the portioon of the picture by blure method
        frame[y:y+h,x:x+w] = cv2.blur(frame[y:y+h,x:x+w],(50,50))
    # now we write the frame inside the output
    output.write(frame)
    # each time that loop runs we change the frame.
    success,frame = video.read()

# this command will save the video for us!
output.release()