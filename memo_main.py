from memo_card_layout import *
from memo_data import Question
from random import *

qst1 = Question("Дім", "house", "apple", "dog", "city")
qst2 = Question("Мишка", "mouse", "cat", "pineaple", "noice")
qst3 = Question("Кіт", "Cat", "horse", "dog", "goat")

list = [qst1, qst2, qst3]

def randomQuestion():
    global list
    question = choice(list)
    radio_list = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]
    shuffle(radio_list)
    answerRB = radio_list[0]
    wronge1= radio_list[1]
    wronge2= radio_list[2]
    wronge3= radio_list[3]
    lb_Question.setText(question.question)
    answerRB.setText(question.answer)
    wronge1.setText(question.wrong_answer1)
    wronge2.setText(question.wrong_answer2)
    wronge3.setText(question.wrong_answer3)


def clickOk():
    show_result()

randomQuestion()

btn_OK.clicked.connect(clickOk)
app.exec_()