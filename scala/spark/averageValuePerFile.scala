
val input = sc.wholeTextFiles("file://home/holden/salesFiles") 

val result = input.mapValues { y =>
    val nums = y.split(" ").map(x => x.toDouble)
    nums.sum / nums.size.toDouble
}