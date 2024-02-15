# in order to access the time which the file has been created we have to do this:
from pathlib import Path
from datetime import datetime

root_dir = Path('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/03-FIleandFolderOperation/Exercise_date_created/Files')



def change_name(file_path):
    stats = file_path.stat()
    second_created = stats.st_ctime
    date_created = datetime.fromtimestamp(second_created)
    date_created_str = date_created.strftime("%Y-%m-%d.%H:%M:%S")
    return date_created_str

def main():
   file_paths = root_dir.glob("**/*")
   for file in list(file_paths):
       if file.is_file():
           new_name = change_name(file) + '-' + file.stem + file.suffix
           print(new_name)
           new_file_path = file.with_name(new_name)
           file.rename(new_file_path)



main()