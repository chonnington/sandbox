import scala.collection.mutable

// COMPANION CLASS & OBJECT

class ChecksumAccumulator {
    private var sum = 0
    def add(b: Byte): Unit = { sum += b } 
    def checksum(): Int = ~(sum & 0xFF) + 1
}

object ChecksumAccumulator {

    private val cache = mutable.Map.empty[String, Int]

    def calculate(s: String): Int =
        if (cache.contains(s))
            cache(s)
        else {
            val acc = new ChecksumAccumulator
            for (c <- s)
                acc.add(c.toByte)
                val cs = acc.checksum()
                cache += (s -> cs)
                cs
        } 
}

// ChecksumAccumulator.calculate("Every value is an object.")

/*

A singleton object is more than a holder of static methods, however. 
It is a first-class object. You can think of a singleton object’s name, 
therefore, as a “name tag” attached to the object:

*/