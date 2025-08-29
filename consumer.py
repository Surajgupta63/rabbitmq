import pika

def callback(ch, method, properties, body):
    message = body.decode()
    print(message)

params = pika.URLParameters("amqps://bvbfmndz:mg0thl9d08gagtu2oQSwIU7JDRXQjsPL@rabbit.lmq.cloudamqp.com/bvbfmndz")
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue="my_queue")
channel.basic_consume(queue="my_queue", on_message_callback=callback, auto_ack=True)
print("consumer ready to consume RabbitMQ queue messages")

channel.start_consuming()