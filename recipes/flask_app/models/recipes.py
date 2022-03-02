from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, render_template, redirect, session, request
from flask_app import bcrypt

import re # the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.under_30_mins = data['under_30_mins']
        self.instructions = data['instructions']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.date_made_on = data['date_made_on']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('recipes_schema').query_db(query)
        # Create an empty list to append our instances of friends
        recipes = []
        # Iterate over the db results and create instances of friends with cls.
        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes

    @classmethod
    def get_one(cls, data):
        query = "Select * from recipes WHERE id = %(id)s";
        result = connectToMySQL('recipes_schema').query_db(query, data)
        print(result)
        return cls(result[0])

    
    @classmethod
    def save (cls, data):
        query = "INSERT INTO recipes (name, description, instructions, under_30_mins, date_made_on, user_id, created_at, updated_at) VALUES ( %(name)s, %(description)s, %(instructions)s, %(under_30_mins)s,%(date_made_on)s, %(user_id)s, NOW(), NOW());"
        return connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def edit(cls,data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions =%(instructions)s, under_30_mins = %(under_30_mins)s WHERE id = %(id)s";
        result = connectToMySQL('recipes_schema').query_db(query, data)
        return result
    
    @classmethod
    def get_recipes(cls, data):
        query = "SELECT * FROM recipes join users on users.id = recipes.user_id WHERE user_id = %(id)s;"
        results = connectToMySQL('recipes_schema').query_db(query, data)

        if results:
            recipes_list = []
            for recipe in results:
                recipes_list.append(cls(recipe))
            return recipes_list
        return []

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        
        return connectToMySQL('recipes_schema').query_db(query,data)

    @staticmethod
    def validate(form_data):
        is_valid = True

        if len(form_data['name']) < 3:
            is_valid = False
            flash("Name is required", "err_recipe_name")
        
        if len(form_data['description']) < 3:
            is_valid = False
            flash("Description is required", "err_recipe_description")
        
        if len(form_data['instructions']) < 3:
            is_valid = False
            flash("Instructions are required", "err_recipe_instructions")

        
        return is_valid