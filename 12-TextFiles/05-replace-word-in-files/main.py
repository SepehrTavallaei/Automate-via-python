from pathlib import Path


files_dir = Path('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/12-TextFiles/05-replace-word-in-files/files')

for filePath in files_dir.iterdir():
    with open(filePath,'r') as file:
        content = file.read()
        new_content = content.replace('amount','units')
    
    with open(filePath,'w') as new_file:
        new_file.write(new_content)
