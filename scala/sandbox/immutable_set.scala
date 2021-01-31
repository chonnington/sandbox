
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