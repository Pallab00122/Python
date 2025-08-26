import pika

conn=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=conn.channel()

channel.queue_declare(queue='chat')

def callback(ch,method, properties, body):
    # print("Friend:", body.decode())
    print(f"received new message: ",body.decode())

channel.basic_consume(queue='chat', on_message_callback=callback, auto_ack=True)

print("Waiting for message")
channel.start_consuming()
