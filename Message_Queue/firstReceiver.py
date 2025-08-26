import pika
import sys
import time
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLabel

class ReceiveApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(" First")
        self.setGeometry(200,200,400,300)

        layout = QVBoxLayout()

        self.chat_box = QTextEdit()
        self.chat_box.setReadOnly(True)
        layout.addWidget(self.chat_box)

        self.setLayout(layout)

        threading.Thread(target=self.start_consumer, daemon=True).start()

    def display_message(self, msg):
        self.chat_box.append(f"Friend: {msg}")

    def start_consumer(self):
        def callback(ch,method,properties,body):
            # print(f" Firstconsumer received message :{body.decode()}")
            msg=body.decode()
            self.chat_box.append(f" Friend: {msg}")
    
        connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel=connection.channel()

        channel.exchange_declare(exchange='pubsub',exchange_type='fanout')
        # Create random name er temporary queue , true means only for this client 
        queue=channel.queue_declare(queue='' ,exclusive=True)

        channel.queue_bind(exchange='pubsub', queue=queue.method.queue)

        channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=callback)

        print(" Waiting for messages. ")
        channel.start_consuming()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReceiveApp()
    window.show()
    sys.exit(app.exec_())
