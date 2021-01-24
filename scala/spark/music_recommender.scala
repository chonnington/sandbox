

val rawUserArtistData = spark.read.textFile("hdfs:///user/ds/user_artist_data.txt")

rawUserArtistData.take(5).foreach(println)

val userArtistDF = rawUserArtistData.map { line => 
    val Array(user, artist, _*) = line.split(' ') 
    (user.toInt, artist.toInt)
}.toDF("user", "artist")

userArtistDF.agg(min("user"), max("user"), min("artist"), max("artist")).show()