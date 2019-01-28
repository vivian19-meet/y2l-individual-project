from flask import Flask
import json 
import requests
from flask import Flask, render_template,request, redirect
from database import *
app = Flask(__name__)

add= False
code= "my code"
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
    return render_template('univ_info.html',u=u,add=add)
@app.route('/test')
def test():
    
    return render_template('test.html')
@app.route('/lang')
def lag():
    global ll
    ll=True
    return render_template('test.html',ll=ll)
@app.route('/math')
def math():
    global mm
    mm=True
    return render_template('test.html',mm=mm)
@app.route('/hhh')
def hhh():
    global hh
    hh=True
    return render_template('test.html',hh=hh)
@app.route('/mu')
def music():
    global mu
    mu=True
    return render_template('test.html',mu=mu)
@app.route('/kk')
def sport():
    global kk
    kk=True
    return render_template('test.html',kk=kk)
@app.route('/so')
def social():
    global so
    so=True
    return render_template('test.html',so=so)
@app.route('/ii')
def introvert():
    global ii
    ii=True
    return render_template('test.html',ii=ii)


@app.route('/adminC', methods=["GET",'POST'])
def adminC():
    global add
    global tt
    if request.method=="POST":
        if(code == request.form["code"]):
            add=True
            return redirect('/')     
        tt=True
    return render_template('adminC.html', add=add)

@app.route('/123456787654321345678534678hsdanarlsknrlibigjk',methods=["GET",'POST'])
def addd():
    if request.method=="POST":
        add_univ(request.form["name"],request.form["location"],
        request.form["fields"],request.form["logo"],request.form["link"],request.form["pics"].split(","))
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
@app.route('/delete/<id>',methods=['GET', 'POST'],)
def delete(id):
    if request.method == 'GET':
        delete_univ_by_id(id)
        return redirect('/search')
    return redirect('/search_results')

'''
@app.route('/searchA', )
def searchA():
    
    else:
        return render_template('search.html',add=add)
'''

if __name__ == '__main__':
    app.run(debug=True)


