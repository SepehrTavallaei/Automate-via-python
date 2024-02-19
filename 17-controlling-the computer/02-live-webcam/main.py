#  the Librarues that we wanto use are 2 first the opencv to get the webcam video & flask to build our web App

import cv2
from flask import Flask,render_template,Response
# we use videoCapture class and in here we can either put 0 or 1 or the number of webcam we have or we can provide the file name that our video is stored so we can process it.
video = cv2.VideoCapture(0)
# in here we should creat a function it is responsible for returning frames :
def get_frame():
    while True:
        success , frame = video.read()
        #  here we should encode the frame to jpg the result will be two variables the first is a boolean type it means of we get the grame or not, and the second one is reaponsible for jpg image
        sc , encoded_image = cv2.imencode('.jpg',frame)
        frame = encoded_image.tobytes() # then we want to convert this encoded image into the previous variable but we will use .tobyte() method to convert ot to bytes
        # and finally we will use Yield key word to return the bite object
        yield(b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\b') # basically we want to return the image and images are constructed in bytes and now we will start the flask part.

# here we define the app
app = Flask(__name__)
# this function is responsible for the hime page
@app.route('/')
def index ():
    dir = '/Users/sepehr/Desktop/notes/PracticalLearningOfPython/17-controlling-the computer/02-live-webcam/index.html'
    return render_template('index.html')
# and then in here we want to creat a finction that provides the video for the html page
@app.route('/vide_feed_url')
def video_feed():
    # this function will return a Response object and we have to give it as input a Generator 
    return Response(get_frame(),mimetype='multipart/x-mixed-replace; boundary=frame')

# and thats is! now we have to run the flask app:
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)
     