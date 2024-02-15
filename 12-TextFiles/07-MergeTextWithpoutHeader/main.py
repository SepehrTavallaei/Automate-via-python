from pathlib import Path

files_dir = Path('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/12-TextFiles/07-MergeTextWithpoutHeader/files')

content = 'id,amount,price\n'
for filePath in files_dir.iterdir():
    with open(filePath,'r') as file:
        raw_content = file.read()
        content = content + raw_content[15:]
        print(content)
    

with open('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/12-TextFiles/07-MergeTextWithpoutHeader/files/result.csv','w') as file:
    file.write(content)
    
