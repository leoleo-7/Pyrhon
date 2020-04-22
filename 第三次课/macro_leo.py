#!/usr/bin/env python
# _*_ coding:  utf-8  _*_
#@Time  :  2020/1/8 
#@Author:  Leo

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def macro():
    context = {

    }
    return render_template('macro.html', **context)



if __name__=="__main__":
    app.run()