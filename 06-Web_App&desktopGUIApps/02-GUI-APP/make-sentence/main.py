from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit

def make_sentence():
    input_text = text.text()
    output_lable.setText(input_text.capitalize()+ '.')
# instansiate the app
app = QApplication([])
window = QWidget()
# setting title for the app
window.setWindowTitle('Sentence Maker')
# all the text boxes,buttins and etc are called widgets we add those widgets like this: 
# the V in the QV stands for vertical if we dont put the uppercase v and put uppercase h instead widgets will stand horizortally
layout = QVBoxLayout()
# this is how we make a text box in our app:
text = QLineEdit()
# now we add this to the layout
layout.addWidget(text)
# now I add an other input text box to the app:
# text = QLineEdit()
# layout.addWidget(text)

# this is how we make buttons for the app:
btn = QPushButton('Make')
layout.addWidget(btn)
# after that we need to take an action for the button
btn.clicked.connect(make_sentence)
# Widogets,signals,slots the order of how PyQt works
# this is how we make a text box so that we can import text to it
output_lable = QLabel('')
layout.addWidget(output_lable)
# but it's not done yet, we need to add the layout to the window object:
window.setLayout(layout)

# at the end this is how we run the programm:
window.show()
app.exec()