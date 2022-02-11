from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/success')
def success():
        return "success"

@app.route('/dojo')
def coding():
        return "dojo"

@app.route('/say/flask')
def hi():
        return "Hi Flask"

@app.route('/say/michael')
def hello():
        return "Hi Michael"

@app.route('/say/john')
def hola():
        return "Hi John"

@app.route('/repeat/<int:num>/<name>')
def thirty_five(num, name):
        int(num)
        return f"hello {num * name}"

# @app.route('/repeat/80/bye')
# def eighty():
#         return "bye" * 80

# @app.route('/repeat/95/dogs')
# def ninety_five():
#         return "dogs" * 95



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.