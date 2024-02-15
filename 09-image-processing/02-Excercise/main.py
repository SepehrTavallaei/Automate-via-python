import cv2
from pathlib import Path
root_dir = Path('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/09-image-processing/02-Excercise/images')
root_file = '/Users/sepehr/Desktop/notes/PracticalLearningOfPython/09-image-processing/02-Excercise/images'
result_file = '/Users/sepehr/Desktop/notes/PracticalLearningOfPython/09-image-processing/02-Excercise/GrayImages'
for file in root_dir.iterdir():
    color = cv2.imread(root_file + '/' + file.name,0)
    # print(type(file))
    cv2.imwrite(result_file + '/' + file.name,color)