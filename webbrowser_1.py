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

        self.image =QLabel()
        pixmap = QPixmap(str(Path_Icon))
        self.image.setPixmap(pixmap)
        self.image.setAlignment(Qt.AlignCenter)
        self.image.setFixedSize(1000,100)
        self.image.raise_()

        self.search = QLineEdit()
        self.search.setPlaceholderText("search here or input url to connect to local server specify path as follows localhost:8088/")
        self.setGeometry(100,100,600,500)

        self.back_button = QPushButton("Go Back")
        self.back_button.clicked.connect(self.go_back)

        self.search_btn = QPushButton("Click Me to search")
        self.search_btn.clicked.connect(self.load_url)

        self.reload_btn = QPushButton("reload")
        self.reload_btn.clicked.connect(self.re_load)
        
        self.forward_button = QPushButton("Go Forward")
        self.forward_button.clicked.connect(self.go_forward)
        


        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.Search_layout = QHBoxLayout()
        self.Search_layout.addWidget(self.back_button)
        self.Search_layout.addWidget(self.forward_button)
        self.Search_layout.addWidget(self.search)
        self.Search_layout.addWidget(self.search_btn)
        self.Search_layout.addWidget(self.reload_btn)


        self.layout.addWidget(self.image)
        self.layout.addLayout(self.Search_layout)
    
        
        self.browser = QWebEngineView()
        self.layout.addWidget(self.browser)
       

    def re_load(self):
          self.browser.reload()

    def go_back(self):
            self.browser.back()

    def go_forward(self):
            self.browser.forward()

    def load_url(self):
            url = self.search.text()
            self.current_url = url            
            if not url:
                  return           
            if not url.startswith("http://") and not url.startswith("https://"):
                url = "http://" + url

            url_local = "http://localhost:8088/"

            if url in (f"{url_local}",f"{url_local}register"):
                self.browser.load(QUrl(url))
            else:
                self.error_html()

    def error_html(self):
            error = f"""
                    <html><body>
                    <h2>No local results for query "{self.current_url}"</h2>
                    <p><a href="https://www.google.com/search?q={self.current_url}">search on Google</a></p>
                    </body></html> """
            self.browser.setHtml(error)


def main():
    app = QApplication(sys.argv)
    browser = Webrowser()
    browser.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
