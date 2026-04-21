

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
        MainWindow.setStyleSheet(u"#centralwidget{\n"
"\n"
"  background-color:white;\n"
"\n"
"}\n"
"\n"
"QLabel {\n"
"color: black;\n"
"}\n"
"\n"
"QLineEdit {\n"
"color: black;\n"
"font-size: 12px; \n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 1px solid rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"\n"
"background-color: rgb(94, 94, 255);\n"
"\n"
"}\n"
"\n"
"#label_11 {\n"
"background-image: url(\"C:/Users/albin/OneDrive/Desktop/resource.qrc/logo_1.png\");\n"
" background-repeat: no-repeat;\n"
"}\n"
"   \n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(170, 40, 491, 481))
        self.widget.setStyleSheet(u"#widget {\n"
"    color: rgb(0, 0, 255);\n"
"    background-color: #f0f0f0;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"}")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 30, 201, 20))
        font = QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 160, 91, 16))
        font1 = QFont()
        font1.setPointSize(11)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 160, 81, 16))
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 160, 49, 16))
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 230, 49, 16))
        self.label_5.setFont(font1)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 300, 71, 16))
        self.label_6.setFont(font1)
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(270, 300, 71, 16))
        self.label_7.setFont(font1)
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(50, 90, 81, 16))
        self.label_8.setFont(font1)
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(50, 180, 171, 31))
        font2 = QFont()
        font2.setPointSize(10)
        self.lineEdit.setFont(font2)
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(270, 180, 171, 31))
        self.lineEdit_2.setFont(font2)
        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(50, 110, 391, 31))
        self.lineEdit_3.setFont(font2)
        self.lineEdit_4 = QLineEdit(self.widget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(50, 250, 391, 31))
        self.lineEdit_4.setFont(font2)
        self.lineEdit_5 = QLineEdit(self.widget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(50, 320, 171, 31))
        self.lineEdit_5.setFont(font2)
        self.lineEdit_6 = QLineEdit(self.widget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_6.setGeometry(QRect(270, 320, 171, 31))
        self.lineEdit_6.setFont(font2)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 380, 391, 31))
        self.pushButton.setFont(font1)
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(120, 420, 151, 21))
        self.label_9.setFont(font2)
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(270, 420, 49, 21))
        self.label_10.setFont(font2)
        self.label_10.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(50, 30, 81, 91))
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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Create an account", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"First Name:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Last Name:", None))
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Personal ID:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Already have an account?", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<a href=\"#\" style=\"color:  rgb(0, 85, 255); text-decoration: underline;\">Login</a>\n"
"", None))
        self.label_11.setText("")
    # retranslateUi

