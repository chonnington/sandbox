
from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local[2]").setAppName("Spark Count")
sc = SparkContext(conf=conf)

key_val = [('Key1', 'Value1'), ('Key1', 'Value2'), ('Key1', 'Value3'), ('Key2', 'Value4'), ('Key2', 'Value5')]
rdd = sc.parallelize(key_val)

rdd.mapValues(lambda x: (x, 1)).reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))