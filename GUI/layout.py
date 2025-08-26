import sys
from PyQt5.QtWidgets import (QApplication,QLabel,QMainWindow,
                             QWidget,QVBoxLayout,QHBoxLayout,QGridLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Example layout colored labels
        level1 = QLabel("Label 1", self)
        level1.setStyleSheet("background-color:green;")
        
        level2 = QLabel("Label 2", self)
        level2.setStyleSheet("background-color:red;")
        
        level3 = QLabel("Label 3", self)
        level3.setStyleSheet("background-color:blue;")
        
        vBox = QHBoxLayout()
        vBox.addWidget(level1)
        vBox.addWidget(level2)
        vBox.addWidget(level3)
        central_widget.setLayout(vBox)

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()