"""
@author:maohui
@time:2022/5/10 14:41
"""


from flask import Flask, render_template, request

app=Flask(__name__)

#创建了网址 /show/info和函数index的对应关系
#以后用户在浏览器上访问这个/show/info，网址自动执行index函数
@app.route("/show/info")
def index():

    #默认：去当前项目目录的templates文件夹中去找
    return render_template("index.html")

@app.route("/news")
def get_news():
    return render_template("news.html")

# 注册
@app.route("/register",methods=["POST","GET"])
def do_register():
    if request.method=="POST":
        # 1.接受用户通过post形式发送过来的数据
        print(request.form)
        #或者用.args获取（geti请求）
        #或者user=request。from。get（“user”）
        # 或者hobby_list=request。from。getlist（“hobby”）
        # 2.给用户返回结果
        return "注册成功"
    else:
        return render_template("register.html")

# 登录
@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=='POST':
        print(request.form.get("username"))
        print(request.form.get("pwd"))
        return "登录成功"
    else:
        return render_template("login.html")
if __name__=='__main__':
    app.run()