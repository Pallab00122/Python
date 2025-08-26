import sys
import pika
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit

class Consumer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RabbitMq Consumer--")
        self.setGeometry(600,100,400,300)

        layout=QVBoxLayout()
        self.chat_box=QTextEdit()
        self.chat_box.setReadOnly(True)
        layout.addWidget(self.chat_box)

        self.setLayout(layout)

    def start_consuming(self):
        connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel=connection.channel()
        channel.queue_declare(queue='chat')

        def callback(ch,method,properties,body):
            message=body.decode()
            self.chat_box.append(f"Received : {message}")

        channel.basic_consume(queue='chat', on_message_callback=callback ,auto_ack=True)
        channel.start_consuming()

if __name__ == "__main__":
    app=QApplication(sys.argv)
    con=Consumer()
    con.show()
    sys.exit(app.exec_())