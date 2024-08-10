from memo_card_layout import *
from memo_data import *
from PyQt5.QtWidgets import QWidget, QApplication
from random import * 

questions=[]
frm = Question('Яблоко', 'apple', 'application', 'pinapple', 'apply')
questions.append(frm)
frm = Question('Дом', 'house', 'horse', 'hurry', 'hour')
questions.append(frm)
frm = Question('Мышь', 'mouse', 'mouth', 'muse', 'museum')
questions.append(frm)
frm = Question('Число', 'number', 'digit', 'amount', 'summary')
questions.append(frm)


def random_Answer():
    global list1
    question = choice(questions)
    radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
    shuffle(radio_list)
    answer = radio_list[0]
    wrong_answer1, wrong_answer2, wrong_answer3 = radio_list[1], radio_list[2], radio_list[3]
    lb_Question.setText(question.question)
    answer.setText(question.answer)
    wrong_answer1.setText(question.wrong_answer1)
    wrong_answer2.setText(question.wrong_answer2)
    wrong_answer3.setText(question.wrong_answer3)
    print("random_Answer"+answer.text())
    list1 = [answer, wrong_answer1, wrong_answer2, wrong_answer3] 

def check_result():
   global list1
   answer, wrong_answer1, wrong_answer2, wrong_answer3=list1[0],list1[1],list1[2],list1[3]
   correct = answer.isChecked()
   print(answer.text())
   if correct:
       lb_Result.setText(text_correct) 
       lb_Correct.setText(answer.text()) 
       show_result()
   else:
       incorrect = wrong_answer1.isChecked() or wrong_answer2.isChecked() or wrong_answer3.isChecked()
       if incorrect:
           lb_Result.setText(text_wrong) 
           lb_Correct.setText(answer.text()) 
           show_result()

def click_OK():
    global list1
    if btn_OK.text() != 'Наступне питання':
        check_result()
    else:
        random_Answer()
        show_question()

list1= []
random_Answer()
show_question()
btn_OK.clicked.connect(click_OK)



app.exec_()
