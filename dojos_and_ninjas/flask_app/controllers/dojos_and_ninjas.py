from flask import Flask, render_template, request, redirect
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask_app import app

@app.route('/')
def index():
    dojos = Dojo.get_all()
    return render_template("index.html", dojos = dojos)



@app.route('/create_dojo', methods = ['POST'])
def create_dojo():
    data = {
        "name" : request.form["name"]
    }

    Dojo.save(data)
    return redirect('/')

@app.route('/dojos/<int:id>')
def show_member(id):
    data = {
        "id" : id
    }
    ninjas = Ninja.get_ninjas(data)
    return render_template("read_one.html", ninjas = ninjas)

@app.route('/ninjas/')
def ninjas():
    dojos = Dojo.get_all()
    
    return render_template("ninjas.html", dojos = dojos)

@app.route('/create/ninja', methods = ['POST'])
def create_ninja():
    data = {
        "dojo_id" : request.form['dojo_id'],
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age']
    }

    Ninja.save(data)
    return redirect(f'/dojos/{request.form["dojo_id"]}')



