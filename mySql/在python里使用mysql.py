# pip install pymysql

from pymysql import Connection

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="MYSQLMIMA1",
    autocommit=True  # 设置了自动提交 就不在需要在代码里面确认了
)

# 执行非查询性质的sql语句

# 获取游标对象
cursor = conn.cursor()

# 选择数据库
conn.select_db("test")

# 执行sql语句
# cursor.execute("create table student( id int,name varchar(10),age int );")

# 执行增加sql语句
cursor.execute("INSERT INTO student (id,name,age) VALUES (10,'龙右',22);")
# 确认操作
# conn.commit()

# 执行查询语句
cursor.execute("SELECT * FROM student ")

results = cursor.fetchall()

for i in results:
    print(i)

# 关闭连接
cursor.close()