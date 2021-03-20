import org.apache.spark.sql.hive.HiveContext

val hiveCtx = new org.apache.spark.sql.hive.HiveContext(sc) 
val rows = hiveCtx.sql("SELECT name, age FROM users")

val firstRow = rows.first() 
println(firstRow.getString(0)) // Field 0 is the name