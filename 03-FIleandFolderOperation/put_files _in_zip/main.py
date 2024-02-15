from pathlib import Path
import zipfile

# jus as always we create a temo dir as roor_dir
root_dir = Path("/Users/sepehr/Desktop/notes/PracticalLearningOfPython/03-FIleandFolderOperation/put_files _in_zip/files")
# then by using / sytntax we creat where we want to store our archive files
archive_path = root_dir / Path('archive.zip')

with zipfile.ZipFile(archive_path,'w') as zf:
    for path in root_dir.glob('*.txt'):
        zf.write(path)
        path.unlink() # unlinks from the root_dir and paste folder a file before that



