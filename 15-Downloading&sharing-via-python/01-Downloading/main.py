# we will download from this web site:
# the very first thing you need to know is the url of the content that you want to download.
url = 'https://filesamples.com/samples/audio/mp3/Symphony%20No.6%20(1st%20movement).mp3'
# for this action we need to import rrequests Library
import requests

req = requests.get(url)
# print(req.content) what we will se is the bytes if this file
# what we should do is to open a file as write Binary mode:
with open('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/15-Downloading&sharing-via-python/01-Downloading/download.mp3','wb') as file:
    file.write(req.content) # and here we go! we have downloaded the file.