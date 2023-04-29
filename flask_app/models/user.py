from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash #this lets us write the flash messages
import re

class User:
    def __init__(self, data):       #we input the user information from DB
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']    #don't store in session
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_user(cls, data): #use the values that you are checking from homepage
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        
        result = connectToMySQL("BeatsPyTopia_schema").query_db(query, data)

        return result       #make sure to use ^^^^^ use the right DB on everything

    # @classmethod
    # def get_user_by_username(cls, data):
    #     query = "SELECT * FROM users WHERE first_name, last_name = %(first_name)s, %(last_name);"
    #     #query works without "last_name = %(first_name)s, but add just in case"
    #     results = connectToMySQL('BeatsPyTopia_schema').query_db(query, data)

    #     users = []              #make sure to ^^^^^ use the right DB

    #     for item in results:
    #         users.append(User(item))

    #     print(users)

    #     return results

    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('BeatsPyTopia_schema').query_db(query, data)

        users = []

        for item in results:
            users.append(User(item))

        return users

    @staticmethod
    def validate_user(data):
        is_valid = True
#create one for name so that they only have letters (copy end for email)
        name_regex = re.compile(r'^[a-zA-Z]+$')
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        
        #email must follow pattern
        if not email_regex.match(data['email']):
            is_valid = False
            flash("Please provide a valid email")

        #first and last name must follow pattern
        if not name_regex.match(data['first_name']):
            is_valid = False
            flash("Please have the first name use letters ONLY")
        if not name_regex.match(data['last_name']):
            is_valid = False
            flash("Please have the last name use letters ONLY")

        #if first and last name don't have more than 2 char, flash message
        if len(data['first_name']) < 2:
            is_valid = False
            flash("First Name must be at least 2 characters")
        if len(data['last_name']) < 2:
            is_valid = False
            flash("Last name must be at least 2 characters")

        #email must be unique
#use this method ONLY when something needs to be unique (Ex: username, email, etc.)
        if len(User.get_user_by_email(data)) != 0: 
            is_valid = False
            flash("Email already in use")
        #password must be at least 8 characters
        if len(data['password']) < 8:
            is_valid = False
            flash("Password must be at least 8 characters")

        #password and confirm_password field must match
        if data['password'] != data['confirm_password']:
            is_valid = False
            flash("Password and confirm password must match exactly")

        return is_valid