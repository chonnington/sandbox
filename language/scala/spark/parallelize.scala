val data = Seq(("a", 3), ("b", 4), ("a", 1)) 
sc.parallelize(data).reduceByKey((x, y) => x + y) // Default parallelism 
sc.parallelize(data).reduceByKey((x, y) => x + y) // Custom parallelism