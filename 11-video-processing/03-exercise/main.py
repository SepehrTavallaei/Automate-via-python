import cv2

video = cv2.VideoCapture('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/11-video-processing/03-exercise/003 video.mp4')

# my way of solving this problem:
# success , frame = video.read()
# counter = 1
# while success and counter < 57:
#     success , frame = video.read()
#     counter+=1

# cv2.imwrite('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/11-video-processing/03-exercise/output.jpeg',frame)

# the better way:

nr_frame = video.get(cv2.CAP_PROP_FRAME_COUNT) # total number of rames
fps = video.get(cv2.CAP_PROP_FPS) # how many frames per second do we have

time_stamp = '00:00:02.75'.split(':')

time = [float(i) for i in time_stamp]

hours , minutes , seconds = time # now we go even ferther and put each tume in a specific variable

frame_number = hours * 3600 * fps + minutes *60 * fps + seconds * fps

success , frame = video.read()

while success and frame_number>0:
    frame_number-=1
    success , frame = video.read()

cv2.imwrite('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/11-video-processing/03-exercise/output.jpeg',frame)

# or we can do this:
