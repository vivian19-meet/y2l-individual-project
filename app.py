from flask import Flask
import json 
import requests
from flask import Flask, render_template,request
app = Flask(__name__)

add= False
code= "vivi"
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search')
def search():
    return render_template('search.html',add=add)

@app.route('/adminC', methods=["GET",'POST'])
def adminC():
    global add
    if request.method=="POST":
        if(code == request.form["code"]):
            add=True
            return render_template('home.html')
            
    return render_template('adminC.html')

@app.route('/123456787654321345678534678hsdanarlsknrlibigjk')
def addd():
    return render_template("add.html")


if __name__ == '__main__':
    app.run(debug=True)


