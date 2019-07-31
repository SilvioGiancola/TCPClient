
from PyQt5.QtCore import QDataStream, QIODevice, QObject, QByteArray, pyqtSignal
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import QTcpSocket, QAbstractSocket
from PyQt5.QtNetwork import *
from PyQt5.QtGui import QPixmap, QImage                                

from PyQt5 import QtWidgets, uic
from functools import partial


# PORTS = (9998, 8000)
# PORT = 8000
# SIZEOF_UINT32 = 4
# HOST = "10.68.74.44"


import sys, signal

import io
import socket
import struct
import time
import pickle
import zlib

import numpy as np
from libs.clientAbstract import ClientAbstract

class ClientSocket(ClientAbstract):

    messageReceived = pyqtSignal(str)
    messageSent = pyqtSignal(str)
    
    def __init__(self, parent=None, HOST="localhost", PORT=0000):
        super(ClientSocket, self).__init__(parent, HOST, PORT)
        self.client_socket = None
        print("[DEPRECATED] ClientSocket is deprecated, please use the Qt version")

    def connectToServer(self):
        #connected only when sending message
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.HOST, self.PORT))
            connection = self.client_socket.makefile('wb')
        except:
            self.client_socket = None
            pass

    def disconnectToServer(self):
        #connected only when sending message
        self.client_socket.close()
        self.client_socket = None
        # pass

    def isConnected(self):
        return self.client_socket is not None


    def sendImage(self):

        if not self.isConnected():
            self.connectToServer()

        if self.isConnected():

            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
            
            frame = cv2.imread('picture_10.jpg')
            result, frame = cv2.imencode('.jpg', frame, encode_param)

            data = pickle.dumps(frame, 0)
            size = len(data)

        # SEND Image
            self.client_socket.sendall(struct.pack(">L", size) + data)


        # Receive Answer
            data = b""
            payload_size = struct.calcsize(">L")
            print("payload_size: {}".format(payload_size))
            # while True:
            while len(data) < payload_size:
                print("Recv: {}".format(len(data)))
                data += self.client_socket.recv(4096)

            print("Done Recv: {}".format(len(data)))
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack(">L", packed_msg_size)[0]
            print("msg_size: {}".format(msg_size))
            while len(data) < msg_size:
                data += self.client_socket.recv(4096)
            frame_data = data[:msg_size]
            data = data[msg_size:]

            print("data", frame_data)
            print("nparray", np.frombuffer(frame_data, dtype=np.float64).reshape((-1,4)))

            self.disconnectToServer()


