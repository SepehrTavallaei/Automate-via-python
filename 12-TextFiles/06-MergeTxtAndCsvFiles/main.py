from pathlib import Path

files_dir = Path('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/12-TextFiles/06-MergeTxtAndCsvFiles/files')

content = ''
for filePath in files_dir.iterdir():
    with open(filePath,'r') as file:
        content = content + file.read()
        print(content)
    content += '\n\n'
    

with open('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/12-TextFiles/06-MergeTxtAndCsvFiles/files/result.csv','w') as file:
    file.write(content)
    
