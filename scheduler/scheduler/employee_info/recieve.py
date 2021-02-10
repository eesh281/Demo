import pika, sys, os

def recieve():
    # import ipdb; ipdb.set_trace()
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='schedule_queue')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body) 
        #this body var is the msg    

    channel.basic_consume(queue='schedule_queue', on_message_callback=callback, auto_ack=True)
    # do whatever you want to do with msg
    print(' [*] Waiting for messages. To exit press CTRL+C')
    data = channel.start_consuming()
    print(data)

    return data
    

# if __name__ == '__main__':
#     try:
#         main()
#     except KeyboardInterrupt:
#         print('Interrupted')
#         try:
#             sys.exit(0)
#         except SystemExit:
#             os._exit(0)