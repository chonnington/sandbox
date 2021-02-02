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