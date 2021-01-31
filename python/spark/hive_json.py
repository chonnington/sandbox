

from pyspark.sql import HiveContext
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("My App")
sc = SparkContext(conf = conf)

hiveCtx = HiveContext(sc)

hiveCtx.hql("CREATE TABLE IF NOT EXISTS src (key INT, value STRING)")
hiveCtx.hql("LOAD DATA LOCAL INPATH 'examples/src/main/resources/kv1.txt' INTO TABLE src")

# Queries can be expressed in HiveQL.
results = hiveCtx.hql("FROM src SELECT key, value").collect()

'''
{
{"user": {"name": "Holden", "location": "San Francisco"}, "text": "Nice day out today"}
{"user": {"name": "Matei", "location": "Berkeley"}, "text": "Even nicer here :)"}
}
'''

tweets = spark.read.json("json/ex.json", multiLine=True)
tweets.take(2)
tweets.registerTempTable("tweets")
results = hiveCtx.sql("SELECT users.user.location, users.user.name FROM tweets")