# 异常处理
# try :
#     可能会出错的代码
# except:
#     出错后处理的代码

# 捕获指定异常
try:
    print(name)
except NameError:
    print("名字错误")