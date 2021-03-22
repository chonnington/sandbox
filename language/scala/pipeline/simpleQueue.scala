import java.util.Properties
import akka.actor.{ActorRef, ActorSystem, Props}
import org.apache.kafka.clients.consumer.KafkaConsumer
import scala.collection.JavaConversions._

object SimpleActorPipeline extends App {

    // Akka Steam actor setup and creation
    val system = ActorSystem("SimpleActorPipeline")
    val simpleActor = system.actorOf(Props[SimpleActor], "SimpleActor")
    val POLL_TIME = 100 // time in ms

    // Props for Kafka Consumer
    val props = new Properties()
    props.put("bootstrap.servers", "localhost:9092")
    props.put("group.id", "simple-actor-consumer")
    props.put("enable.auto.commit", "true")
    props.put("auto.commit.interval.ms", "1000")
    props.put("session.timeout.ms", "30000")
    props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer")
    props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer")

    val consumer = new KafkaConsumer[String, String](props)
    consumer.subscribe(List("simple-actor-pipeline")) // Kafka-Consumer reading from the topic

    println("simple-actor data-pipeline starting...")
    while (true) {
        val records = consumer.poll(POLL_TIME)
        for (record <- records) { 
            simpleActor.tell(SimpleMessage(record.value), ActorRef.noSender)
        }
    }
}