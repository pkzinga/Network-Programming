import sys
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QLineEdit,QLabel,QPushButton,QHBoxLayout
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtCore import Qt,QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from pathlib import Path


Path_Icon =  Path(__file__).parent / "kuthu.jpg"

class Webrowser(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kuthu Search Browser")
        self.setWindowIcon(QIcon(QPixmap(str(Path_Icon))))
        self.setGeometry(200,200,1000,700)



        self.layout = QVBoxLayout()
        self.setLayout(self.layout)






def main():
    app = QApplication(sys.argv)
    sys.exit(app.exec_())

if __name__ == "__main_-":
    main()
