import pika
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

        

if __name__ == "__main__":
    app=QApplication(sys.argv)
    pro=Producer()
    pro.show()
    sys.exit(app.exec_())    