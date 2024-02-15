from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel,QPushButton,QLineEdit

def btn_clicked():
    print('btn clicked')
    text_box.setText(text.text())
    

app = QApplication([])
window = QWidget()
window.setWindowTitle('test my undrestanding')
layout = QVBoxLayout()
text = QLineEdit()
layout.addWidget(text)
btn = QPushButton('test')
layout.addWidget(btn)
btn.clicked.connect(btn_clicked)
text_box = QLabel('')
layout.addWidget(text_box)


window.setLayout(layout)
window.show()
app.exec()
