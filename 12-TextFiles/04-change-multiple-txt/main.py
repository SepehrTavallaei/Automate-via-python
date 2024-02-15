from pathlib import Path

files_dir = Path('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/12-TextFiles/04-change-multiple-txt/files')

for file_path in files_dir.iterdir():
    with open(file_path,'r') as file:
        content =  file.read()
    
    with open(file_path,'w') as file2:
        file2.write(content[0:-1])
