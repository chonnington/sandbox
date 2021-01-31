
from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local[2]").setAppName("Spark Count")
sc = SparkContext(conf=conf)

book = sc.textFile("books/breakfast_at_tiffanys.txt")
book.take(1)

words = book.flatMap(lambda x: x.split(" "))
result = book.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)

rdd = sc.parallelize(result.collect())

def toCSVLine(data):
    return ','.join(str(d) for d in data)

rdd = rdd.map(toCSVLine)
rdd.saveAsTextFile('output.csv')

