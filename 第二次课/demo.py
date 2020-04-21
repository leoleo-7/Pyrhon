#!/usr/bin/env python
# _*_ coding:  utf-8  _*_
#@Time  :  2020/1/8 
#@Author:  Leo

from flask import Flask,url_for,redirect,request

app = Flask(__name__)

@app.route('/')
def index():
    print(url_for("article_list",aid=3))
    return  "hello world"

@app.route('/article/<aid>/')
def article_list(aid):
    return "article list {}".format(aid)

@app.route('/signin/', methods=['GET','POST'])
def login():
    return 'login'

@app.route('/profile/', methods=['GET','POST'])
def profile():
    name = request.args.get("leo")
    #此处是后面的传参 http://127.0.0.1:2000/profile/?leo=lei
    #get请求
    #request.form.get("name")
    #post请求

    # if name:
    #     return name
    # else:
    #     return redirect("/login/")

    if not name:
        return redirect(url_for('login'),code = 301)  #url_for 指定函数url
    else:
        return name

if __name__=="__main__":
    app.run()