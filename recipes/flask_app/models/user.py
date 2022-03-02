from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, render_template, redirect, session, request
from flask_app import bcrypt

import re # the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls,data):
        query = "INSERT into users (first_name,last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL('recipes_schema').query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM emails;'
        results = connectToMySQL('recipes_schema').query_db(query)

        users = []
        for user in results:
            users.append(cls(user))
        
        return users
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('recipes_schema').query_db(query, data)
        print(results)
        return cls(results[0])

    @classmethod
    def get_one_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('recipes_schema').query_db(query, data)
        if results:
            return cls(results[0])
        return False

    @staticmethod
    def validation(form_data):
        is_valid = True

        if len(form_data['first_name']) < 1:
            is_valid = False
            flash("First Name is required", "err_user_first_name")
        
        if len(form_data['last_name']) < 1:
            is_valid = False
            flash("Last Name is required", "err_user_last_name")
        
        if len(form_data['email']) < 1:
            is_valid = False
            flash("Email is required", "err_user_email")
        elif not EMAIL_REGEX.match(form_data['email']): 
            flash("Invalid email address!", "err_user_email")
            is_valid = False
        else:
            potentail_user = User.get_one_by_email({'email': form_data['email']})
            if potentail_user:
                flash("Email is already taken", 'err_user_email')
                is_valid = False
        
        if len(form_data['password']) < 1:
            is_valid = False
            flash("Password is required", "err_user_password")
        
        if len(form_data['confirm_password']) < 1:
            is_valid = False
            flash("Confirm Password is required", "err_user_confirm_password")
        elif form_data['password'] != form_data['confirm_password']:
            is_valid = False
            flash("Passwords do not match", 'err_user_confirm_password')
        
        return is_valid


    @staticmethod
    def validate_login(form_data):
        is_valid = True


        if len(form_data['email']) < 1:
            is_valid = False
            flash("Email is required", "err_user_email_login")
        elif not EMAIL_REGEX.match(form_data['email']): 
            flash("Invalid email address!", "err_user_email_login")
            is_valid = False
        
        
        if len(form_data['password']) < 1:
            is_valid = False
            flash("Password is required", "err_user_password_login")
        
        else:
            potential_user = User.get_one_by_email({'email': form_data['email']})
            if not potential_user:
                is_valid = False
                flash("User doesn't exist", "err_user_email_login")
            elif not bcrypt.check_password_hash(potential_user.password, form_data['password']):
                is_valid= False
                flash("password is not correct", "err_user_password_login")
            else:
                session['uuid'] = potential_user.id

        

        
        return is_valid
    
    
    
    # @classmethod
    # def get_last_email(cls):
    #     query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
    #     results = connectToMySQL('user_login').query_db(query)
    #     return User(results[0])



    # @staticmethod
    # def validate_user( user ):
    #     is_valid = True
    #     # test whether a field matches the pattern
    #     if not EMAIL_REGEX.match(user['name']): 
    #         flash("Invalid email address!")
    #         is_valid = False
    #     else: flash(f"valid email is {user['name']}")
    #     return is_valid

