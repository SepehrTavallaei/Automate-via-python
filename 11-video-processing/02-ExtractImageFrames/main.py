import cv2


# we want to extract all the frames in a Video
image_dir = './directory/images'
video = cv2.VideoCapture('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/11-video-processing/02-ExtractImageFrames/directory/002 video.mp4')
# now if we print video we see nothing:
print(video) # the output is:  < cv2.VideoCapture 0x104591830>

# but there is a special method that we can use to see some more valuable info:
# print(video.read()) # read will execute the first frame (actually it is the next frame)

# now if we are going to loop thro the video we do this:

success , frame = video.read()
counter = 1
while success:
    cv2.imwrite(f'/Users/sepehr/Desktop/notes/PracticalLearningOfPython/11-video-processing/02-ExtractImageFrames/directory/images/{counter}.jpeg',frame)
    success , frame = video.read()
    counter +=1


