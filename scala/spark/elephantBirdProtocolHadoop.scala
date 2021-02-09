val job = new Job()
val conf = job.getConfiguration LzoProtobufBlockOutputFormat.setClassConf(classOf[Places.Venue], conf); 
val dnaLounge = Places.Venue.newBuilder()

dnaLounge.setId(1);
dnaLounge.setName("DNA Lounge") 
dnaLounge.setType(Places.Venue.VenueType.CLUB)

val data = sc.parallelize(List(dnaLounge.build()))
val outputData = data.map { pb =>
    val protoWritable = ProtobufWritable.newInstance(classOf[Places.Venue]); 
    protoWritable.set(pb)
    (null, protoWritable)
}

outputData.saveAsNewAPIHadoopFile(outputFile, 
    classOf[Text],
    classOf[ProtobufWritable[Places.Venue]], 
    classOf[LzoProtobufBlockOutputFormat[ProtobufWritable[Places.Venue]]], conf)