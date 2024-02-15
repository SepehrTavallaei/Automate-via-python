# both os and pathlib are used to access data.
from pathlib import Path

p1 = Path("/Users/sepehr/Desktop/notes/PracticalLearningOfPython/03-FIleandFolderOperation/Files/abc.txt")
 # it gets us the file object not the string of where its located
# print(p1.exists())  for example this returns True as the file is located on the location.
#  you may ask why just don't we use the actuall sting of the location why we complicate things?well in this example the benfits are not visible
# but in the long run eventually you will notice the diffrence.
if p1.exists(): 
    with open(p1,'r') as file:
        print(file.read())

#  but, what if we creat a file path that is not exist?
        # like this:
p2 = Path("/Users/sepehr/Desktop/notes/PracticalLearningOfPython/03-FIleandFolderOperation/Files/ghi.txt") 

if not p2.exists():
    with open(p2,'w') as file:
        file.write('Content 3')
# we can use these methods as well to improve our performance with files:
print(p2.name)
print(p2.suffix)
print(p2.stem)
# or we can also point pathlib to a foldre and then we can iterate through the subdirectories that are located inside that folder:
p3 = Path('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/03-FIleandFolderOperation/Files')
for item in p3.iterdir():
    print(item.name)