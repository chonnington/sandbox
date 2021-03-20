

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("My App")
sc = SparkContext(conf=conf)

a = [1, 2, 3, 4, 5]

a = sc.parallelize(a)

b = [10, 9, 8, 7, 6]

b = sc.parallelize(b)

c = a.cartersian(b)

print(c.take(5))

# Be warned, however, that the Cartesian product is very expensive for large RDDs.