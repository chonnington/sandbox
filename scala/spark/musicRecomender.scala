
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

//////////////////////////////////////////////////////////////////////////////////

import org.apache.spark.sql._
import org.apache.spark.broadcast._

def buildCounts(
    rawUserArtistData: Dataset[String],
    bArtistAlias: Broadcast[Map[Int,Int]]): DataFrame = {
        rawUserArtistData.map { line =>
                val Array(userID, artistID, count) = line.split(' ').map(_.toInt) 
                val finalArtistID = bArtistAlias.value.getOrElse(artistID, artistID)
                (userID, finalArtistID, count)
            }.toDF("user", "artist", "count")
            }

val bArtistAlias = spark.sparkContext.broadcast(artistAlias)
val trainData = buildCounts(rawUserArtistData, bArtistAlias)
trainData.cache()

//////////////////////////////////////////////////////////////////////////////////