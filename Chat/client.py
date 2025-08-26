import sys
import socket
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QTextEdit

class ChatClient(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chat Client ")
        self.setGeometry(100, 100, 400, 300)

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('127.0.0.1', 12345))

        self.layout = QVBoxLayout()

        self.chat_box = QTextEdit()
        self.chat_box.setReadOnly(True)
        self.layout.addWidget(self.chat_box)

        self.label = QLabel("Type your message:")
        self.layout.addWidget(self.label)

        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Enter message here")
        self.input_box.returnPressed.connect(self.send_message)
        self.layout.addWidget(self.input_box)

        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)
        self.layout.addWidget(self.send_button)

        self.setLayout(self.layout)

        self.receiver_thread = threading.Thread(target=self.receive_messages, daemon=True)
        self.receiver_thread.start()

    def send_message(self):
        message = self.input_box.text()
        if message:
            self.client_socket.send(message.encode())
            self.chat_box.append(f"You: {message}")
            self.input_box.clear()

    def receive_messages(self):
        while True:
            try:
                data = self.client_socket.recv(1024).decode()
                if data:
                    self.chat_box.append(f"Server: {data}")
            except:
                break

if __name__ == "__main__":
    app = QApplication(sys.argv)
    client_window = ChatClient()
    client_window.show()
    sys.exit(app.exec_())

