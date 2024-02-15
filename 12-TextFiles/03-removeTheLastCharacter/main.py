# from pathlib import Path

# csv files are just another type of files that are non-binary (text files)

with open('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/12-TextFiles/03-removeTheLastCharacter/004 file3.csv','r') as file:
    content = file.read()

print(content)
with open('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/12-TextFiles/03-removeTheLastCharacter/004 file3_new.csv','w') as new_file:
    new_file.write(content[0:-1])



