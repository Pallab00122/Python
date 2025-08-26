import pika
import time
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit

class Producer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RabbitMQ Producer--")
        self.setGeometry(100,100,400,300)

        self.connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel=self.connection.channel()
        self.channel.queue_declare(queue='chat')

        layout=QVBoxLayout()
        self.chat_box=QTextEdit()
        self.chat_box.setReadOnly(True)
        layout.addWidget(self.chat_box)

        self.input_box=QLineEdit()
        layout.addWidget(self.input_box)

        self.send_btn=QPushButton("Send Message")
        self.send_btn.clicked.connect(self.send_message)
        layout.addWidget(self.send_btn)

        self.setLayout(layout)

    def send_message(self):
        message=self.input_box.text()
        if message:
            self.channel.basic_publish(exchange='',routing_key='chat',body=message.encode())
            self.chat_box.append(f"Sent : {message}")
            self.input_box.clear()
            time.sleep(2)

    def closeEvent(self, a0):
        return super().closeEvent(a0)

if __name__ == "__main__":
    app=QApplication(sys.argv)
    pro=Producer()
    pro.show()
    sys.exit(app.exec_())    