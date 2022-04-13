from app import app
from models.order_list import *
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html', title ="Home", order_list=orders) #uses the jinja 2 template 

@app.route('/orders/<order>')
def order(order):
    return render_template('order.html', title ="Your Order", order_list=orders[int(order)])