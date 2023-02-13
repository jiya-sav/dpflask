""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash


''' Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along '''

# Define the User class to manage actions in the 'users' table
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) User represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class Recipes(db.Model):
    __tablename__ = 'recipes'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    recipeid = db.Column(db.Integer, primary_key=True)
    _recipename = db.Column(db.String(255), unique=False, nullable=False)
    _recipelink = db.Column(db.String(255), unique=False, nullable=False)
    _recipetype = db.Column(db.String(255), unique=False, nullable=False)
    _calories = db.Column(db.Integer, unique=False, nullable=False)

    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, recipename, recipeid, recipelink, recipetype, calories):
        self._recipename = recipename    # variables with self prefix become part of the object, 
        self._recipelink = recipelink
        self._recipetype = recipetype
        self._calories = calories

    # a name getter method, extracts name from object
    @property
    def recipename(self):
        return self._recipename
    
    # a setter function, allows name to be updated after initial object creation
    @recipename.setter
    def recipename(self, recipe):
        self._recipename = recipename
    
    # a getter method, extracts email from object
    @property
    def recipeid(self):
        return self._recipeid
    
    # a setter function, allows name to be updated after initial object creation
    @recipeid.setter
    def recipeid(self, recipeid):
        self._recipeid = recipeid
        
    # check if uid parameter matches user id in object, return boolean
    def is_recipeid(self, recipeid):
        return self._recipeid == recipeid
    
    # link
    @property
    def recipelink(self):
        return self._recipelink
    
    @recipelink.setter
    def recipename(self, recipelink):
        self._recipelink = recipelink
    
    # type
    @property
    def recipetype(self):
        return self._recipetype
 
    @recipetype.setter
    def recipetype(self, recipetype):
        self._recipetype = recipetype
        
    # calories
    @property
    def calories(self):
        return self._calories
    
    @calories.setter
    def calories(self, calories):
        self._calories = calories
        
        
    # output content using str(object) in human readable form, uses getter
    # output content using json dumps, this is ready for API response
    def __str__(self):
        return json.dumps(self.read())
    
    
    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from User(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "recipeid": self.recipeid,
            "recipename": self.recipename,
            "recipelink": self.recipelink,
            "recipetype": self.recipetype,
            "calories": self.calories
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, recipename="", recipelink="", recipetype=""):
        """only updates values with length"""
        if len(recipename) > 0:
            self.recipename = recipename
        if len(recipelink) > 0:
            self.recipelink = recipelink
        if len(recipetype) > 0:
            self.recipetype(recipetype)
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

"""Database Creation and Testing """


# Builds working data for testing
def initRecipes():
    """Create database and tables"""
    db.drop_all()
    db.create_all()
    """Tester data for table"""
    r1 = Recipe(recipename='Avocado Toast', recipelink='https://californiaavocado.com/recipes', recipetype='Breakfast', calories=100)
    r2 = Recipe(recipename='Scrambled Eggs', recipelink='https://californiaavocado.com/recipes', recipetype='Breakfast', calories=100)
    r3 = Recipe(recipename='Pancake', recipelink='https://californiaavocado.com/recipes', recipetype='Breakfast', calories=100)
    r4 = Recipe(recipename='Mac and Cheese', recipelink='https://californiaavocado.com/recipes', recipetype='Lunch', calories=2000)
    r5 = Recipe(recipename='Panini Sandwich', recipelink='https://californiaavocado.com/recipes', recipetype='Lunch', calories=2000)
    r6 = Recipe(recipename='Salad', recipelink='https://californiaavocado.com/recipes', recipetype='Lunch', calories=2000)
    r7 = Recipe(recipename='Minestrone Soup', recipelink='https://californiaavocado.com/recipes', recipetype='Dinner', calories=3000)
    r8 = Recipe(recipename='Lasagna', recipelink='https://californiaavocado.com/recipes', recipetype='Dinner', calories=3000)
    r9 = Recipe(recipename='Pasta', recipelink='https://californiaavocado.com/recipes', recipetype='Dinner', calories=3000)
    r10 = Recipe(recipename='Brownies', recipelink='https://californiaavocado.com/recipes', recipetype='Dessert', calories=400)
    r11 = Recipe(recipename='Chocolate Chip Cookies', recipelink='https://californiaavocado.com/recipes', recipetype='Dessert', calories=400)
    r12 = Recipe(recipename='Custard Pudding', recipelink='https://californiaavocado.com/recipes', recipetype='Dessert', calories=400)
 
    recipes = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12]

    # adding my own tester data for the table
    
    # adding my own tests for bookings class
    bookingID = 1
    """Builds sample user/note(s) data"""
    for recipe in recipes:
        try:
            
            '''add a few 1 to 4 notes per user'''
            '''add user/post data to table'''
            recipe.create()
        except IntegrityError:
            '''fails with bad or duplicate data'''
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {recipe.uid}")
    
    

            