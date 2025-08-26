import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow,
                             QWidget, QPushButton)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.initUI()

    def initUI(self):
        self.button = QPushButton("Click me!", self)
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size:30px")
        self.button.clicked.connect(self.on_Click)

        self.label = QLabel("Hello", self)
        self.label.setGeometry(200, 100, 100, 50)
        self.label.setStyleSheet("font-size:20px")

    def on_Click(self):
        self.button.setText("Clicked")
        self.label.setText("Goodbye")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
