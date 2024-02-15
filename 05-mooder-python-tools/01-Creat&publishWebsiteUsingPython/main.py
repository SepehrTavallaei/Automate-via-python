# using our local python text editor we can only create a web in the local host but, if we use reple ide we can see our web site online, unfortunatly because of the bad access to the network I can not get my web site online to the internet

# to creat a web site you need a web framework, Flask & Jdango are two popular web frameworks out there
# Flask is easier to make web sites so we use flask.

from flask import Flask
# then we creat an object instance using the Flask Class
app = Flask(__name__) # we give it the name of the file we are running now.
# then here we define the url when the visitor visits this page
# this is the homepage:
@app.route('/')
def home():
    return "welcome to my website"
# so for every url of our website we add one decorator,
@app.route('/book')
def book():
    return "I currently read 25 books but I'm trying to learn more"
# the at the end we call run method.
app.run()