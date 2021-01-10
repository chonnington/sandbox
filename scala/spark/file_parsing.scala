
val d1 = spark.read.format("json").load("file.json") 
val d2 = spark.read.json("file.json")

d1.write.format("parquet").save("file.parquet")
d2.write.parquet("file.parquet")