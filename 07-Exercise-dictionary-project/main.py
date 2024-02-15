from pathlib import Path
import json
from PyQt6.QtWidgets import QApplication,QLineEdit,QPushButton,QLabel,QWidget,QVBoxLayout





def find_meaning():
    file = Path('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/07-Exercise-dictionary-project/002 data.json')
    data = json.load(open(file))
    if data[text.text()]:
        result = ''
        for item in data[text.text()]:
            result += item + '\n'
    else:
        result = 'there is no meaning for that word'

    text_box.setText(result)
    

def main():
    global text_box,text
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle('my dictionary')
    layout = QVBoxLayout()

    text = QLineEdit()
    layout.addWidget(text)

    translate_btn = QPushButton('search')
    layout.addWidget(translate_btn)
    translate_btn.clicked.connect(find_meaning)

    text_box = QLabel('')
    layout.addWidget(text_box)

    window.setLayout(layout)
    window.show()
    app.exec()


main()