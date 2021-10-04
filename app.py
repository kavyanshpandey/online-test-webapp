from pywebio.input import *
from pywebio.output import *
from flask import Flask
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH


app = Flask(__name__)


def exam():
        
    c = 0

    

    name = input("Please enter your name to start the test", type ="text")


    q1 = radio("Q1. Which is the base language of the web?",['javaScript','ASP','PHP','HTML'])
    if q1 =='HTML':
        c+=1

    q2 = radio("Q2. Which one of the following is not a programming language?",['Python','HTML','Scala','Java'])
    if q2 =='HTML':
        c+=1

    q3 = radio("Q3. Secondary memory is also called _____.",['Virtual memory','RAM','ROM','Hard drives'])
    if q3 =='ROM':
        c+=1

    q4 = radio("Q4. Which function is used to get the length of a string in Python?",['count()','length()','dis()','len()'])
    if q4 == 'len()':
        c+=1

    q5 = radio("Q5. Which one of the following is not a web framework?",['Django','React','Numpy','Angular'])
    if q5 == 'Numpy':
        c+=1

    if c>3:
        style(put_text("Congratulations, " + name + ". Your score is "+ str(c)),'color:green')
        style(put_text("Result : PASS"),'color:green')
        put_text("Thank You for participating..")

    else:
        style(put_text("Oops, " + name + ". Your score is "+ str(c)),'color:red')
        style(put_text("Result : FAIL"), 'color:red')
        put_text("Thank You for participating..")



app.add_url_rule('/','webio_view',webio_view(exam),methods=['GET','POST','OPTIONS'])

if __name__ == '__main__':
    app.run(debug=True, port= 5000)
