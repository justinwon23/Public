from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def render_lists():
    users = [
   {'first_name' : 'Michael', 'last_name' : 'Choi', 'Full_Name' : 'Michael Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin', 'Full_Name' : 'John Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen', 'Full_Name' : 'Mark Guilllen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel', 'Full_Name' : 'KB Tonel'}
]
    return render_template("index.html", students = users)


if __name__=="__main__":
    app.run(debug=True)

