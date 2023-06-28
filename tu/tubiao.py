# 导包
from pyecharts.charts import Line
# 创建对象
line=Line();

# 添加x轴数据
line.add_xaxis(["中国","美国","英国"]);

# 添加y轴数据
line.add_yaxis("GDP",[30,20,10])

#  生成图表
line.render()