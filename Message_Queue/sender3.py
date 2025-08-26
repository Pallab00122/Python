import pika
import time
# from pika.exchange_type import ExchangeType

connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()

channel.exchange_declare(exchange='pubsub',exchange_type='fanout')

print("Sender started. Type messages to broadcast .\n")

while True:
    message = input("Enter message: ")
    if message.lower() == "exit":
        print("Sender Exit")
        break

    channel.basic_publish(exchange='pubsub', routing_key='',body=message.encode())
    print(f"Sent : {message}")

    time.sleep(3)

connection.close()