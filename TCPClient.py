import sys, signal
from functools import partial
import argparse

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from libs.frontend import Ui_MainWindow

from libs.clientQt import ClientQt
from libs.clientSocket import ClientSocket

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def main():

    # Argument Parser
    parser = argparse.ArgumentParser(
        description="Run a TCP Client user Interface to connect and ocmmunicate with a specific server ")
    parser.add_argument("--HOST", type=str, default="localhost",
                        help="host IP")
    parser.add_argument("--PORT", type=int, default=8493,
                        help="commmunication port")
    parser.add_argument("--socket",action="store_true", 
                        help="use socket instead of QTCPSocket (deprecated)")
    args = parser.parse_args()

    app = QApplication(sys.argv)
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    win = uic.loadUi("libs/frontend.ui")
    # win = MainWindow()
    
    win.IPLine.setText(args.HOST)
    win.portBox.setValue(args.PORT)    

    if args.socket:
        cli = ClientSocket(HOST=args.HOST, PORT=args.PORT)
    else:
        cli = ClientQt(HOST=args.HOST, PORT=args.PORT)

    # Socket connection handle while messaging
    if args.socket:
        win.connectButton.setEnabled(False)
        win.disconnectButton.setEnabled(False)
    # QT handles connection/disconnection
    else:
        win.connectButton.clicked.connect(cli.connectToServer)
        win.disconnectButton.clicked.connect(cli.disconnectToServer)

    win.sendImageButton.clicked.connect(cli.sendImage)

    win.lineedit.returnPressed.connect(cli.sendMessage)
    win.lineedit.textChanged.connect(cli.updateText)

    win.IPLine.returnPressed.connect(lambda: cli.updateIP(win.IPLine.text()))
    win.portBox.valueChanged.connect(cli.updatePort)

    cli.messageReceived.connect(win.textEdit.append)
    cli.messageSent.connect(win.textEdit.append)

    if not args.socket:
        cli.connected.connect(partial(win.connectButton.setEnabled, False))
        cli.connected.connect(partial(win.disconnectButton.setEnabled, True))
        cli.disconnected.connect(partial(win.connectButton.setEnabled, True))
        cli.disconnected.connect(partial(win.disconnectButton.setEnabled, False))
  
    win.show()

    return app.exec_()

if __name__ == '__main__':
    sys.exit(main())