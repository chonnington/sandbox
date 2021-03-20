class ChecksumAccumulator {
    var sum = 0
}

val acc = new ChecksumAccumulator
val csa = new ChecksumAccumulator

acc.sum = 3

class ChecksumAccumulator {
    private var sum = 0
}

val acc = new ChecksumAccumulator
acc.sum = 5 // Won't compile, because sum is private

class ChecksumAccumulator {

    private var sum = 0

    def add(b: Byte): Unit = {
        sum += b
    }

    def checksum(): Int = { 
        return ~(sum & 0xFF) + 1
    } 

}

// In file ChecksumAccumulator.scala
class ChecksumAccumulator {
    private var sum = 0
    def add(b: Byte): Unit = { sum += b } 
    def checksum(): Int = ~(sum & 0xFF) + 1
}