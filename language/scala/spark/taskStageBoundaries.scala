

def simpleSparkProgram(rdd : RDD[Double]): Long = { 
    rdd.filter(_< 1000.0) //stage1
       .map(x => (x, x))
       .groupByKey() //stage2
       .map{ case(value, groups) => (groups.sum, value)} //stage 3
       .sortByKey() //stage 3
       .count() //stage 3
}