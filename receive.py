#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.URLParameters('amqp://guest:guest@amqp1-server:5672/%2F'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
