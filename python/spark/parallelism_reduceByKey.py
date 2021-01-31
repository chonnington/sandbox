

from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local[2]").setAppName("Spark Count")
sc = SparkContext(conf=conf)

data = [("a", 3), ("b", 4), ("a", 1)]

a = sc.parallelize(data).reduceByKey(lambda x, y: x + y)  # Default parallelism
b = sc.parallelize(data).reduceByKey(lambda x, y: x + y, 10)  # Custom parallelism

b.take(2)
