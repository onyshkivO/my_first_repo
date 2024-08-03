from PyQt5 import *
from PyQt5.QtWidgets import *

app = QApplication([])
win_card = QWidget()
win_card.resize(600, 600)
win_card.move(300, 300)
win_card.setWindowTitle('Memory Card')
btn_menu = QPushButton('Меню')
btn_rest = QPushButton('Відпочити')
btn_next = QPushButton('Відповісти')
sp_rest = QSpinBox()
question = QLabel('питання')
minutes = QLabel('хвилин')
RadioGroupBox = QGroupBox("Варіанти відповідей")

RadioGroup = QButtonGroup()

rbtn_ans1 = QRadioButton('1')
rbtn_ans2 = QRadioButton('2')
rbtn_ans3 = QRadioButton('3')
rbtn_ans4 = QRadioButton('4')
RadioGroup.addButton(rbtn_ans1)
RadioGroup.addButton(rbtn_ans2)
RadioGroup.addButton(rbtn_ans3)
RadioGroup.addButton(rbtn_ans4) 

layout_ans = QHBoxLayout()
layout_ans1 = QVBoxLayout()
layout_ans2 = QVBoxLayout()

layout_ans1.addWidget(rbtn_ans1)
layout_ans1.addWidget(rbtn_ans2)
layout_ans2.addWidget(rbtn_ans3)
layout_ans2.addWidget(rbtn_ans4)

layout_ans.addLayout(layout_ans1)
layout_ans.addLayout(layout_ans2)

RadioGroupBox.setLayout(layout_ans)


line_1 = QHBoxLayout()
line_1.addWidget(btn_menu)
line_1.addStretch(1)
line_1.addWidget(btn_rest)
line_1.addWidget(sp_rest)
line_1.addWidget(minutes)

line_2 = QHBoxLayout()
line_2.addWidget(question)

line_4 = QHBoxLayout()
line_4.addWidget(btn_next)

main = QVBoxLayout()
main.addLayout(line_1)
main.addLayout(line_2)
main.addWidget(RadioGroupBox)   
main.addLayout(line_4)
win_card.setLayout(main)
win_card.show()
app.exec_()
