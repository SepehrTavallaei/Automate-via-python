import cv2


# this is the current shape size of the image:
# print(image.shape)

def calculate_size(scale_percentage,width,height):
    new_width = int(width * scale_percentage/100)
    new_height = int(height * scale_percentage / 100)
    print('new Dim: ',new_height,new_width)
    return (new_width,new_height)

def resize(image_path,scale_percentage,resized_path):
    image = cv2.imread(image_path)
    new_dim = calculate_size(scale_percentage,image.shape[1],image.shape[0])
    # cv2.resize(...) gives us a resized version of Images so inorder to save them we have to go one more step
    resized_image = cv2.resize(image,new_dim)
    # and here we go, we write images.
    cv2.imwrite(resized_path,resized_image)


image_path = '/Users/sepehr/Desktop/notes/PracticalLearningOfPython/09-image-processing/03-resize-images/005 galaxy.jpeg'
result_path = '/Users/sepehr/Desktop/notes/PracticalLearningOfPython/09-image-processing/03-resize-images/new_image.jpeg'
resize(image_path,120,result_path)