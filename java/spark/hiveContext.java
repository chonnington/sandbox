import org.apache.spark.sql.hive.HiveContext; 
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SchemaRDD;

HiveContext hiveCtx = new HiveContext(sc);
SchemaRDD rows = hiveCtx.sql("SELECT name, age FROM users");
Row firstRow = rows.first(); 
System.out.println(firstRow.getString(0)); // Field 0 is the name