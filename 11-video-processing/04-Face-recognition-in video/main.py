import cv2

video = cv2.VideoCapture('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/11-video-processing/04-Face-recognition-in video/directory/006 video.mp4')
success,frame = video.read()
face_cascade = cv2.CascadeClassifier('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/11-video-processing/04-Face-recognition-in video/directory/006 faces.xml')
width = frame.shape[1]
height = frame.shape[0]

output = cv2.VideoWriter('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/11-video-processing/04-Face-recognition-in video/directory/output.avi',cv2.VideoWriter_fourcc(*'DIVX'),30,(width,height))
# output = cv2. VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'DIVX'),

while success:
    
    faces = face_cascade.detectMultiScale(frame,1.1,4)
    for (x,y,w,h) in faces:
        # now that we have the rectangle and all the frames we have to put them in a video for that before this loop we need to creat an empty video
        cv2.rectangle(frame,(x,y),(w+x,y+h),(255,255,255),4)

    output.write(frame)
    success,frame = video.read()

output.release()
