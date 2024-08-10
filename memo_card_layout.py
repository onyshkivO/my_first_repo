''' Вікно для картки питання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

card_width, card_height = 600, 500
app = QApplication([])


# віджети, які треба буде розмістити:
btn_Menu = QPushButton('Меню') # кнопка повернення до основного вікна
btn_Sleep = QPushButton('Відпочити') # кнопка прибирає вікно та повертає його після закінчення таймера
box_Minutes = QSpinBox() # введення кількості хвилин
box_Minutes.setValue(30)
btn_OK = QPushButton('Відповісти') # кнопка відповіді
lb_Question = QLabel('') # текст питання
# Панель з варіантами:
RadioGroupBox = QGroupBox("Варіанти відповідей") # група на екрані для перемикачів із відповідями
RadioGroup = QButtonGroup() # а це для угруповання перемикачів, щоб керувати їхньою поведінкою



rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')


RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


# Розміщуємо варіанти відповідей у два стовпці всередині групи:
layout_ans1 = QHBoxLayout()  
layout_ans2 = QVBoxLayout() # вертикальні будуть усередині горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # дві відповіді у перший стовпець
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # дві відповіді у другий стовпець
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # розмістили стовпці в одному рядку

RadioGroupBox.setLayout(layout_ans1) # готова "панель" з варіантами відповідей 


# розміщуємо всі віджети у вікні, вони розташовані в чотири рядки:
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()


layout_line1.addWidget(btn_Menu)
layout_line1.addStretch(1) # розрив між кнопками робимо по можливості довшим
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(box_Minutes)
layout_line1.addWidget(QLabel('хвилин')) # нам не потрібна змінна для цього напису

AnswerGroup = QGroupBox("Відповідь") 

lb_isCorrect = QLabel('123')
lb_answerText = QLabel('321')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_isCorrect)
layout_res.addWidget(lb_answerText)
AnswerGroup.setLayout(layout_res)

layout_line2.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnswerGroup)
AnswerGroup.hide()


layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK, stretch=2) # кнопка має бути великою
layout_line4.addStretch(1)


# Тепер створені 4 рядки розмістимо один під одним:
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addLayout(layout_line3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # прогалини між вмістом


# # Результат роботи цього модуля: віджети розміщені всередині layout_card, який можна призначити вікну.

def show_questions():
    AnswerGroup.hide()
    RadioGroupBox.show()

def show_result():
    AnswerGroup.show()
    RadioGroupBox.hide()




win_card = QWidget()
win_card.resize(card_width, card_height)
win_card.move(300, 300)
win_card.setWindowTitle('Memory Card')


win_card.setLayout(layout_card)
win_card.show()