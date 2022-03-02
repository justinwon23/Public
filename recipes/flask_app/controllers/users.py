
from flask import Flask, render_template,request, redirect, session
from flask_app import app, Bcrypt
from flask_app.models.user import User
from flask_app.models.recipes import Recipe

bcrypt = Bcrypt(app)


@app.route('/')
def index():
    if 'uuid' in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'uuid' not in session:
        return redirect('/')
    user = User.get_one({'id':session['uuid']})
    recipes = Recipe.get_all()

    edits = Recipe.get_recipes({'id':session['uuid']})
    return render_template('dashboard.html', user = user, recipes = recipes, edits = edits)

@app.route('/delete/<int:id>')
def delete(id):
    Recipe.delete({"id":id})
    return redirect('/dashboard')

@app.route('/recipes/new')
def new_recipe():
    if 'uuid' not in session:
        return redirect('/')
    


    return render_template('recipe_new.html')

@app.route('/recipes/<int:id>')
def view_recipe(id):
    data = {
        "id" : id
    }
    user = User.get_one({'id':session['uuid']})
    recipe = Recipe.get_one(data)

    return render_template ('/recipe.html', recipe = recipe, user=user)

@app.route('/recipe/create', methods = ['POST'])
def save():
    is_valid= Recipe.validate(request.form)
    if not is_valid:
        return redirect('/recipes/new')

    data = {
        "name" : request.form['name'],
        "instructions" : request.form['instructions'],
        "description" : request.form['description'],
        "date_made_on" : request.form['date_made_on'],
        "under_30_mins" : request.form['under_30_mins'],
        "user_id" : session['uuid']
        
        }
    Recipe.save(data)
    return redirect('/dashboard')
    
    
    

@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    if 'uuid' not in session:
        return redirect('/')
    
    data = {
        "id":id
    }
    recipe = Recipe.get_one(data)

    return render_template('recipe_edit.html', recipe = recipe)

@app.route('/recipes/modify', methods= ['POST'])
def update():
    Recipe.edit(request.form)

    return redirect('/dashboard')


@app.route('/user/create', methods=['POST'])
def user_create():
    #validate
    is_valid = User.validation(request.form)
    if not is_valid:
        return redirect('/')

    #bycrypt
    password_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password' : password_hash

    }

    #create the user
    id = User.create(data)

    #store into session -> UUID - the row given back to me after creation
    session['uuid'] = id

    return redirect('/')

@app.route('/logout')
def logout():
    del session['uuid']

    return redirect('/')

@app.route('/user/process_login', methods=['POST'])
def user_login():
    is_valid = User.validate_login(request.form)
    if not is_valid:
        return redirect('/')
    
    else:

        return redirect('/')









