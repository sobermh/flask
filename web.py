"""
@author:maohui
@time:2022/5/10 14:41
"""


from flask import Flask, render_template, request
import pymysql

app=Flask(__name__)

#创建了网址 /show/info和函数index的对应关系
#以后用户在浏览器上访问这个/show/info，网址自动执行index函数
@app.route("/index")
def index():
    #1.找到index.html的文件，读取所有的内容
    #2.找到内容中的“特殊的占位符”，将数据替换
    #3.将替换完成的字符串返回给用户的浏览器
    #默认：去当前项目目录的templates文件夹中去找
    names=["zhangsan","lisi","毛辉","俞琦"]
    ages=["18","23","1"]
    return render_template("index.html",title="俞琦",name_list=names,age_list=ages)

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
        username=request.form.get("username")
        password = request.form.get("pwd")
        sexy=request.form.get("gender")
        # 连接数据库
        conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd="123456",charset='utf8',db='users')
        cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
        #发送指令
        sql="insert into user(username,password,sexy) values(%s,%s,%s)"
        cursor.execute(sql,[username,password,sexy])
        conn.commit()
        #关闭连接
        cursor.close()
        conn.close()
        return "注册成功"
    else:
        return render_template("register.html")

# 登录
@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=='POST':
        username=request.form.get("username")
        password=request.form.get("pwd")
        # 连接数据库
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd="123456", charset='utf8', db='users')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 发送指令
        sql = "select * from user where username=%s and password=%s"
        cursor.execute(sql, [username, password])
        data=cursor.fetchone()
        # 关闭连接
        cursor.close()
        conn.close()
        if (data != None):
            return "登录成功"
        else:
            return "用户不存在"
    else:
        return render_template("login.html")

@app.route("/js")
def js_do():
    return render_template("js.html")

@app.route("/jquery")
def query_do():
    return render_template("jquery.html")
if __name__=='__main__':
    app.run(host='0.0.0.0')