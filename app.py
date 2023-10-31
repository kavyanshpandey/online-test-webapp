from pywebio.input import *
from pywebio.output import *
from flask import Flask
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from pywebio.session import *

app = Flask(__name__)


def exam():
        
    c = 0
  
    put_html("<h1>Quiz</h1>")

    name = input("Please enter your name to start the test", type ="text", validate = validate_name)


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

    if c>3:
    	message = [style(put_html("<h1 style='display:inline;border-bottom:0px'>Congratulations !! </h1>"+ name + ", your score is <b>"+ str(c) + "</b><br><br>") ,'color:green;'),style(put_html("<p>Result : <b>PASSED</b></p>"),'color:green'), put_html("<b>Thank You for your participation.</b>")]
    	popup("Result", content=message, size='large', implicit_close=True, closable=True)
    else:
    	message = [style(put_html("<h1 style='display:inline;border-bottom:0px'>Oops! " + "</h1>" + name + ", your score is <b>"+ str(c) + "</b><br><br>"),'color:red'), style(put_html("<p>Result : <b>FAILED</b></p>"), 'color:red') , put_html("<b>Thank You for your participation.</b><br><br>"), style(put_link('Retry ↺',""), 'color:red;align-content: center;border-radius: 5px;color:#f9faf8;padding: 5px 100px;text-align:center;align-items : center;background-color: white;\
            background-image: linear-gradient(270deg, #8cf5f5 1%, #0a43f3 100%);')]
    	popup("Result", content=message, size='large', implicit_close=True, closable=True)
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

# Main function to activate 
if __name__ == '__main__':
    app.run(debug=True, port= 5000)