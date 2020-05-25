import json
from flask import Flask, render_template,redirect,jsonify
from flask import request
from flask import *  
import os
import ast
import json
import requests
import socket
import pandas as pd
app = Flask(__name__)
app.secret_key = "soorajit"
@app.route('/',methods=['GET', 'POST'])
def house():
    return render_template('house/house.html')

@app.route('/chatbot',methods=['GET', 'POST'])
def chatbot():
    msg=request.args.get('msg', 0, type=str)
    print(msg)
    return jsonify(data='launched')
if __name__ == '__main__':
   app.run(debug = True,host="0.0.0.0",port=2020)
    
