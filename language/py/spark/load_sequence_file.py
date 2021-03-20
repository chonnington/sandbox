
from pyspark import SparkContext

sc = SparkContext("local", "Simple App")

inFile = "foobar"

data = sc.sequenceFile(inFile,
                       "org.apache.hadoop.io.Text", 
                       "org.apache.hadoop.io.IntWritable")