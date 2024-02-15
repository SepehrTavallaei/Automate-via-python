from bs4 import BeautifulSoup
import requests
from PyQt6.QtWidgets import QApplication,QVBoxLayout,QWidget,QLabel,QPushButton,QLineEdit,QComboBox,QHBoxLayout

def currecncy_converter(in_currency,out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    req = requests.get(url).text
    soup = BeautifulSoup(req,"html.parser")
    rate = soup.find('span',class_='ccOutputRslt').get_text().split(' ')[0]
    return rate

    
    

def btn_clicked():
    in_cur = in_commbo.currentText()
    T_cur = target_commbo.currentText()
    value = float(text.text())* float(currecncy_converter(in_cur,T_cur))
    result = f'{str(float(text.text()))} is {value} {T_cur}'
    text_box.setText(result)

app = QApplication([])
window = QWidget()
window.setWindowTitle('currency converter')

layout = QVBoxLayout()
layout1 = QHBoxLayout()
layout.addLayout(layout1)
text_box = QLabel('')
layout.addWidget(text_box)

layout2 = QVBoxLayout()
layout1.addLayout(layout2) 
layout3 = QVBoxLayout()
layout1.addLayout(layout3)

in_commbo = QComboBox()
currencies = ['USD',"EUR","INR"]
in_commbo.addItems(currencies)
layout2.addWidget(in_commbo)

target_commbo = QComboBox()
target_commbo.addItems(currencies)
layout2.addWidget(target_commbo)

text = QLineEdit()
button = QPushButton('convert usd to EUR')

layout3.addWidget(text)
layout3.addWidget(button)
button.clicked.connect(btn_clicked)



window.setLayout(layout)
window.show()
app.exec()