case class Person(id: Long, name: String, cityId: Long)

case class City(id: Long, name: String)

val family = Seq(
  Person(0, "Agata", 0),
  Person(1, "Iweta", 0),
  Person(2, "Patryk", 2),
  Person(3, "Maksym", 0)).toDS

val cities = Seq(
  City(0, "Warsaw"),
  City(1, "Washington"),
  City(2, "Sopot")).toDS

val joined = family.joinWith(cities, family("cityId") === cities("id"))

joined.printSchema

joined.show