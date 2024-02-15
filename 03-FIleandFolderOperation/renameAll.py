from pathlib import Path


# December = Path('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/03-FIleandFolderOperation/Files2/December')
# November = Path('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/03-FIleandFolderOperation/Files2/November')


# my way of solving this problem: 

# def change_name_based_on_FolderName(dir,file_paths):
#     for path in file_paths:
#         new_name = dir.name + "-" + path.stem + path.suffix
#         new_path = path.with_name(new_name)
#         path.rename(new_path)

# change_name_based_on_FolderName(December,list(December.iterdir()))
# change_name_based_on_FolderName(November,list(November.iterdir()))

# the tutor's way of solving it:


root_dir = Path('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/03-FIleandFolderOperation/Files2')
file_paths = (root_dir.glob("**/*")) # using this .glob("**/*") will give us access to all the sub directiries in that dir

for path in file_paths:
    if path.is_file():
        parent_folder = path.parts[-2]
        new_file_name = parent_folder + '-' + path.stem + path.suffix
        new_path_file = path.with_name(new_file_name)
        path.rename(new_path_file)

