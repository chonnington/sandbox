import sys
from random import random
from operator import add

from pyspark.sql.session import SparkSession
from pyspark.sql.functions import unix_timestamp, udf, hour, minute, from_unixtime


if __name__ == "__main__":

    output_file = sys.argv[1]
    spark = SparkSession.builder\
            .getOrCreate()

    for x in range(6,7):
        s3_location = "s3://region/dir/sdir/path/" + str(x).zfill(2) +".csv"
        time_format = "yyyy-MM-dd HH-mm-ss"

        df = spark.read.option("header","true")\
             .option("inferSchema","true")\
             .csv(s3_location)

        df1 = df[(df['pickup_latitude'] < 40.917577)\
                 & (df['pickup_latitude'] > 40.477399)\
                 & (df['pickup_longitude'] > -74.259090)\
                 & (df['pickup_longitude'] < -73.700272)]

        df2 = df1[(df1['dropoff_longitude'] < 0)\
              & (df1['dropoff_latitude'] > 0)\
              &(df1['pickup_longitude'] != df1['dropoff_longitude'])\
              & (df1['pickup_latitude'] != df1['dropoff_latitude'])]

        time_duration = unix_timestamp("tpep_dropoff_datetime",format = time_format)\
                      - unix_timestamp("tpep_pickup_datetime", format = time_format)
        df3 = df2.withColumn("time_duration",time_duration)\
                 .withColumn("hour",hour(df2.tpep_pickup_datetime))\
                 .withColumn("dayOfWeek",from_unixtime(unix_timestamp\
                            (df1.tpep_pickup_datetime,time_format),"uuuuu").cast("Integer"))

        df4 = df3[(df3['trip_distance'] < 500)\
                  & (df3['time_duration'] > 10)]

        df5 = df4[(df4['fare_amount'] > 0)\
                  & (df4['extra'] >= 0)\
                  & (df4['mta_tax'] >= 0)\
                  & (df4['tip_amount'] >= 0)\
                  & (df4['tolls_amount'] >= 0)\
                  & (df4['improvement_surcharge'] >= 0)\
                  & (df4['total_amount'] > 0)]

        df5.write.csv(output_file + "/2015/" + str(x).zfill(2) + ".csv")
