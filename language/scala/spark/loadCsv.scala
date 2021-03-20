case class Person(name: String, favoriteAnimal: String)

val input = sc.wholeTextFiles(inputFile) 

val result = input.flatMap { case (_, txt) =>
    val reader = new CSVReader(new StringReader(txt));
    reader.readAll().map(x => Person(x(0), x(1))) 
}