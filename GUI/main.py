import sys
from PyQt5.QtWidgets import QApplication,QLabel,QMainWindow,QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI Window ")
        self.setGeometry(700,300,500,500)

        label=QLabel("Hello",self)
        label.setFont(QFont("Arial",40))
        label.move(60, 15)
        label.setGeometry(0,0,500,100)
        label.setStyleSheet("color: yellow;"
                            "background-color:green;"
                            "font-weight: bold"
                            )
        label.setAlignment(Qt.AlignHCenter) #Center the text

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()