
from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local[2]").setAppName("Spark Count")
sc = SparkContext(conf=conf)

A, B, Z = 'A', 'B', 'Z'

data = [(A, 2.),
        (A, 4.),
        (A, 9.),
        (B, 10.),
        (B, 20.),
        (Z, 3.),
        (Z, 5.),
        (Z, 8.),
        (Z, 12.)]

rdd = sc.parallelize(data)

result = rdd.map(lambda x: (x[0], list(x[1:])))

# todo: this is bombing out.. gotta fix data format
sumCount = rdd.combineByKey((lambda x: (x, 1)),
                            (lambda x, y: (x[0] + y, x[1] + 1)),
                            (lambda x, y: (x[0] + y[0], x[1] + y[1])))

sumCount.map(lambda key, xy: (key,
                              xy[0]/xy[1])).collectAsMap()

