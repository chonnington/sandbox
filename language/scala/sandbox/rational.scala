class Rational(n: Int, d: Int) {
    println("Created " + n + "/" + d)
}

// scala> new Rational(1, 2)
// Created 1/2
// res0: Rational = Rational@2591e0c9

class Rational(n: Int, d: Int) {
    override def toString = n + "/" + d
}

// scala> val x = new Rational(1, 3)
// x: Rational = 1/3
// scala> val y = new Rational(5, 7)
// y: Rational = 5/7