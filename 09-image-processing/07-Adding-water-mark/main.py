import cv2

image = cv2.imread('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/09-image-processing/07-Adding-water-mark/010 elfs.jpeg')
waterMark = cv2.imread('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/09-image-processing/07-Adding-water-mark/010 watermark.png')

# this way we locate the coordinator of x & y to the place which is one of the coordinators of a method that we are going to use in the future.
x = image.shape[1]-waterMark.shape[1]
y = image.shape[0]-waterMark.shape[0]


waterMark_place = image[y:,x:]
cv2.imwrite('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/09-image-processing/07-Adding-water-mark/010 watermark_place.jpeg',waterMark_place)
# now if we print the shape of water_matk_place variable we will see the same size as the watermark has
print(waterMark_place.shape)
# and now is the time when we replce this two pictures 
# the first input is the watermark place and the weight is the opacity of it and then the third input is the water markmthe last input is called Gama and whate we put as the input will be replaced to all files
blend = cv2.addWeighted(waterMark_place,0.5,waterMark,0.5,0)
cv2.imwrite('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/09-image-processing/07-Adding-water-mark/blendMixture.jpeg',blend)
# now it is time to replace these two images
image[y:,x:] = blend
cv2.imwrite('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/09-image-processing/07-Adding-water-mark/elfs-watermarked.jpeg',image)