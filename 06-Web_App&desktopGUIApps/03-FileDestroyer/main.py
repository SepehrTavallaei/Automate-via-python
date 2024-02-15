from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel
from PyQt6.QtWidgets import QPushButton,QFileDialog
from PyQt6.QtCore import Qt
from pathlib import Path
def open_files():
    global file_names
    # we write 2 variables because this function returns two objects the first one is the list of all the file names that we select and the second is some extra info that we don't need
    file_names, _ = QFileDialog.getOpenFileNames(window,'Select files')
    
    message.setText('\n'.join(file_names))

def destroy_files():
    for file_name in file_names:
        # if you don't know how to deal with this module we covered it in the File Operation section
        path = Path(file_name)
        with open(path,'wb') as file:
            file.write(b'')
        path.unlink()
    message.setText('')



app = QApplication([])
window = QWidget()
window.setWindowTitle('File Destroyer')
layout = QVBoxLayout()

description = QLabel('Select the files you want to destroy. The files will be <font color="red">permanantly</font> deleted')
layout.addWidget(description)

open_btn = QPushButton('open files')
# a small window will show up when we hover the mouse on the button and the context of it is what we give the methode as the paarameter
open_btn.setToolTip('open files')
# here is how we give size to a button:
open_btn.setFixedWidth(100)
# the second Argument here is for you to center open button
layout.addWidget(open_btn,alignment=Qt.AlignmentFlag.AlignCenter)
open_btn.clicked.connect(open_files)



destroy_btn = QPushButton('Destroy files')
destroy_btn.setFixedWidth(100)
layout.addWidget(destroy_btn,alignment=Qt.AlignmentFlag.AlignCenter)
destroy_btn.clicked.connect(destroy_files)

message = QLabel('')
layout.addWidget(message)


window.setLayout(layout)
window.show()
app.exec()