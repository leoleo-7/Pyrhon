#!/usr/bin/env python
# _*_ coding:  utf-8  _*_
#@Time  :  2020/1/8 
#@Author:  Leo

from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

#自定义过滤器
#my_cut是过滤器的名字
@app.template_filter("my_cut")
def cut(value):
    return value.replace("hello", "")

@app.template_filter("handle_time")
def handle_time(time):
    '''
    大于一分钟--》刚刚
    大于一分钟小于一小时--》xx分钟之前
    大于一小时小于24个小时--》xx小时以前
    大于24小时
    :param time:
    :return:
    '''
    if isinstance(time, datetime):
        now = datetime.now()
        # total_seconds() 得到总秒数
        timestamp = (now - time).total_seconds()
    if timestamp < 60:
        return "刚刚"
    elif timestamp >=60 and timestamp < 60*60:
        return "%s分钟之前" % int(timestamp/60)
    elif timestamp >= 60*60 and timestamp <= 60*60*24:
        return "%s小时之前" % int(timestamp/(60*60))
    else:
        return time

@app.route('/')
def index():
    context = {
        "username": 'hello world',
        "name": 'leo',
        "age": -18,
        "es": "<script>alert('hello')</script>",
        "books": [
            "Python", "php", "java"
        ],
        "now_time": datetime(2020, 4, 11, 21, 22, 00)
    }
    return render_template('index.html', **context)



if __name__=="__main__":
    app.run()