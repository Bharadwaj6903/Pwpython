#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q2
from flask import Flask
app= Flask(__name__)
@app.route("/hellow")
def hel():
    return "Hello world"
if __name__=='__main__':
    app.run()


# ![title](fl2.png)
# 

# In[ ]:


#Q3
App Routing means mapping the URLs to a specific function that will handle the logic for that URL.
Modern web frameworks use more meaningful URLs to help users remember the URLs and make navigation simpler. 

Example: In our application, the URL (“/”) is associated with the root or home URL.
    So if our site’s domain was www.example.org and we want to add routing to “www.example.org/hello”, we would use “/hello”.
  
    

To bind a function to an URL path we use the app.route decorator.

By using app routing we as a developer,can access a particular function or a form that runs on the server side


# In[ ]:


#Q1
Flask is a web framework that provides libraries to build lightweight web applications in python. 
It is developed by Armin Ronacher who leads an international group of python enthusiasts (POCCO). 
It is based on WSGI toolkit and jinja2 template engine. Flask is considered as a micro framework.

Advantages of flask:
Higher compatibility with latest technologies
Technical experimentation
Easier to use for simple cases
Codebase size is relatively smaller
High scalability for simple applications,
Easy to build a quick prototype
Routing URL is easy
Easy to develop and maintain applications
Database integration is easy
Small core and easily extensible
Minimal yet powerful platform
Lots of resources available online especially on GitHub


# ![title](fl41.png)

# In[ ]:


#Q4  Above output also belogs to Qustion 4 .i am unable to include 2 photos for 1 cell
from flask import Flask
app= Flask(__name__)
@app.route("/welcome")
def hel():
    return "Welcome to Oracle corporation"

@app.route("/")
def details():
    return "Company name: Oracle Corporation </br>Location : India</br>Contact-Details : 999-999-9999 "
if __name__=='__main__':
    app.run()


# ![title](fl41.png)

# ![title](fl42.png)

# In[ ]:


#Q5)  url_for is used for url binding
from flask import Flask,redirect,url_for,request
app= Flask(__name__)
@app.route("/pass/<int:score>")
def p(score):
    return "Congrats,You have passed with marks "+str(score) 

@app.route("/fail/<int:score>")
def f(score):
    return "Sorry,you have failed and your marks are "+str(score) 

@app.route("/results/<int:marks>")
def res(marks):
    result = ""
   
    if marks>35:
        result="p"
        return redirect(url_for(result,score=marks))
       
    else:
        
        result="f"
        return redirect(url_for(result,score=marks))
         
 

if __name__=='__main__':
    app.run()


# ![title](f51.png)

# In[ ]:




