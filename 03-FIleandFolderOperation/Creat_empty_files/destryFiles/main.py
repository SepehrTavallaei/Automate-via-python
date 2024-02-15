from pathlib import Path
# first we set the root dir:
root_dir = Path('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/03-FIleandFolderOperation/Creat_empty_files/destryFiles/destination')

# then we loop through all the subfolders in the root dir which the format is csv:
for path in root_dir.glob('*.csv'):
    # we use with structure to open the file in the write binary mode so we can change them:
    with open(path,'wb') as file :
        # here we change the file:
        file.write(b'')
    # and then for each file we do the unlink command (it is like delete) to remove the files
    path.unlink()

# this way if we recap all the memory that we just deleted the main files (wothout the same inputs) are not available anymore
    
