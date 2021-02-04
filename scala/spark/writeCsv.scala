
pandaLovers.map(person => List(person.name, person.favoriteAnimal).toArray).mapPartitions { people =>
    val stringWriter = new StringWriter();
    val csvWriter = new CSVWriter(stringWriter); 
    csvWriter.writeAll(people.toList) 
    Iterator(stringWriter.toString)
}.saveAsTextFile(outFile)