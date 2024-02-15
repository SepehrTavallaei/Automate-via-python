from pathlib import Path

root_dir = Path('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/03-FIleandFolderOperation/Creat_empty_files/files')

for i in range(10,21):
    file_name = str(i) + '.txt'
    file_path = root_dir / Path(file_name)
    file_path.touch()
    