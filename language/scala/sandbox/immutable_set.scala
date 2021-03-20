// Approach #1

var jetSet = Set("Boeing", "Airbus")
jetSet += "Lear"
println(jetSet.contains("Cessna"))

// Approach #2

import scala.collection.mutable
val movieSet = mutable.Set("Hitch", "Poltergeist")
movieSet += "Shrek"
println(movieSet)

// Approach #3

import scala.collection.immutable.HashSet
val hashSet = HashSet("Tomatoes", "Chilies")
println(hashSet + "Coriander")

// Approach #4

import scala.collection.mutable
val treasureMap = mutable.Map[Int, String]()
treasureMap += (1 -> "Go to island.")
treasureMap += (2 -> "Find big X on ground.")
treasureMap += (3 -> "Dig.")
println(treasureMap(2))


// Approach #5

val romanNumeral = Map(
    1 -> "I", 
    2 -> "II", 
    3 -> "III", 
    4 -> "IV", 
    5 -> "V")
println(romanNumeral(4))