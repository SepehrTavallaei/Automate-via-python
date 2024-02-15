from pathlib import Path

root_dir = Path("/Users/sepehr/Desktop/notes/PracticalLearningOfPython/03-FIleandFolderOperation/HardExercise/files")
file_paths = root_dir.glob("**/*")


def change_name():
    for path in file_paths:
        if path.is_file():
            custom_set = path.parts
            new_file_name = ''
            for i in range(len(custom_set)-1,1,-1):
                new_file_name += custom_set[i] + '-'
            
            new_file_path = path.with_name(new_file_name)
            path.rename(new_file_path)

            
change_name()