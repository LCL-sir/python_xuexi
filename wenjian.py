# 打开文件
# ls = open("D:\IdeaProjects\python_xuexi\测试.txt", "r", encoding="utf-8")

# 读取文件
# # du = ls.read()
# du1 = ls.readlines()
# # print(du)
# print(du1)
#
# # 关闭文件
# ls.close();

# 写入文件 -- w 模式 会把原来的文件内容清空，然后在写入
# ls = open("D:\IdeaProjects\python_xuexi\测试.txt", "w", encoding="utf-8")
#
# ls.write("在程序中写入")
# # 写入后刷新到硬盘里面去
# ls.flush()

# 写入文件 -- a 不会清空原来的内容
ls = open("D:\IdeaProjects\python_xuexi\测试.txt", "a", encoding="utf-8")
ls.write("追加")
ls.flush()
ls.close()
