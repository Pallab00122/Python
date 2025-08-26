import sys
import socket
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class ClientSide(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chat Client")
        self.setGeometry(100,100,400,150)

        # Create Socket
        self.client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client_socket.connect(('127.0.0.1', 12345))

        self.layout = QVBoxLayout()

        self.label=QLabel("Type your message")
        self.layout.addWidget(self.label)

        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Enter message here")
        self.input_box.returnPressed.connect(self.send_message)
        self.layout.addWidget(self.input_box)

        self.send_button=QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)
        self.layout.addWidget(self.send_button)

        self.setLayout(self.layout)


    def send_message(self):
        message=self.input_box.text()
        if message:
            self.client_socket.send(message.encode())
            self.input_box.clear()
        

if __name__ == "__main__":
    app=QApplication(sys.argv)
    client=ClientSide()
    client.show()
    sys.exit(app.exec_())