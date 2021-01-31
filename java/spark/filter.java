JavaRDD < String > inputRDD = sc.textFile("log.txt");
JavaRDD < String > errorsRDD = inputRDD.filter(
new Function < String, Boolean > () {
    public Boolean call(String x) {
        return x.contains("error");
    }
}
});