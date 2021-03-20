val input = sc.hadoopFile[Text, Text, KeyValueTextInputFormat](inputFile).map { 
    case (x, y) => (x.toString, y.toString)
}