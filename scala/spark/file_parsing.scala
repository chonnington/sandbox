
val df = spark.read.format("csv").load("dataset/fb_price-history.csv") 

df.show()

df.write.format("parquet").save("output/fb.parquet")

val df = spark.read.option("header", "true").parquet("output/fb.parquet")

val first_row = df.first() 
df = csv_rows.filter(row => row != skipable_first_row)   

val colName = ""

df.select(colName)
      .stat
      .approxQuantile(colName, Array(0.5), 0.001) //median
      .head