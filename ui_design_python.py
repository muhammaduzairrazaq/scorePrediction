# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_design.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(935, 611)
        Form.setMinimumSize(QSize(935, 611))
        Form.setMaximumSize(QSize(935, 611))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 935, 611))
        self.label.setStyleSheet(u"background-image:url(:/newPrefix/frame.png);")
        self.label.setPixmap(QPixmap(u":/newPrefix/frame.png"))
        self.label.setScaledContents(True)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(62, 299, 159, 43))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"	color: white;\n"
"}\n"
"\n"
"QLineEdit::hover{\n"
"border: 2px solid rgba(115, 255, 138, 0.3);\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"")
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(262, 299, 159, 43))
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"	color: white;\n"
"}\n"
"\n"
"QLineEdit::hover{\n"
"border: 2px solid rgba(115, 255, 138, 0.3);\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"")
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(62, 361, 159, 43))
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"	color: white;\n"
"}\n"
"\n"
"QLineEdit::hover{\n"
"border: 2px solid rgba(115, 255, 138, 0.3);\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"")
        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(262, 361, 159, 43))
        self.lineEdit_4.setStyleSheet(u"QLineEdit {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"	color: white;\n"
"}\n"
"\n"
"QLineEdit::hover{\n"
"border: 2px solid rgba(115, 255, 138, 0.3);\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(62, 460, 359, 43))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"	color: white;\n"
"	font-size: 15px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgba(115, 255, 138, 0.3);\n"
"border-radius:10px;\n"
"border: 2px solid rgba(115, 255, 138, 0.3);\n"
"animation: pulse 1s infinite;\n"
"\n"
"}\n"
"")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(585, 156, 73, 50))
        self.label_2.setStyleSheet(u"QLabel{\n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QLabel::hover{\n"
"border: 2px solid rgba(210, 115, 255, 0.3);\n"
"\n"
"}")
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(777, 156, 73, 50))
        self.label_3.setStyleSheet(u"QLabel{\n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QLabel::hover{\n"
"border: 2px solid rgba(210, 115, 255, 0.3);\n"
"\n"
"}")
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(587, 305, 73, 50))
        self.label_4.setStyleSheet(u"QLabel{\n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QLabel::hover{\n"
"border: 2px solid rgba(210, 115, 255, 0.3);\n"
"\n"
"}")
        self.label_4.setScaledContents(True)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(779, 305, 73, 50))
        self.label_5.setStyleSheet(u"QLabel{\n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QLabel::hover{\n"
"border: 2px solid rgba(210, 115, 255, 0.3);\n"
"\n"
"}")
        self.label_5.setScaledContents(True)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(589, 453, 73, 50))
        self.label_6.setStyleSheet(u"QLabel{\n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QLabel::hover{\n"
"border: 2px solid rgba(210, 115, 255, 0.3);\n"
"\n"
"}")
        self.label_6.setScaledContents(True)
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(781, 453, 73, 50))
        self.label_7.setStyleSheet(u"QLabel{\n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QLabel::hover{\n"
"border: 2px solid rgba(210, 115, 255, 0.3);\n"
"\n"
"}")
        self.label_7.setScaledContents(True)
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(680, 218, 75, 31))
        self.label_8.setStyleSheet(u"QLabel{\n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"color: white;\n"
"qproperty-alignment: 'AlignCenter';\n"
"}\n"
"\n"
"QLabel::hover{\n"
"border: 2px solid rgba(210, 115, 255, 0.3);\n"
"\n"
"}")
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(682, 367, 75, 31))
        self.label_9.setStyleSheet(u"QLabel{\n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"color: white;\n"
"qproperty-alignment: 'AlignCenter';\n"
"}\n"
"\n"
"QLabel::hover{\n"
"border: 2px solid rgba(210, 115, 255, 0.3);\n"
"\n"
"}")
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(684, 515, 75, 31))
        self.label_10.setStyleSheet(u"QLabel{\n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"color: white;\n"
"qproperty-alignment: 'AlignCenter';\n"
"}\n"
"\n"
"QLabel::hover{\n"
"border: 2px solid rgba(210, 115, 255, 0.3);\n"
"\n"
"}")
        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(62, 175, 159, 43))
        self.comboBox.setStyleSheet(u"QComboBox {\n"
" 	background-color:transparent;\n"
"	border:none;\n"
"	color: white;\n"
"	font-size: 12px;\n"
"    padding: 3px; /* Set padding to adjust the text position */\n"
"    combobox-popup: 0; /* Remove the side scroll bar */\n"
"}\n"
"QComboBox::hover{\n"
"border: 2px solid rgba(115, 255, 138, 0.3);\n"
"border-radius: 10px; \n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	background-color: transparent;\n"
"   }\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgba(123, 255, 128, 0.76);\n"
"	color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox::down-arrow {\n"
"    image:url(:/newPrefix/arrow.png); /* Replace with the path to your downward arrow image */\n"
"    width: 35; /* Adjust the width of the arrow image */\n"
"    height: 35; /* Adjust the height of the arrow image */\n"
"    padding-right: 14px; /* Adjust the padding between the arrow and text */\n"
"    vertical-align: middle; /* Align the arrow vertically in the middle */\n"
"    background: transparent; /* Set "
                        "the background as transparent */\n"
"}\n"
"")
        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(262, 175, 159, 43))
        self.comboBox_2.setStyleSheet(u"QComboBox {\n"
" 	background-color:transparent;\n"
"	border:none;\n"
"	color: white;\n"
"	font-size: 12px;\n"
"    padding: 3px; /* Set padding to adjust the text position */\n"
"    combobox-popup: 0; /* Remove the side scroll bar */\n"
"}\n"
"QComboBox::hover{\n"
"border: 2px solid rgba(115, 255, 138, 0.3);\n"
"border-radius: 10px; \n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	background-color: transparent;\n"
"   }\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgba(123, 255, 128, 0.76);\n"
"	color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox::down-arrow {\n"
"    image:url(:/newPrefix/arrow.png); /* Replace with the path to your downward arrow image */\n"
"    width: 35; /* Adjust the width of the arrow image */\n"
"    height: 35; /* Adjust the height of the arrow image */\n"
"    padding-right: 14px; /* Adjust the padding between the arrow and text */\n"
"    vertical-align: middle; /* Align the arrow vertically in the middle */\n"
"    background: transparent; /* Set "
                        "the background as transparent */\n"
"}\n"
"")
        self.comboBox_3 = QComboBox(Form)
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(62, 237, 359, 43))
        self.comboBox_3.setStyleSheet(u"QComboBox {\n"
" 	background-color:transparent;\n"
"	border:none;\n"
"	color: white;\n"
"	font-size: 12px;\n"
"    padding: 3px; /* Set padding to adjust the text position */\n"
"    combobox-popup: 0; /* Remove the side scroll bar */\n"
"}\n"
"QComboBox::hover{\n"
"border: 2px solid rgba(115, 255, 138, 0.3);\n"
"border-radius: 10px; \n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	background-color: transparent;\n"
"   }\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgba(123, 255, 128, 0.76);\n"
"	color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox::down-arrow {\n"
"    image:url(:/newPrefix/arrow.png); /* Replace with the path to your downward arrow image */\n"
"    width: 35; /* Adjust the width of the arrow image */\n"
"    height: 35; /* Adjust the height of the arrow image */\n"
"    padding-right: 14px; /* Adjust the padding between the arrow and text */\n"
"    vertical-align: middle; /* Align the arrow vertically in the middle */\n"
"    background: transparent; /* Set "
                        "the background as transparent */\n"
"}\n"
"")
        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(535, 118, 366, 136))
        self.label_11.setStyleSheet(u"QLabel{\n"
"background-color: transparent;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QLabel::hover{\n"
"border: 2px solid rgba(210, 115, 255, 0.3);\n"
"background-color: rgba(210, 115, 255, 0.3);\n"
"\n"
"}")
        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(537, 267, 366, 136))
        self.label_12.setStyleSheet(u"QLabel{\n"
"background-color: transparent;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QLabel::hover{\n"
"border: 2px solid rgba(210, 115, 255, 0.3);\n"
"background-color: rgba(210, 115, 255, 0.3);\n"
"\n"
"}")
        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(539, 415, 366, 136))
        self.label_13.setStyleSheet(u"QLabel{\n"
"background-color: transparent;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QLabel::hover{\n"
"border: 2px solid rgba(210, 115, 255, 0.3);\n"
"background-color: rgba(210, 115, 255, 0.3);\n"
"\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    
    def mapq(self,flag1,flag2):
        self.f11= QPixmap(flag1)
        self.f22 =  QPixmap(flag2)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Current Score", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Overs Done", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"Wickets Out", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"Runs Last Five", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Predict Score", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_8.setText("")
        self.label_9.setText("")
        self.label_10.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Select Batting Team", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"Select Bowling Team", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("Form", u"Select City", None))

        self.label_11.setText("")
        self.label_12.setText("")
        self.label_13.setText("")
    # retranslateUi

