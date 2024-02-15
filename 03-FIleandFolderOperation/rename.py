from pathlib import Path

files = Path('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/03-FIleandFolderOperation/Files')
file_paths = list(files.iterdir())

for path in file_paths:
    new_file_name = "new-" + path.stem + path.suffix
    new_file_path = path.with_name(new_file_name)
    path.rename(new_file_path)
