import pika
from .recieve import recieve
import json


def send_msg(message):

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='schedule_queue')

    channel.basic_publish(exchange='', routing_key='schedule_queue', body=json.dumps(message))
    print(" [x] Sent msg")
    connection.close()
    recieve()

