import time

from pywebio.input import *
from pywebio.output import *
from flask import Flask
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH

app = Flask(__name__)

def exam():
    c = 0
    put_markdown('## Welcome To Online Python Test Program ')


    name = input("Please enter your name to start the test", type ="text")
    if name == '':
        with popup("Please Enter your name"):
            put_text("Your cannot go further without entering your Name ")
        return exam()

    q1 = radio("Base language of web?",['javaScript','ASP','PHP','HTML'])
    put_processbar('bar')
    if q1 == 'HTML':

    name = input("Please enter your name to start the test ?", type ="text")


    q1 = radio("Q1. Base language of web?",['javaScript','ASP','PHP','HTML'])
    if q1 =='HTML':

        c+=1

    q2 = radio("Q2. Which is not a programming language",['Python','HTML','Scala','Java'])
    if q2 =='HTML':
        c+=1

    q3 = radio("Q3. Secondery memory is also called _____",['Virtual memory','RAM','ROM','Hard drives'])
    if q3 =='ROM':
        c+=1

    q4 = radio("Q4. functions that is used to get th length of string in Python",['count()','length()','dis()','len()'])
    if q4 == 'len()':
        c+=1

    q5 = radio("Q5. Which is not a web framework",['Django','React','Numpy','Angular'])
    if q5 == 'Numpy':
        c+=1

    q6 = radio("Is Python case sensitive?", ['yes', 'NO'])
    if q6 == 'yes':
        c+=1

    q7 = select("Choose which is not a keyword in python",["False", "class", "Woom", "global"])
    if q7 == 'Woom':
        c+=1

    q8 = radio("Is touple mutable or not?",['Yes', 'NO'])
    if q8 == 'NO':
        c+=1

    q9 = radio("Do python support looping in its code? ",['yes','No'])
    if q9 == 'yes':
        c+=1

    q10 = radio("Can we use Switch staments in python",['yes','No'])
    if q10 == 'No':
        c+=1

    q11 = radio("Is python interpreted langugae?", ['yes', 'No'])
    if q11 == 'yes':
        c+=1

    q12 = radio("can Array in python hold any type of data?", ['yes','No'])
    if q12 == 'No':
        c+=1

    q13 = checkbox("What is Full form of PEP?", options=['Python Enhancement Proposal', 'Python Enchantment Propasl','Programming Enhancment Proposition', 'Python Enrichment Program'])
    if q13 == 'Python Enhancement Proposal':
        c+=1


    style(put_markdown("## Wait Please ! Unitl We Processing your results"), 'color:blue')

    put_processbar('bar')
    for i in range(1,11):
        set_processbar('bar', i/10)
        time.sleep(1)

    put_markdown("# Here is your Result")
    if c>=10:
         style(put_text("\tCongratulations, " + name + ", your score is "+ str(c)),'color:green')
         style(put_text("\tResult : Great Score keep polishing your Skills in Python"),'color:green')
         style(put_text("\tThank You for your participation.."), 'color:green')
    elif c>=5 and c<10:
        style(put_text("\tCongratulations, " + name + ", your score is " + str(c)), 'color:green')
        style(put_text("\tResult : Nice Try ! You have to work a little bit more in python"), 'color:green')
        style(put_text("\tThank You for your participation.."), 'color:green')
    else:
          style(put_text("Oops, " +name + ", your score is "+ str(c)),'color:red')
          style(put_text("Result : Sorry You Failed in this test. Try Again for better Score"), 'color:red')
          style(put_text("\tThank You for your participation.."), 'color:red')



app.add_url_rule('/','webio_view',webio_view(exam),methods=['GET','POST','OPTIONS'])

if __name__ == '__main__':
    app.run(debug=True, port= 5000)
