

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"#MainWindow {\n"
"    background-image: url(\"C:/Users/albin/OneDrive/Desktop/resource.qrc/rks.jpg\");\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"\n"
"\n"
"#widget {\n"
"    background-color: #fff;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: rgb(94, 94, 255);\n"
"\n"
"}\n"
"\n"
"QLineEdit {\n"
"color:black;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 1px solid rgb(0, 170, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget {\n"
"  background-color:white;\n"
"}")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(190, 80, 441, 371))
        self.widget.setSizeIncrement(QSize(300, 400))
        self.widget.setStyleSheet(u"#widget {\n"
"    color: rgb(0, 0, 255);\n"
"    background-color: #f0f0f0;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"\n"
"    "
"}\n"
"")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 20, 81, 31))
        font = QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 90, 81, 16))
        font1 = QFont()
        font1.setPointSize(11)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 160, 71, 16))
        self.label_3.setFont(font1)
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(60, 110, 321, 31))
        font2 = QFont()
        font2.setPointSize(10)
        self.lineEdit.setFont(font2)
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_2.setGeometry(QRect(60, 180, 321, 31))
        self.lineEdit_2.setFont(font2)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 260, 322, 31))
        self.pushButton.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, 220, 141, 20))
        self.label_4.setFont(font2)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(250, 220, 49, 21))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"")
        self.label_5.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 30, 81, 91))
        self.label_6.setStyleSheet(u"#label_6 {\n"
"background-image: url(\"C:/Users/albin/OneDrive/Desktop/resource.qrc/logo_1.png\");\n"
" background-repeat: no-repeat;\n"
"   \n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Don't have an account?", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<a href=\"#\" style=\"color:  rgb(0, 85, 255); text-decoration: underline;\">Register</a>\n"
"", None))
        self.label_6.setText("")
    # retranslateUi

