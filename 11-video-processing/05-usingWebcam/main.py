import cv2

# int he path we put the file path for the VideoCapture, but if we put an integer, for example we put 0 we acces the first camera of out laptop, 1 is for the second
video = cv2.VideoCapture(0)

success, frame = video.read()

height = frame.shape[0]
width  = frame.shape[1]

face_cascaed = cv2.CascadeClassifier('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/11-video-processing/05-usingWebcam/006 faces.xml')
output = cv2.VideoWriter('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/11-video-processing/05-usingWebcam/output.avi',
cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))

count = 0

while success:
    faces = face_cascaed.detectMultiScale(frame,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),4)
    output.write(frame)
    success,frame = video.read()
    count +=1
    print(count)