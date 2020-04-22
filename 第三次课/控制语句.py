#!/usr/bin/env python
# _*_ coding:  utf-8  _*_
#@Time  :  2020/1/8 
#@Author:  Leo

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def control_demo():
    context = {
        "username": 'leo',
        "books": [
            "Python", "php", "java"
        ],
        "users": {
            "name": "leo",
            "age": 18,
            "address": "css"
        }

    }
    return render_template('control_demo.html', **context)



if __name__=="__main__":
    app.run()