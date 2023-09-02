#!/usr/bin/env python

import json
from flask import Flask,request

app=Flask(__name__)
@app.route('/')
def index():
    return json.dumps({'name': 'Rishu',
                       'email': 'barnwalrishu078@gmail.com','age':19,'place':'Bhubanewar'})
@app.route('/check')
def getname():
    return json.dumps({'eligible': 'True'})

@app.route('/prime/<int:a>')
def prime(a):
    flag=0
    for i in range(2,a):
        if(a%i==0):
            flag=1
            break
    if(flag==0):
        res={"num":a,"prime":True}
    else:
        res={"num":a,"prime":False}
    return json.dumps(res)
@app.route('/writing_query')
def w_query():
    #breakpoint()
    language = request.args.get('language', 'Not Language Defined')
    return language

app.run()
