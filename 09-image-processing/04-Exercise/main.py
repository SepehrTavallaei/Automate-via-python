import cv2
from pathlib import Path

root_dir = Path('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/09-image-processing/04-Exercise/images').glob('**/*.jpeg')

def size(scale_percentage,width,height):
    new_width = int(scale_percentage*width/100)
    new_height = int(scale_percentage*height/100)
    print('new Dim: ',width,height)
    return (new_width,new_height)

def resize(scale_percentage,file_name):
    result_path = '/Users/sepehr/Desktop/notes/PracticalLearningOfPython/09-image-processing/04-Exercise/resized_images'
    image = cv2.imread(file_name)
    resized_image = cv2.resize(image,size(scale_percentage,image.shape[1],image.shape[0]))
    cv2.imwrite(result_path+'/'+file_name.split('/')[len(file_name.split('/'))-1],resized_image)

def main():
    scale = int(input('in what scale you want your Images to be resized?'))
    for file in root_dir:
        resize(scale,'/Users/sepehr/Desktop/notes/PracticalLearningOfPython/09-image-processing/04-Exercise/images/'+file.name)

main()