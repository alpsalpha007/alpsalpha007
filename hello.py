#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1 style="color:red;">Hello, World!</h1>'

@app.route("/about")
def about():
    return "<p>About the project. blablabla</p>"
/* the line below is the decorator, it wraps functions inside a function */
@app.route("/my_div")
def my_div():
    return "This is from MY DIV"

@app.route("/picture")
def pic():
    return '<img src= "/static/Scarface-TWIY-1.jpg" width = "50px">'
