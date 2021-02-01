// Initialization code; we load the user info from a Hadoop SequenceFile on HDFS.
// This distributes elements of userData by the HDFS block where they are found,
// and doesn't provide Spark with any way of knowing in which partition a
// particular UserID is located.

val sc = new SparkContext(...)

// inefficient
val userData = sc.sequenceFile[UserID, UserInfo]("hdfs://...").persist()

// efficient
val userData = sc.sequenceFile[UserID, UserInfo]("hdfs://...")
                 .partitionBy(new HashPartitioner(100)) // Create 100 partitions 
                 .persist()

/*

100 passed to partitionBy() represents the number of partitions, which will control how many parallel tasks per‐ 
form further operations on the RDD (e.g., joins); 
in general, make this at least as large as the number of cores in your cluster.

*/


// we assume that this is a SequenceFile containing (UserID, LinkInfo) pairs.
def processNewLogs(logFileName: String) {

    val events = sc.sequenceFile[UserID, LinkInfo](logFileName)

    val joined = userData.join(events)

    val offTopicVisits = joined.filter {
        case (userId, (userInfo, linkInfo)) => !userInfo.topics.contains(linkInfo.topic)
    }.count()

    println("Number of visits to non-subscribed topics: " + offTopicVisits)
}