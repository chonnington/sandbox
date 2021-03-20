from pyspark import SparkConf, SparkContext


conf = SparkConf().setMaster("local").setAppName("My App")
sc = SparkContext(conf=conf)

num = sc.parallelize(list(range(25)))

seqOp = (lambda x, y: (x[0] + y, x[1] + 1))
combOp = (lambda x, y: (x[0] + y[0], x[1] + y[1]))

sc.parallelize([1, 2, 3, 4]).aggregate((0, 0), seqOp, combOp)

sc.parallelize([]).aggregate((0, 0), seqOp, combOp)
