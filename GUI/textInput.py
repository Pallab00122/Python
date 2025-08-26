import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI Window ")
        self.setGeometry(700, 300, 500, 500)

        label = QLabel(self)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        # Create widgets to display the chat messages
        self.chat_label = QLabel()
        # Place this label inside the layout so it appears on the screen
        layout.addWidget(self.chat_label)

        self.message_input = QLineEdit()  #text input field
        self.message_input.setPlaceholderText("Type your message here...")
        self.message_input.returnPressed.connect(self.send_message)
        layout.addWidget(self.message_input)
        # returnPressed is a signal from QLineEdit ( when Enter is pressed).

        central_widget.setLayout(layout)

        self.chat_history = []

    def send_message(self):
        message = self.message_input.text()   # Get the message from the input field
        self.chat_history.append(message)
        self.update_chat_display()
        self.message_input.clear()

    def update_chat_display(self):
        message = "\n".join(self.chat_history)
        # displays the user's input on the screen.
        self.chat_label.setText(message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
