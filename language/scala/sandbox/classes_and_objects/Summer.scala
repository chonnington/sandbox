// In file Summer.scala
import ChecksumAccumulator.calculate

object Summer {
    def main(args: Array[String]) = {
        for (arg <- args)
            println(arg + ": " + calculate(arg))
    } 
}

// to get it to run: 
// scalac ChecksumAccumulator.scala Summer.scala
// scala Summer of love