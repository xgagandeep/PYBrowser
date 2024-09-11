import sys
from PyQt5.QtWidgets import QApplication, QWidget , QPushButton, QMessageBox, QMainWindow , QAction , QVBoxLayout, QTabWidget, QHBoxLayout,QLabel , QToolButton,QTabBar ,QLineEdit , QGridLayout,QDialog
from PyQt5 import QtCore , QtGui
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import sys
import PyQt5
from PyQt5.QtGui import QIcon,QPixmap
from datetime import datetime as dt

class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.top = -1
        self.left = 0
        self.height = 300
        self.width = 500

        self.createWindow()


    def createWindow(self):
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.setWindowTitle("Browser")
        w = self.size()

        button = QPushButton('PyQt5 button', self)
        button.move(100,70)
        button.clicked.connect(QApplication.instance().quit)

        self.button = QPushButton('', self)
        #button.move(100,70)
        self.button.clicked.connect(QApplication.instance().quit)
        #self.tabs.setCornerWidget(self.button)
        self.button1 = QPushButton('', self)
        self.button2 = QPushButton('', self)
        self.button.setIcon(QIcon(QPixmap("close-window.png")))
        self.button.setStyleSheet(
                        ":hover{background-color:red;color:white;border:0;}"
                        "QPushButton{background-color: transparent;width:40px;height:29px; margin:0;}"


                        )
        #button.move(100,70)
        self.button1.clicked.connect(self.btn_min_clicked)
        self.button2.clicked.connect(self.btn_max_clicked)
        self.button1.setStyleSheet(
                        ":hover{background-color:#00596b;}"
                        "QPushButton{background-image:url('minimize.png');background-color: transparent;border-left-style: none;border-top-style: none;border-bottom-style: none;width:40px;height:29px!important}"


                        )

        self.button2.setStyleSheet(
                        ":hover{background-color:#00596b;}"
                        "QPushButton{background-image:url('mid-button.png');background-color: transparent;border-left-style: none;border-top-style: none;border-bottom-style: none;width:40px;height:29px!important; margin:0!important;}"


                        )

        self.cornerwidget = QWidget(self)
        self.layout1 = QHBoxLayout(self.cornerwidget)
        self.layout1.addWidget(self.button1)
        self.layout1.addWidget(self.button2)
        self.layout1.addWidget(self.button)
        self.layout1.setSpacing(0)
        self.cornerwidget.setStyleSheet(
                        "background-color: #004551;"

                        )
        self.layout1.setContentsMargins(0,0,0,0);
        self.maxNormal=False
        self.Normal=False
        self.table_widget = MyTableWidget(self,self.cornerwidget)
        self.setCentralWidget(self.table_widget)
        self.table_widget.tabs.tabBarDoubleClicked.connect( self.btn_max_clicked )

        self.table_widget.tabs.setDocumentMode(True)
        # self.table_widget.tabs.tabBarClicked.connect(self.mousePress)


        #self.centralWidget().setContentsMargins(0,0,0,0);
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.show()


    def mousePressEvent(self, event):

         self.Normal = False
         self.offset = event.pos()

    def mouseReleaseEvent(self, event):
        x=event.globalX()
        y=event.globalY()

        x_w = self.offset.x()
        y_w = self.offset.y()
        if y_w<10:
            print(wi)
            print(x)

            if y<2:
                if self.Normal == False:

                    self.btn_max_clicked();

                    print(self.maxNormal)


    def mouseMoveEvent(self,event):
        # if event.button() == Qt.LeftButton:

        x=event.globalX()
        y=event.globalY()

        x_w = self.offset.x()
        y_w = self.offset.y()
        if y_w<10:
            print(wi)
            print(x)
            self.move(x-x_w, y-y_w)

            if x<10:
                self.move(0,-7)
                self.btn_half_clicked();

                print(self.maxNormal)

            elif x > (wi-10):
                self.move(wi/2,-7)
                self.btn_half_clicked();

                print(self.maxNormal)





    def btn_half_clicked(self):
        print("half_clicked")

        self.maxNormal= False


        self.resize(wi/2,h)



    def btn_max_clicked(self):
        print("max_clicked")
        print(self.maxNormal)

        if(self.isMaximized()):
            print(self.maxNormal)
            self.showNormal()
            self.maxNormal= False

        else:
            self.showMaximized()
            self.maxNormal=True

    def btn_min_clicked(self):
        self.showMinimized()







