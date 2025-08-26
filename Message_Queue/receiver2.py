import sys
import pika
import queue
import time
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget

message_queue=queue.Queue() # A thread safe object , it uses locks to ensure that only one thread can access and modify the queue data

class chatWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Receiver Chat")
        self.setGeometry(100, 100, 400, 400)

        self.chat_box = QTextEdit(self)  # text area to display message
        self.chat_box.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.chat_box)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        threading.Thread(target=self.process_message,daemon=True).start() #GUI Thread: Continues to run the app.exec_() loop, keeping the window active and responsive to user input.

    def process_message(self):
        while True:
            message=message_queue.get()
            self.show_message(message)
            time.sleep(10)

    def show_message(self , message):
        self.chat_box.append(f"{message}")

def rabbitmq_consume():
    def callback(ch,method,properties,body):
        message_queue.put(body.decode())

    connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel=connection.channel()
    channel.queue_declare(queue='chat') #ensure the queue exists

    channel.basic_consume(queue='chat',on_message_callback=callback,auto_ack=True)
    print("Waiting for messages")
    channel.start_consuming()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = chatWindow()
    window.show()
    threading.Thread(target=rabbitmq_consume,daemon=True).start() #Background Thread: Runs the rabbitmq_consumer function to listen for messages without interfering with the GUI.
    sys.exit(app.exec_())
