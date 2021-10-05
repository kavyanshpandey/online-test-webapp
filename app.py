from pywebio.input import *
from pywebio.output import *
from flask import Flask
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH


app = Flask(__name__)


def exam():
        
    c = 0

    

    name = input("Please enter your name to start the test ?", type ="text",required="true")


    q1 = radio("Q1. Base language of web?",['javaScript','ASP','PHP','HTML'],required="true")
    if q1 =='HTML':
        c+=1

    q2 = radio("Q2. Which is not a programming language",['Python','HTML','Scala','Java'],required="true")
    if q2 =='HTML':
        c+=1

    q3 = radio("Q3. Secondery memory is also called _____",['Virtual memory','RAM','ROM','Hard drives'],required="true")
    if q3 =='ROM':
        c+=1

    q4 = radio("Q4. functions that is used to get th length of string in Python",['count()','length()','dis()','len()'],required="true")
    if q4 == 'len()':
        c+=1

    q5 = radio("Q5. Which is not a web framework",['Django','React','Numpy','Angular'],required="true")
    if q5 == 'Numpy':
        c+=1

    q6 = radio("Q6. JavaScript is a _______________ language.",['Object-Oriented','High-level','Assembly-language','Object-Based'],required="true")
    if q6 == 'Object-Based':
        c+=1

    q7 = radio("Q7. Which character in JavaScript code will be interpreted as XML markup?",[' !','>','&',' .'],required="true")
    if q7 == '&':
        c+=1

    q8 = radio("Q8.Which object is the main entry point to all client-side JavaScript features and APIs?",['Standard','Location','Window','Position'],required="true")
    if q8 == 'Window':
        c+=1

    q9 = radio("Q9. What kind of scoping does JavaScript use?",['Literal','Lexical','Segmental','Sequential'],required="true")
    if q9 == 'Lexical':
        c+=1

    q10 = radio("Q10. Which keyword is used to define the function in javascript?",['void','int','function','main'],required="true")
    if q10 == 'function':
        c+=1


    if c>7:
        style(put_text("Congratulations, " + name + ", your score is "+ str(c)),'color:green')
        style(put_text("Result : PASSED"),'color:green')
        put_text("Thank You for your participation..")

    else:
        style(put_text("Oops, " +name + ", your score is "+ str(c)),'color:red')
        style(put_text("Result : FAILED"), 'color:red')
        put_text("Thank You for your participation..")



app.add_url_rule('/','webio_view',webio_view(exam),methods=['GET','POST','OPTIONS'])

if __name__ == '__main__':
    app.run(debug=True, port= 5000)
