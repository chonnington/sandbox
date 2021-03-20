
val data = sc.sequenceFile(inFile, classOf[Text], classOf[IntWritable]).
    map{case (x, y) => (x.toString, y.get())}

// save sequence file

val data = sc.parallelize(List(("Panda", 3), ("Kay", 6), ("Snail", 2))) 

data.saveAsSequenceFile(outputFile)