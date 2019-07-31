# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit.setText("")
        self.lineedit.setObjectName("lineedit")
        self.verticalLayout.addWidget(self.lineedit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.IPLine = QtWidgets.QLineEdit(self.centralwidget)
        self.IPLine.setObjectName("IPLine")
        self.horizontalLayout_2.addWidget(self.IPLine)
        self.portBox = QtWidgets.QSpinBox(self.centralwidget)
        self.portBox.setMaximum(99999)
        self.portBox.setProperty("value", 8493)
        self.portBox.setObjectName("portBox")
        self.horizontalLayout_2.addWidget(self.portBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setObjectName("connectButton")
        self.horizontalLayout.addWidget(self.connectButton)
        self.disconnectButton = QtWidgets.QPushButton(self.centralwidget)
        self.disconnectButton.setObjectName("disconnectButton")
        self.horizontalLayout.addWidget(self.disconnectButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.sendImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendImageButton.setObjectName("sendImageButton")
        self.verticalLayout.addWidget(self.sendImageButton)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.IPLine.setText(_translate("MainWindow", "10.68.74.44"))
        self.connectButton.setText(_translate("MainWindow", "Connect"))
        self.disconnectButton.setText(_translate("MainWindow", "Disconnect"))
        self.sendImageButton.setText(_translate("MainWindow", "Send Image"))
