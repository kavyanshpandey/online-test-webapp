from pywebio.input import *
from pywebio.output import *
from flask import Flask
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH


#  enter your questions here 
questions = [
        {
            "question":"Base language of web?",
            "options":['javaScript','ASP','PHP','HTML'],
            "answer":"HTML"
        },
        {
            "question":"Which is not a programming language",
            "options":['Python','HTML','Scala','Java'],
            "answer":"HTML"
        },
        {
            "question":"Secondery memory is also called _____",
            "options":['Virtual memory','RAM','ROM','Hard drives'],
            "answer":"ROM"
        },
        {
            "question":"functions that is used to get the length of string in Python",
            "options":['count()','length()','dis()','len()'],
            "answer":"len()"
        },
        {
            "question":"Which is not a web framework",
            "options":['Django','React','Numpy','Angular'],
            "answer":"Numpy"
        },
        
    ]

app = Flask(__name__)


def get_min_marks(questions_length):
    return questions_length//2

def exam():
    
    marks = 0
    min_marks = get_min_marks(len(questions))


    name = input("Please enter your name to start the test", type ="text")

    question_no = 0
    for question in questions:
        q = radio(f"{question['question']}",question["options"])
        if q == question["answer"]:
            marks+=1


    if marks>min_marks:
        style(put_text("Congratulations, " + name + ", your score is "+ str(marks)),'color:green')
        style(put_text("Result : PASSED"),'color:green')
        put_text("Thank You for your participation..")

    else:
        style(put_text("Oops, " +name + ", your score is "+ str(marks)),'color:red')
        style(put_text("Result : FAILED"), 'color:red')
        put_text("Thank You for your participation..")



app.add_url_rule('/','webio_view',webio_view(exam),methods=['GET','POST','OPTIONS'])

if __name__ == '__main__':
    app.run(debug=True, port= 5000)
