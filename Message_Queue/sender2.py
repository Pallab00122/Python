import pika
import time

connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()

channel.queue_declare(queue='chat')

print("Sender started ")

while True:
    message=input("Enter message :")
    if message.lower() == exit:
        print("Sender Exit")
        break

    channel.basic_publish(exchange='',routing_key='chat',body=message.encode())
    print(f"Sent: {message}")
    time.sleep(3)

connection.close()
