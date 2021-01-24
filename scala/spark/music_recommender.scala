
val rawUserArtistData = spark.read.textFile("hdfs:///user/ds/user_artist_data.txt")

rawUserArtistData.take(5).foreach(println)

val userArtistDF = rawUserArtistData.map { line => 
    val Array(user, artist, _*) = line.split(' ') 
    (user.toInt, artist.toInt)
}.toDF("user", "artist")

userArtistDF.agg(min("user"), max("user"), min("artist"), max("artist")).show()

val artistByID = rawArtistData.flatMap { line => 
    val (id, name) = line.span(_ != '\t')
    if (name.isEmpty) {
        None
    } else { 
        try {
            Some((id.toInt, name.trim)) 
        } catch {
            case _: NumberFormatException => None 
        }
    }
}.toDF("id", "name")

val rawArtistAlias = spark.read.textFile("hdfs:///user/ds/artist_alias.txt") 

val artistAlias = rawArtistAlias.flatMap { line =>
    val Array(artist, alias) = line.split('\t') 
    if (artist.isEmpty) {
        None
    } else {
        Some((artist.toInt, alias.toInt))
    }
}.collect().toMap