var z = Array("Zara", "Nuha", "Ayan")

// imperative

// Unit is a subtype of scala.AnyVal. Akin to Java void

def printArgs(args: Array[String]): Unit = {
    var i = 0
    while (i < args.length) {
        println(args(i))
        i += 1 
    }
}

// functional 

def printArgs(args: Array[String]): Unit = {
    for (arg <- args)
        println(arg)
}

def printArgs(args: Array[String]): Unit = {
    args.foreach(println)
}