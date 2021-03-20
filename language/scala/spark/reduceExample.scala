// reduce numbers 1 to 10 by adding them up
val x = sc.parallelize(1 to 10, 2)
val y = x.reduce((accum,n) => (accum + n)) 
// y: Int = 55
 
// shorter syntax
val y = x.reduce(_ + _) 
// y: Int = 55
 
// same thing for multiplication
val y = x.reduce(_ * _) 
// y: Int = 3628800