class MyTableWidget(QWidget):

    def __init__(self, parent,cornerwidget):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.history = {}
        # Initialize tab screen
        self.tabs = QTabWidget(movable=True, tabsClosable=True, tabShape=1)


        self.tabs.resize(0,500)

        # Add tabs


        self.tabs.tabCloseRequested.connect(self.remove_tab)
        #self.tabs.tabBarDoubleClicked.connect( self.new_tab )
        # Create first tab

        # Add tabs to widget
        self.layout.addWidget(self.tabs)

        self.layout.setContentsMargins(0,10,0,0);
        self.layout.setSpacing(0)
        self.url = 'http://google.com'

        self.gridLayout = QGridLayout()

        self.searchBar = QLineEdit()
        self.goback = QPushButton('B')
        self.goforward = QPushButton('F')
        self.reload = QPushButton('r')
        self.home = QPushButton('h')
        self.gridLayout.addWidget(self.goback,0,0)
        self.gridLayout.addWidget(self.goforward,0,1)
        self.gridLayout.addWidget(self.reload,0,2)
        self.gridLayout.addWidget(self.home,0,3)
        self.gridLayout.addWidget(self.searchBar,0,4)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0,5,5,4)
        self.layout.addLayout(self.gridLayout)
        #self.layout.addWidget(self.gridLayout)
        self.searchBar.setText(self.url)
        self.goback.clicked.connect(lambda: self.tabs.currentWidget().back())

        self.goforward.clicked.connect(lambda: self.tabs.currentWidget().forward())
        self.reload.clicked.connect(lambda: self.tabs.currentWidget().reload())
        self.searchBar.returnPressed.connect(self.loadpage)

        self.setLayout(self.layout)
        self.new_tab()



        self.goback.setStyleSheet(
                        ":hover{background-color:#00596b;}"
                        "QPushButton{background-color: #004551;border-left-style: none;border-top-style: none;border-bottom-style: none;width:40px;height:29px!important; margin:0!important;}"
                        )
        self.goforward.setStyleSheet(
                        ":hover{background-color:#00596b;}"
                        "QPushButton{background-color: #004551;border-left-style: none;border-top-style: none;border-bottom-style: none;width:40px;height:29px!important; margin:0!important;}"
                        )
        self.reload.setStyleSheet(
                        ":hover{background-color:#00596b;}"
                        "QPushButton{background-color: #004551;border-left-style: none;border-top-style: none;border-bottom-style: none;width:40px;height:29px!important; margin:0!important;}"
                        )
        self.home.setStyleSheet(
                        ":hover{background-color:#00596b;}"
                        "QPushButton{background-color: #004551;border-left-style: none;border-top-style: none;border-bottom-style: none;width:40px;height:29px!important; margin:0!important;}"
                        )










        self.addtabbutton = QPushButton("+")
        self.cn = QWidget()
        self.layout1 = QHBoxLayout(self.cn)
        self.layout1.addWidget(self.addtabbutton)
        self.addtabbutton.setStyleSheet(
                        ":hover{background-color:#00596b;color:white;}"
                        "QPushButton{background-color: transparent;width:40px;height:30px;padding-top:3px;border:1px solid black;border-top:none;}"


                        )
        self.layout1.setSpacing(0)
        self.cn.setStyleSheet(
                        "background-color: #004551;"

                        )
        self.layout1.setContentsMargins(0,0,0,0);
        self.addtabbutton.clicked.connect(self.new_tab)

        #self.tabs.tabBarDoubleClicked.connect( self.new_tab )

        self.tabs.setCornerWidget(cornerwidget)
        self.tabs.setCornerWidget(self.cn,corner=Qt.TopLeftCorner)
        self.tabs.currentChanged.connect(self.changeurl)


    def forward(self):

        self.view.page().triggerAction(QWebEnginePage.Forward)


    def back(self,browser=None):
        #self.view.page().action(QWebEnginePage.Back)

        self.view.page().triggerAction(QWebEnginePage.Back)
        print('forward enabled', self.view.page().action(QWebEnginePage.Forward).isEnabled())

    def changeurl(self):
        if self.tabs.currentWidget().url():
            qurl = self.tabs.currentWidget().url()
            self.searchBar.setText(qurl.toString())

        else:
            self.searchBar.setText("History")


    def mouseDoubleClickEvent(self, event):
        self.offset = event.pos()
        y_w = self.offset.y()
        if y_w<10:

            self.new_tab()

    def loadpage(self):
        if self.searchBar.text().lower() == "history":
            self.showHistory()
        else:
            self.url = QUrl(self.searchBar.text())
            if self.url.scheme() == "":

                self.url.setScheme("https")
            self.tabs.currentWidget().setUrl(self.url)
    def update_history(self):
        if self.tabs.currentWidget().url():
            qurl = self.tabs.currentWidget().url()
            x =dt.now()

            self.history[x.strftime("%c")] = qurl.toString()
        print(self.history)

    def showHistory(self):
         d = QDialog()
         vbox = QVBoxLayout()
         for h in self.history:
             h1 = QLabel()
             h1.setText(h+" -->"+self.history[h])
             vbox.addWidget(h1)
         d.setLayout(vbox)

         d.setWindowModality(Qt.ApplicationModal)
         d.exec_()

    def remove_tab(self,currentIndex):
        self.tabs.removeTab(currentIndex)


    def new_tab(self,z = 0):
            if z ==0 :
                self.view = QWebEngineView()
                self.defaulturl = 'http://google.com'
                self.view.load(PyQt5.QtCore.QUrl(self.defaulturl))

                i = self.tabs.addTab(self.view,"Google")
                self.view.urlChanged.connect( self.changeurl)
                self.view.loadFinished.connect(self.update_history)
                self.view.loadFinished.connect(lambda _, i=i, browser=self.view:
                                             self.tabs.setTabText(i, browser.page().title()))


            else:
                self.tab1 = QWidget()
                return self.tabs.addTab(self.tab1,"History")

