#!/usr/bin/env python
# _*_ coding:  utf-8  _*_
#@Time  :  2020/1/8 
#@Author:  Leo

from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    #默认会从templates文件下找文件
    #ctrl shift 清空浏览器缓存
    return render_template("profile/user.html")

@app.route('/profile/')
def profile():
    context = {
        "username": "逻辑教育",
        "age": 18,
        "books": {
            "python": 33,
            "java": 55,
        },
        "book": ["python", "Java", "php"]

    }
    # return render_template("index.html", context=context)
    return render_template("index.html", **context)

if __name__ == '__main__':
    app.run()