import sys
import pika
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit

class ConsumerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RabbitMQ Consumer")
        self.setGeometry(600, 100, 400, 300)

        # UI setup
        layout = QVBoxLayout()
        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)
        layout.addWidget(self.output_box)
        self.setLayout(layout)

        # RabbitMQ in a background thread
        self.thread = threading.Thread(target=self.start_consuming, daemon=True)
        self.thread.start()

    def start_consuming(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='chat')

        def callback(ch, method, properties, body):
            message = body.decode()
            self.output_box.append(f"📩 Received: {message}")

        channel.basic_consume(queue='chat', on_message_callback=callback, auto_ack=True)
        channel.start_consuming()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    consumer = ConsumerApp()
    consumer.show()
    sys.exit(app.exec_())

