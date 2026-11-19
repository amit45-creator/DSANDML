from flask import Flask

'''
It creates an instance of the flask class, which will be your wsgi (web server gateway interface) application.
'''

### wsgi application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this flask course. hello "

@app.route("/index")
def index():
    return "Welcome to this flask course. hello "

if __name__=="__main__":
    app.run(debug=True)



