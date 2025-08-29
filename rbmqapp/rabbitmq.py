import pika

def publish_message(message):
    params = pika.URLParameters("amqps://bvbfmndz:mg0thl9d08gagtu2oQSwIU7JDRXQjsPL@rabbit.lmq.cloudamqp.com/bvbfmndz")
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue="my_queue")
    channel.basic_publish(
        exchange="",
        routing_key="my_queue",
        body=message,
    )

    channel.close()