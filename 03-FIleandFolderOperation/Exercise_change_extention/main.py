from pathlib import Path

root_dir = Path("/Users/sepehr/Desktop/notes/PracticalLearningOfPython/03-FIleandFolderOperation/Exercise_change_extention/Files")
file_paths = root_dir.glob("**/*")
def change_suffix():
    for path in file_paths:
        if path.is_file():
            new_file_name = path.stem + '.csv'
            new_file_path = path.with_name(new_file_name)
            path.rename(new_file_path)

change_suffix()