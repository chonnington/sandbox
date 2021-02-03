class DomainNamePartitioner(numParts: Int) extends Partitioner { 

    override def numPartitions: Int = numParts

    override def getPartition(key: Any): Int = {
        val domain = new Java.net.URL(key.toString).getHost() 
        val code = (domain.hashCode % numPartitions) 
        if (code < 0) {
            code + numPartitions // Make it non-negative 
        } else {
            code
        } 
    }

    // Java equals method to let Spark compare our Partitioner objects
    override def equals(other: Any): Boolean = other match { 
        case dnp: DomainNamePartitioner =>
            dnp.numPartitions == numPartitions 
        case _ =>
            false
    } 
}