from flask import Flask, session
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = "So Secr3t"

bcrypt = Bcrypt(app)