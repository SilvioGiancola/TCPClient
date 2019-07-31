

from PyQt5.QtCore import QDataStream, QIODevice, QObject, QByteArray, pyqtSignal
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import QTcpSocket, QAbstractSocket
from PyQt5.QtNetwork import *
from PyQt5.QtGui import QPixmap, QImage                                

from PyQt5 import QtWidgets, uic
from functools import partial


import sys, signal

import io

# PORTS = (9998, 8000)

# class Client(QMainWindow, Ui_MainWindow):
class ClientAbstract(QObject):

    # conn = pyqtSignal(bool)
    # disconn = pyqtSignal(bool)
    messageReceived = pyqtSignal(str)
    messageSent = pyqtSignal(str)

    # PORT = 8493
    # SIZEOF_UINT32 = 4
    # HOST = "10.68.74.44"


    def __init__(self, parent=None, HOST="localhost", PORT=0000):
        super(ClientAbstract, self).__init__(parent)

        self.HOST = HOST        
        self.PORT = PORT
        self.text = ""

        # Initialize data IO variables
        self.nextBlockSize = 0
        self.request = None

        
        # self.connectToServer()

    # return information if connected
    def isConnected(self):
        pass

    # Create connection to server
    def connectToServer(self):
        pass
        
    # 
    def disconnectToServer(self):
        pass
    
    # send images
    def sendImage(self):
        pass
            

    def sendMessage(self):
        pass


    def readFromServer(self):
        pass


    def serverHasError(self):
        message = f"Error: {self.errorString()}"
        self.messageReceived.emit(message)        
        self.disconnectToServer()

    def updateText(self, txt):
        self.text = txt
        
    def updateIP(self, value):
        self.HOST = value
        self.reconnect()
        
    def updatePort(self, value):
        self.PORT = value
        self.reconnect()

    def reconnect(self):
        self.disconnectToServer()
        self.connectToServer()
              

