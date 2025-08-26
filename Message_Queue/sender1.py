import pika

connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()

# Create queue (chat)
channel.queue_declare(queue='chat')

while True:
    msg=input("You : ")
    if msg.lower() == 'exit':
        break
    channel.basic_publish(exchange='', routing_key='chat', body=msg)

connection.close()
