import sys
import threading
import socket
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget,
    QLineEdit, QPushButton, QTextEdit, QInputDialog, QComboBox, QLabel
)


class ChatClient(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chat Client")
        self.setGeometry(100, 100, 600, 400)

        # Small pop up open
        self.username, ok = QInputDialog.getText(self, "Username", "Enter your username:")
        if not ok or not self.username:
            sys.exit()

        # Connect to server
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect(('127.0.0.1', 12345))
            self.client_socket.send(self.username.encode())
        except:
            sys.exit()

        main_layout = QHBoxLayout()
        left_layout = QVBoxLayout()

        self.user_label = QLabel(f"You are : {self.username}")
        left_layout.addWidget(self.user_label)

        self.chat_box = QTextEdit()
        self.chat_box.setReadOnly(True)
        left_layout.addWidget(self.chat_box)

        """ input_layout ( made a horizontal row with combo +text + button )"""
        input_layout = QHBoxLayout()
        self.recipient_box = QComboBox()
        input_layout.addWidget(self.recipient_box)

        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Type a message ----")
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

        threading.Thread(target=self.receive_messages, daemon=True).start()
        
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

    def send_message(self):
        message = self.input_box.text() # What user type it will take
        recipient = self.recipient_box.currentText() # In the drop down it will select the person
        if message and recipient:
            self.client_socket.send(f"{recipient}|{message}".encode())
            self.input_box.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    client = ChatClient()
    client.show()
    sys.exit(app.exec_())
    