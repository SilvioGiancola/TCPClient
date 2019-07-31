from PyQt5.QtCore import QDataStream, QIODevice, QObject, QByteArray, pyqtSignal
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import QTcpSocket, QAbstractSocket
from PyQt5.QtNetwork import *
from PyQt5.QtGui import QPixmap, QImage                                

from PyQt5 import QtWidgets, uic
from functools import partial

from libs.clientAbstract import ClientAbstract

# PORTS = (9998, 8000)

# class Client(QMainWindow, Ui_MainWindow):
class ClientQt(QTcpSocket, ClientAbstract):

    # conn = pyqtSignal(bool)
    # disconn = pyqtSignal(bool)
    messageReceived = pyqtSignal(str)
    messageSent = pyqtSignal(str)

    # PORT = 8493
    SIZEOF_UINT32 = 4
    # HOST = "10.68.74.44"


    def __init__(self, parent=None, HOST="localhost", PORT=0000):
        super(ClientQt, self).__init__(parent, HOST, PORT)

        self.nextBlockSize = 0
        self.request = None
        self.text = ""

        self.stateChanged.connect(self.plotState)
        self.readyRead.connect(self.readFromServer)
        self.disconnected.connect(self.disconnectToServer)
        self.error.connect(self.serverHasError)

        self.connectToServer()


    def isConnected(self):
        return self.state == QAbstractSocket.ConnectedState

    # Create connection to server
    def connectToServer(self):
        self.connectToHost(self.HOST, self.PORT)
        if self.waitForConnected(1000):
            self.messageReceived.emit("[CONNECTED]")
        else:
            self.messageReceived.emit("[NOT CONNECTED]")

    def disconnectToServer(self):
        self.close()

    def sendImage(self):
        self.request = QByteArray()
        stream = QDataStream(self.request, QIODevice.WriteOnly)
        stream.setVersion(QDataStream.Qt_4_9)
        stream.writeUInt32(0)
        stream.writeUInt32(1) # HEADER: this is an QImage

        ba = QByteArray()
        buffer = QBuffer(ba)
        self.img = QImage()
        self.img.load(f"{self.text}")
        self.img.save(buffer, "PNG") # writes image into ba in PNG format
        stream.writeBytes(ba)

        stream.device().seek(0)
        stream.writeUInt32(self.request.size() - self.SIZEOF_UINT32)
        self.write(self.request)
        self.nextBlockSize = 0
        self.request = None
        print(f"sending '{self.text}' to Server")
        self.messageSent.emit("[SENT] " + self.text)


    def sendMessage(self):
        self.request = QByteArray()
        stream = QDataStream(self.request, QIODevice.WriteOnly)
        stream.setVersion(QDataStream.Qt_4_9)
        stream.writeUInt32(0)
        stream.writeUInt32(0) # HEADER: this is a QString

        stream.writeQString(f"{self.text}")

        stream.device().seek(0)
        stream.writeUInt32(self.request.size() - self.SIZEOF_UINT32)
        self.write(self.request)
        self.nextBlockSize = 0
        self.request = None
        print(f"sending '{self.text}' to Server")
        self.messageSent.emit("[SENT] " + self.text)


    def readFromServer(self):
        stream = QDataStream(self)
        stream.setVersion(QDataStream.Qt_4_9)
 
        while True:
            if self.nextBlockSize == 0:
                if self.bytesAvailable() < self.SIZEOF_UINT32:
                    break
                self.nextBlockSize = stream.readUInt32()
            if self.bytesAvailable() < self.nextBlockSize:
                break

            header = stream.readUInt32()
            print("header", header)
            if header == 0: # QString
                textFromServer = stream.readQString()

                # print("messageReceived:", textFromServer)
                print(f"received '{textFromServer}' from Server")

                self.messageReceived.emit("[RECEIVED] " + textFromServer)
                self.nextBlockSize = 0




    def plotState(self, state):        
        if state == 0: print("[STATE] UnconnectedState")
        elif state == 1: print("[STATE] HostLookupState")
        elif state == 2: print("[STATE] ConnectingState")
        elif state == 3: print("[STATE] ConnectedState")
        elif state == 4: print("[STATE] BoundState")
        elif state == 5: print("[STATE] ClosingState")
        elif state == 6: print("[STATE] ListeningState")
        else: print("ERROR: Undefined state")


