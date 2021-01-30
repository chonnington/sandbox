
data = [("a", 3), ("b", 4), ("a", 1)]

sc.parallelize(data).reduceByKey(lambda x, y: x + y) # Default parallelism 
sc.parallelize(data).reduceByKey(lambda x, y: x + y, 10) # Custom parallelism