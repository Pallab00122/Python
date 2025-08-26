import sys
import socket
import threading
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget,
    QLineEdit, QPushButton, QTextEdit, QInputDialog, QComboBox, QLabel
)


class ChatClient(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chat Client - With Client List")
        self.setGeometry(100, 100, 600, 400)

        # Ask for username
        self.username, ok = QInputDialog.getText(
            self, "Username", "Enter your username:")
        if not ok or not self.username:
            sys.exit()

        # Connect to server
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect(('127.0.0.1', 12345))
            self.client_socket.send(self.username.encode())
        except:
            print("❌ Could not connect to server")
            sys.exit()

        # Main layout
        main_layout = QHBoxLayout()

        # LEFT: Chat area
        left_layout = QVBoxLayout()

        # Show your username
        self.user_label = QLabel(f"✅ You are: {self.username}")
        left_layout.addWidget(self.user_label)

        # Chat display
        self.chat_box = QTextEdit()
        self.chat_box.setReadOnly(True)
        left_layout.addWidget(self.chat_box)

        # Input layout
        input_layout = QHBoxLayout()
        self.recipient_box = QComboBox()
        input_layout.addWidget(self.recipient_box)

        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Type a message...")
        self.input_box.returnPressed.connect(self.send_message)
        input_layout.addWidget(self.input_box)

        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)
        input_layout.addWidget(self.send_button)

        left_layout.addLayout(input_layout)

        # RIGHT: Client list
        self.client_list_widget = QListWidget()
        self.client_list_widget.setFixedWidth(150)

        # Add layouts to main layout
        main_layout.addLayout(left_layout, stretch=3)
        main_layout.addWidget(self.client_list_widget, stretch=1)

        self.setLayout(main_layout)

        # Start receiver thread
        threading.Thread(target=self.receive_messages, daemon=True).start()

    def send_message(self):
        message = self.input_box.text()
        recipient = self.recipient_box.currentText()
        if message and recipient:
            try:
                self.client_socket.send(f"{recipient}|{message}".encode())
                self.input_box.clear()
            except:
                self.chat_box.append("❌ Failed to send message.")

    def receive_messages(self):
        while True:
            try:
                data = self.client_socket.recv(1024).decode()
                if data.startswith("USERLIST:"):
                    # Update dropdown and list widget
                    users = data[len("USERLIST:"):].split(",")
                    self.recipient_box.clear()
                    self.recipient_box.addItems(users)

                    self.client_list_widget.clear()
                    self.client_list_widget.addItems(users)
                else:
                    self.chat_box.append(data)
            except:
                break


if __name__ == "__main__":
    app = QApplication(sys.argv)
    client = ChatClient()
    client.show()
    sys.exit(app.exec_())
