JavaDoubleRDD result = rdd.mapToDouble(new DoubleFunction < Integer > () {
    public double call(Integer x) {
        return (double) x * x;
    }
});

System.out.println(result.mean());