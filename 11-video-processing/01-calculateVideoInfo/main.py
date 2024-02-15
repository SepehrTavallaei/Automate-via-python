import cv2

video = cv2.VideoCapture('./video/002 video.mp4')

width = video.get(cv2.CAP_PROP_FRAME_WIDTH) # this will give us the width of the video
height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)# this will give us the height of the video

number_frames = video.get(cv2.CAP_PROP_FRAME_COUNT) # number of frames
fps = video.get(cv2.CAP_PROP_FPS) # the number of frames per second


