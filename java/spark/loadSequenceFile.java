public static class ConvertToNativeTypes implements PairFunction<Tuple2<Text, IntWritable>, String, Integer> {
    public Tuple2<String, Integer> call(Tuple2<Text, IntWritable> record) {
        return new Tuple2(record._1.toString(), record._2.get()); 
    }
}

JavaPairRDD<Text, IntWritable> input = sc.sequenceFile(fileName, Text.class, IntWritable.class);

JavaPairRDD<String, Integer> result = input.mapToPair( new ConvertToNativeTypes());
