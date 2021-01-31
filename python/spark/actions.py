
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("My App")
sc = SparkContext(conf=conf)

inputRDD = sc.textFile("README.md")

errorsRDD = inputRDD.filter(lambda x: "error" in x)
warningsRDD = inputRDD.filter(lambda x: "warning" in x)
badLinesRDD = errorsRDD.union(warningsRDD)

print("Input had " + badLinesRDD.count() + " concerning lines" )
print("Here are 10 examples:")

for line in badLinesRDD.take(10):
    print(line)