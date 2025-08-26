import sys
import pika
import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit

class ProducerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RabbitMQ Producer")
        self.setGeometry(100, 100, 400, 300)

        # RabbitMQ setup
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='chat')

        # UI setup
        layout = QVBoxLayout()
        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)
        layout.addWidget(self.output_box)

        self.input_box = QLineEdit()
        layout.addWidget(self.input_box)

        self.send_btn = QPushButton("Send Message")
        self.send_btn.clicked.connect(self.send_message)
        layout.addWidget(self.send_btn)

        self.setLayout(layout)

    def send_message(self):
        message = self.input_box.text()
        if message:
            self.channel.basic_publish(exchange='', routing_key='chat', body=message.encode())
            self.output_box.append(f"✅ Sent: {message}")
            self.input_box.clear()
            time.sleep(1)  # simulate producer delay

    def closeEvent(self, event):
        self.connection.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    producer = ProducerApp()
    producer.show()
    sys.exit(app.exec_())
