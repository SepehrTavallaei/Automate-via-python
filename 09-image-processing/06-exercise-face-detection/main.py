import cv2
from pathlib import Path
def face_detection(file_name):
    image = cv2.imread(file_name)
    face_cascade = cv2.CascadeClassifier('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/09-image-processing/06-exercise-face-detection/007 faces.xml')
    faces = face_cascade.detectMultiScale(image,1.1,4)
    return len(faces)

def main():
    root_dir = '/Users/sepehr/Desktop/notes/PracticalLearningOfPython/09-image-processing/06-exercise-face-detection/images'
    result_dir = '/Users/sepehr/Desktop/notes/PracticalLearningOfPython/09-image-processing/06-exercise-face-detection/face-images'
    image_file = Path(root_dir).glob('**/*.jpeg')

    for image in image_file:
        if face_detection(root_dir+'/'+image.name) >= 1:
            face_img = cv2.imread(root_dir+'/'+image.name)
            cv2.imwrite(result_dir+'/'+image.name,face_img)

main()