"""
@author:maohui
@time:2022/5/12 14:45
"""

import pymysql

# 1.连接mysql
conn =pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd="123456",charset='utf8',db='users')
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
# 2.发送指令(切记：！！！！千万不要用字符串格式化去sql拼接，会被sql注入)
sql = "update user set sexy=%s where username=%s"
cursor.execute(sql,["female","zhangsan"])
conn.commit()
# 3.关闭连接
cursor.close()
conn.close()