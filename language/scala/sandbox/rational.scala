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

class Rational(n: Int, d: Int) {
    require(d != 0)
    override def toString = n + "/" + d
}

class Rational(n: Int, d: Int) {

    require(d != 0)

    val numer: Int = n
    val denom: Int = d

    override def toString = numer + "/" + denom

    def add(that: Rational): Rational =
        new Rational(
            numer * that.denom + that.numer * denom,
            denom * that.denom
    )

    def lessThan(that: Rational) =
        this.numer * that.denom < that.numer * this.denom 

    def max(that: Rational) =
        if (this.lessThan(that)) that else this
}


// scala> val oneHalf = new Rational(1, 2)
// oneHalf: Rational = 1/2
// scala> val twoThirds = new Rational(2, 3)
// twoThirds: Rational = 2/3
// scala> oneHalf add twoThirds
// res2: Rational = 7/6