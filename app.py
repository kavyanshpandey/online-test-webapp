from pywebio.input import *
from pywebio.output import *
from flask import Flask
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH


app = Flask(__name__)


def exam():
        
    c = 0
  
    put_markdown("<h1>Quiz</h1>")
    name = input("Please enter your name to start the test: ", type ="text")

    q1 = radio("Q1. Base language of the web is ?",['javaScript','ASP','PHP','HTML'])
    if q1 =='HTML':
        c+=1

    q2 = radio("Q2. Which of the following is not a programming language ?",['Python','HTML','Scala','Java'])
    if q2 =='HTML':
        c+=1

    q3 = radio("Q3. Secondery memory is also known as _____.",['Virtual memory','RAM','ROM','Hard drives'])
    if q3 =='ROM':
        c+=1

    q4 = radio("Q4. Function that is used to get the length of a string in Python is ?",['count()','length()','dis()','len()'])
    if q4 == 'len()':
        c+=1

    q5 = radio("Q5. Which of the following is not a web framework ?",['Django','React','Numpy','Angular'])
    if q5 == 'Numpy':
        c+=1

    if c>3:
        style(put_text("Congratulations, " + name + ", your score is "+ str(c)),'color:green')
        style(put_text("Result : PASSED"),'color:green')
        put_text("Thank You for your participation..")

    else:
        style(put_text("Oops, " +name + ", your score is "+ str(c)),'color:red')
        style(put_text("Result : FAILED"), 'color:red')
        put_text("Thank You for your participation..")

"""A method to validate the name entered by user"""
def validate_name(name):
	#removing all spaces from the input name
	name = name.replace(" ","")
	#performing validation checks
	#check 1 : Name must not be empty
	#check 2 : It should contain only alphabets [a-z] or [A-Z]
	if(name == "" or not(name.isalpha())):
		return("Please enter a non empty name consisting of alphabets only")


app.add_url_rule('/','webio_view',webio_view(exam),methods=['GET','POST','OPTIONS'])

if __name__ == '__main__':
    app.run(debug=True, port= 5000)
