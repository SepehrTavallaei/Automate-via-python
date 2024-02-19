#  in this section we will learn How to record and save Audio files
# we will use two libraries that are third party which means that we have to pip insatll them the names are : sounddevice & scipy
# this give us access to the mice
import sounddevice
# this give us access to creat and save an audio file
from scipy.io.wavfile import write

# first we have to know jow many seconds the audio should be:
seconds = 1 
# this is common to put as sampling Hz  
fps =  44100
# here we start recording the file and as inputs we give it how many frames it should take to stop reccording, so secends times frame per sec is the desired number , and then we giev the fps and then the channels, the number we put dor the channels is either 1 or 2 depending in the system that we are coding with
my_recording = sounddevice.rec(frames=seconds*fps ,samplerate=fps,channels=1)
# once we start recording we use wait method that means the programm will wait untill the recording finishes and then it continue to it's process
sounddevice.wait()
# and then we write and save the audio using write function and we give as an input the file path
file_path = '/Users/sepehr/Desktop/notes/PracticalLearningOfPython/17-controlling-the computer/03-RecordingAudio/output1.mp3'
write(file_path, fps, my_recording)
# the recording is a numpy array :
print(type(my_recording))