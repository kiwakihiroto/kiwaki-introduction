# -*- coding: utf-8 -*- 
from flask import Flask, render_template, request 
import os 

app = Flask(__name__, static_folder='.', static_url_path='') 

@app.route('/') 
def index(): 
    return "木脇　潤人" 

if __name__ == '__main__': 
    app.run(debug=True)
