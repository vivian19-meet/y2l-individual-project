from flask import Flask
import json 
import requests
from flask import Flask, render_template,request, redirect
from database import *
app = Flask(__name__)

add= False
code= "vivi"
@app.route('/')
def home():
    return render_template('home.html' ,add=add)
@app.route('/log_out')
def log_out():
    global add
    add=False 
    return redirect('/')

@app.route('/un_info/<id>')
def un_info(id):
    u = get_univ_by_id(id)

    return render_template('univ_info.html',u=u)


@app.route('/adminC', methods=["GET",'POST'])
def adminC():
    global add
    if request.method=="POST":
        if(code == request.form["code"]):
            add=True
            return redirect('/')
            
    return render_template('adminC.html')

@app.route('/123456787654321345678534678hsdanarlsknrlibigjk',methods=["GET",'POST'])
def addd():
    if request.method=="POST":
        add_univ(request.form["name"],request.form["location"],request.form["fields"])

        return render_template("add.html")
    else:
        return render_template("add.html")

@app.route('/search_results')
def search_results():

    return render_template('search_results.html')

@app.route('/search',methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        fields = request.form['search']
        global universities
        universities = get_univ_by_field(fields)
        universities = get_univ_by_field(fields)
        return render_template('search_results.html',universities=universities)
    return render_template('search.html',add=add)

'''
@app.route('/searchA', )
def searchA():
    
    else:
        return render_template('search.html',add=add)
'''

if __name__ == '__main__':
    app.run(debug=True)


