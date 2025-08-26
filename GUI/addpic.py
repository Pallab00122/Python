import sys
from PyQt5.QtWidgets import QApplication,QLabel,QMainWindow,QWidget
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI Window ")
        self.setGeometry(700,300,500,500)

        label=QLabel(self)
        label.setGeometry(0,0,500,500)
        label.setScaledContents(True)

        pixmap=QPixmap("pic.jpg")
        label.setPixmap(pixmap)

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


# One example of chat app

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit

# class ChatApp(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         # Set the window properties (title and initial size)
#         self.setWindowTitle("Chat Application")
#         self.setGeometry(100, 100, 400, 300)  # (x, y, width, height)

#         # Create a central widget for the main window
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)

#         # Create a QVBoxLayout to arrange the widgets
#         layout = QVBoxLayout()

#         # Create a QLabel widget to display chat messages
#         self.chat_label = QLabel()
#         self.chat_label.setWordWrap(True)  # Wrap long messages
#         layout.addWidget(self.chat_label)

#         # Create a QLineEdit for typing new messages
#         self.message_input = QLineEdit()
#         self.message_input.setPlaceholderText("Type your message here...and press Enter key.")
#         self.message_input.returnPressed.connect(self.send_message)
#         layout.addWidget(self.message_input)

#         # Set the layout for the central widget
#         central_widget.setLayout(layout)

#         # Initialize chat history
#         self.chat_history = []

#     def send_message(self):
#         # Get the message from the input field
#         message = self.message_input.text()

#         # Append the message to the chat history
#         self.chat_history.append(message)

#         # Update the chat display
#         self.update_chat_display()

#         # Clear the input field
#         self.message_input.clear()

#     def update_chat_display(self):
#         # Display the chat history in the QLabel
#         chat_text = "\n".join(self.chat_history)
#         self.chat_label.setText(chat_text)

# def main():
#     app = QApplication(sys.argv)
#     window = ChatApp()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == "__main__":
#     main()