if __name__ == "__main__":
    app =  QApplication(sys.argv)

    screen_resolution = app.desktop().availableGeometry()
    wi = screen_resolution.width()
    h = screen_resolution.height()
    #pp.setStyle('Breeze')

    app.setStyleSheet("QTabWidget::right-corner{top:-1px;} QTabWidget::pane { /* The tab widget frame */  }  QTabWidget::tab-bar{ /* move to the right by 5px */}/* Style the tab using the tab sub-control. Note that it reads QTabBar _not_ QTabWidget */QTabBar{ qproperty-drawBase: 0;background-color:#004551;}QTabBar::tab {background:#004551; color:white;font-size:12px;border:1px solid black;/* same as the pane color */height:25px;padding:2px; width:150px;}QTabBar::tab:hover {background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #fafafa, stop: 0.4 #f4f4f4, stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);}QTabBar::tab:selected {background-color:#00596b;/* same as pane color */}QTabBar::tab:!selected {/* make non-selected tabs look smaller */}QMainWindow{background-color:#00596b;}QTabBar::scroller{width:50px;}QTabBar::tab:top{margin-left:-1px;}QTabBar::tab:top:selected {border-bottom-color:#00596b;border-top-color:#00596b;}QLineEdit{height:25px; padding-left:20px;padding-right:20px;}QTabBar::close-button{background-image:url('closetab.png');background-position:0px 0px;margin-top:-2px;}QTabBar::close-button:!selected{background-image:url('closetabnotselected.png');}")#bf0b62
    window = window()

    sys.exit(app.exec_())
