# pip install pyspark

# 1.导包
from pyspark import SparkConf, SparkContext

# 2.创建SparkConf对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

# 3.创建SparkContext对象
sc = SparkContext(conf=conf)

# 4.打印版本
print(sc.version)

# 5.关闭
sc.stop()