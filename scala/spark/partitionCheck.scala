import org.apache.spark.HashPartitioner

val pairs = sc.parallelize(List((1, 1), (2, 2), (3, 3)))

pairs.partitioner

val partitioned = pairs.partitionBy(new HashPartitioner(2))

partitioned.partitioner