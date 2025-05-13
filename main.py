# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerGYMboG.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget, QFileDialog)
import sys
import hashlib

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(600, 400))
        MainWindow.setMaximumSize(QSize(600, 400))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(600, 400))
        self.centralwidget.setMaximumSize(QSize(601, 401))
        self.centralwidget.setStyleSheet(u"")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(70, 170, 351, 32))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(427, 170, 101, 34))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(67, 280, 100, 35))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(430, 280, 101, 35))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 350, 461, 18))
        self.label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 20, 260, 50))
        font = QFont()
        font.setFamilies([u"Noto Sans"])
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 130, 211, 31))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.label_3.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)

        


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"QUICK HASH", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Examine", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"MD5", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"SHA256", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"WAITING FOR FILE", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"QUICK HASH", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Your file to hash", None))
    # retranslateUi


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.open_file_dialog)
        self.ui.pushButton_2.clicked.connect(self.md5)
        self.ui.pushButton_3.clicked.connect(self.sha256)

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select a File")
        if file_path:
            self.ui.lineEdit.setText(file_path)
    def md5(self):
        file_path = self.ui.lineEdit.text()
        if file_path:
            md5_hash = hashlib.md5(open(file_path, "rb").read()).hexdigest()
            self.ui.label.setText(md5_hash)
            print(md5_hash)
    def sha256(self):
        file_path = self.ui.lineEdit.text()
        if file_path:
            sha256_hash = hashlib.sha256(open(file_path, "rb").read()).hexdigest()
            self.ui.label.setText(sha256_hash)
            print(sha256_hash)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())



    