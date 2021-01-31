import org.apache.spark.sql.catalyst.encoders.ExpressionEncoder
import org.apache.spark.sql.Encoder
import spark.implicits._

val employeeDF = spark.sparkContext.textFile("examples/src/main/resources/employee.txt").map(_.split(",")).map(attributes => Employee(attributes(0), attributes(1).trim.toInt)).toDF()

employeeDF.createOrReplaceTempView("employee")

val youngstersDF = spark.sql("SELECT name, age FROM employee WHERE age BETWEEN 18 AND 30")

youngstersDF.map(youngster => "Name: " + youngster(0)).show()

// matchSummaryT.createOrReplaceTempView("match_desc")
// missSummaryT.createOrReplaceTempView("miss_desc")
// spark.sql("""SELECT a.field, a.count + b.count total, a.mean - b.mean delta
//              FROM match_desc a INNER JOIN miss_desc b ON a.field = b.field
//              WHERE a.field NOT IN ("id_1", "id_2")
//              ORDER BY delta DESC, total DESC""").show()