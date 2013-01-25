
from PyQt4 import QtCore, QtGui
import socket

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.connected = False
        mixsock = socket

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(963, 421)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.in1A = QtGui.QPushButton(self.centralwidget)
        self.in1A.setGeometry(QtCore.QRect(140, 120, 51, 51))
        self.in1A.setObjectName(_fromUtf8("in1A"))
        self.in2A = QtGui.QPushButton(self.centralwidget)
        self.in2A.setGeometry(QtCore.QRect(210, 120, 51, 51))
        self.in2A.setObjectName(_fromUtf8("in2A"))
        self.in3A = QtGui.QPushButton(self.centralwidget)
        self.in3A.setGeometry(QtCore.QRect(280, 120, 51, 51))
        self.in3A.setObjectName(_fromUtf8("in3A"))
        self.in6A = QtGui.QPushButton(self.centralwidget)
        self.in6A.setGeometry(QtCore.QRect(490, 120, 51, 51))
        self.in6A.setObjectName(_fromUtf8("in6A"))
        self.in5A = QtGui.QPushButton(self.centralwidget)
        self.in5A.setGeometry(QtCore.QRect(420, 120, 51, 51))
        self.in5A.setObjectName(_fromUtf8("in5A"))
        self.in4A = QtGui.QPushButton(self.centralwidget)
        self.in4A.setGeometry(QtCore.QRect(350, 120, 51, 51))
        self.in4A.setObjectName(_fromUtf8("in4A"))
        self.in6B = QtGui.QPushButton(self.centralwidget)
        self.in6B.setGeometry(QtCore.QRect(490, 240, 51, 51))
        self.in6B.setObjectName(_fromUtf8("in6B"))
        self.in3B = QtGui.QPushButton(self.centralwidget)
        self.in3B.setGeometry(QtCore.QRect(280, 240, 51, 51))
        self.in3B.setObjectName(_fromUtf8("in3B"))
        self.in5B = QtGui.QPushButton(self.centralwidget)
        self.in5B.setGeometry(QtCore.QRect(420, 240, 51, 51))
        self.in5B.setObjectName(_fromUtf8("in5B"))
        self.in2B = QtGui.QPushButton(self.centralwidget)
        self.in2B.setGeometry(QtCore.QRect(210, 240, 51, 51))
        self.in2B.setObjectName(_fromUtf8("in2B"))
        self.in1B = QtGui.QPushButton(self.centralwidget)
        self.in1B.setGeometry(QtCore.QRect(140, 240, 51, 51))
        self.in1B.setObjectName(_fromUtf8("in1B"))
        QtCore.QObject.connect(self.in1B, QtCore.SIGNAL("clicked()"), self.input)
        self.in4B = QtGui.QPushButton(self.centralwidget)
        self.in4B.setGeometry(QtCore.QRect(350, 240, 51, 51))
        self.in4B.setObjectName(_fromUtf8("in4B"))

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 250, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.connectBtn = QtGui.QPushButton(self.centralwidget)
        self.connectBtn.setGeometry(QtCore.QRect(130, 10, 71, 23))
        self.connectBtn.setAutoDefault(False)
        self.connectBtn.setDefault(False)
        self.connectBtn.setFlat(False)
        self.connectBtn.setObjectName(_fromUtf8("connectBtn"))
        QtCore.QObject.connect(self.connectBtn, QtCore.SIGNAL("clicked()"), self.mixConnect)

        self.blackA = QtGui.QPushButton(self.centralwidget)
        self.blackA.setGeometry(QtCore.QRect(70, 120, 51, 51))
        self.blackA.setObjectName(_fromUtf8("blackA"))
        self.blackB = QtGui.QPushButton(self.centralwidget)
        self.blackB.setGeometry(QtCore.QRect(70, 240, 51, 51))
        self.blackB.setObjectName(_fromUtf8("blackB"))

        self.takeBtn = QtGui.QPushButton(self.centralwidget)
        self.takeBtn.setGeometry(QtCore.QRect(660, 140, 51, 51))
        self.takeBtn.setObjectName(_fromUtf8("take"))
        QtCore.QObject.connect(self.takeBtn, QtCore.SIGNAL("clicked()"), self.take)

        self.freezeBtn = QtGui.QPushButton(self.centralwidget)
        self.freezeBtn.setGeometry(QtCore.QRect(590, 210, 51, 51))
        self.freezeBtn.setObjectName(_fromUtf8("freeze"))
        QtCore.QObject.connect(self.freezeBtn, QtCore.SIGNAL("clicked()"), self.freeze)

        self.fadeBtn = QtGui.QPushButton(self.centralwidget)
        self.fadeBtn.setGeometry(QtCore.QRect(590, 140, 51, 51))
        self.fadeBtn.setObjectName(_fromUtf8("fade"))
        QtCore.QObject.connect(self.fadeBtn, QtCore.SIGNAL("clicked()"), self.fade)

        self.standby = QtGui.QPushButton(self.centralwidget)
        self.standby.setGeometry(QtCore.QRect(210, 10, 75, 23))
        self.standby.setAutoDefault(False)
        self.standby.setDefault(False)
        self.standby.setFlat(False)
        self.standby.setObjectName(_fromUtf8("standby"))
        QtCore.QObject.connect(self.standby, QtCore.SIGNAL("clicked()"), self.shutdown)
        #self.standby.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.pipBtn = QtGui.QPushButton(self.centralwidget)
        self.pipBtn.setGeometry(QtCore.QRect(660, 210, 51, 51))
        self.pipBtn.setObjectName(_fromUtf8("pip"))
        QtCore.QObject.connect(self.pipBtn, QtCore.SIGNAL("clicked()"), self.pip)

        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(760, 130, 161, 161))
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName(_fromUtf8("frame"))

        self.downBtn = QtGui.QPushButton(self.frame)
        self.downBtn.setGeometry(QtCore.QRect(60, 110, 41, 41))
        self.downBtn.setText(_fromUtf8(""))
        self.downBtn.setObjectName(_fromUtf8("down"))
        QtCore.QObject.connect(self.downBtn, QtCore.SIGNAL("clicked()"), self.down)

        self.selectBtn = QtGui.QPushButton(self.frame)
        self.selectBtn.setGeometry(QtCore.QRect(60, 60, 41, 41))
        self.selectBtn.setText(_fromUtf8(""))
        self.selectBtn.setObjectName(_fromUtf8("select"))
        QtCore.QObject.connect(self.selectBtn, QtCore.SIGNAL("clicked()"), self.select)

        self.upBtn = QtGui.QPushButton(self.frame)
        self.upBtn.setGeometry(QtCore.QRect(60, 10, 41, 41))
        self.upBtn.setText(_fromUtf8(""))
        self.upBtn.setObjectName(_fromUtf8("up"))
        QtCore.QObject.connect(self.upBtn, QtCore.SIGNAL("clicked()"), self.up)

        self.rightBtn = QtGui.QPushButton(self.frame)
        self.rightBtn.setGeometry(QtCore.QRect(110, 60, 41, 41))
        self.rightBtn.setText(_fromUtf8(""))
        self.rightBtn.setObjectName(_fromUtf8("right"))
        QtCore.QObject.connect(self.rightBtn, QtCore.SIGNAL("clicked()"), self.right)

        self.leftBtn = QtGui.QPushButton(self.frame)
        self.leftBtn.setGeometry(QtCore.QRect(10, 60, 41, 41))
        self.leftBtn.setText(_fromUtf8(""))
        self.leftBtn.setObjectName(_fromUtf8("left"))
        QtCore.QObject.connect(self.leftBtn, QtCore.SIGNAL("clicked()"), self.left)

        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(760, 110, 91, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.ip = QtGui.QLineEdit(self.centralwidget)
        self.ip.setGeometry(QtCore.QRect(10, 10, 113, 20))
        self.ip.setText(_fromUtf8("10.11.12.23"))
        self.ip.setObjectName(_fromUtf8("ip"))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 963, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)


        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit.triggered.connect(QtGui.qApp.quit)

        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))

        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionPreferences)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "VKmix", None))
        self.in1A.setStatusTip(_translate("MainWindow", "Input 1", None))
        self.in1A.setText(_translate("MainWindow", "1", None))
        self.in2A.setStatusTip(_translate("MainWindow", "Input 2", None))
        self.in2A.setText(_translate("MainWindow", "2", None))
        self.in3A.setStatusTip(_translate("MainWindow", "Input 3", None))
        self.in3A.setText(_translate("MainWindow", "3", None))
        self.in6A.setStatusTip(_translate("MainWindow", "Input 6", None))
        self.in6A.setText(_translate("MainWindow", "6", None))
        self.in5A.setStatusTip(_translate("MainWindow", "Input 5", None))
        self.in5A.setText(_translate("MainWindow", "5", None))
        self.in4A.setStatusTip(_translate("MainWindow", "Input 4", None))
        self.in4A.setText(_translate("MainWindow", "4", None))
        self.in6B.setStatusTip(_translate("MainWindow", "Input 6", None))
        self.in6B.setText(_translate("MainWindow", "6", None))
        self.in3B.setStatusTip(_translate("MainWindow", "Input 3", None))
        self.in3B.setText(_translate("MainWindow", "3", None))
        self.in5B.setStatusTip(_translate("MainWindow", "Input 5", None))
        self.in5B.setText(_translate("MainWindow", "5", None))
        self.in2B.setStatusTip(_translate("MainWindow", "Input 2", None))
        self.in2B.setText(_translate("MainWindow", "2", None))
        self.in1B.setStatusTip(_translate("MainWindow", "Input 1", None))
        self.in1B.setText(_translate("MainWindow", "1", None))
        self.in4B.setStatusTip(_translate("MainWindow", "Input 4", None))
        self.in4B.setText(_translate("MainWindow", "4", None))
        self.label.setText(_translate("MainWindow", "Preview", None))
        self.label_2.setText(_translate("MainWindow", "Program", None))
        self.connectBtn.setStatusTip(_translate("MainWindow", "Connect", None))
        self.connectBtn.setText(_translate("MainWindow", "Connect", None))
        self.blackA.setStatusTip(_translate("MainWindow", "Black", None))
        self.blackA.setText(_translate("MainWindow", "Black", None))
        self.blackB.setStatusTip(_translate("MainWindow", "Black", None))
        self.blackB.setText(_translate("MainWindow", "Black", None))
        self.takeBtn.setStatusTip(_translate("MainWindow", "Take", None))
        self.takeBtn.setText(_translate("MainWindow", "Take", None))
        self.freezeBtn.setStatusTip(_translate("MainWindow", "Freeze", None))
        self.freezeBtn.setText(_translate("MainWindow", "Freeze", None))
        self.fadeBtn.setStatusTip(_translate("MainWindow", "Fade", None))
        self.fadeBtn.setText(_translate("MainWindow", "Fade", None))
        self.standby.setStatusTip(_translate("MainWindow", "Standby", None))
        self.standby.setText(_translate("MainWindow", "Standby", None))
        self.pipBtn.setStatusTip(_translate("MainWindow", "PIP", None))
        self.pipBtn.setText(_translate("MainWindow", "PIP", None))
        self.downBtn.setStatusTip(_translate("MainWindow", "Down", None))
        self.selectBtn.setStatusTip(_translate("MainWindow", "Select", None))
        self.upBtn.setStatusTip(_translate("MainWindow", "Up", None))
        self.rightBtn.setStatusTip(_translate("MainWindow", "Right", None))
        self.leftBtn.setStatusTip(_translate("MainWindow", "Left", None))
        self.label_3.setText(_translate("MainWindow", "System buttons", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences", None))

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

    def mixConnect(self): #set
        IP = self.ip.text()
        PORT = 10001
        self.mixsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mixsock.settimeout(3) # 3 second timeout

        if self.connected == False:
            try:
                self.statusbar.showMessage('Connecting...')
                self.mixsock.connect((IP, PORT))
                self.connected = True
                self.statusbar.showMessage('Connected')
                self.connectBtn.setText(_translate("MainWindow", "Disonnect", None))
            except socket.error:
                self.statusbar.showMessage('Socket error')
        elif self.connected:
            self.mixsock.close()
            self.connected = False
            self.connectBtn.setText(_translate("MainWindow", "Connect", None))

    def shutdown(self): #set
        if self.connected:
            self.mixsock.sendall("F041041024F0400E1??\r")
            self.mixsock.recv(4096)
            self.mixsock.close()
        else:
            self.statusbar.showMessage('Disconnected')

    def select(self): #set
        if self.connected:
            self.mixsock.sendall("F041041024F000128??\r")
            return self.mixsock.recv(4096)
        else:
            self.statusbar.showMessage('Disconnected')

    def fade(self): #set
        if self.connected:
            self.mixsock.sendall("F041041024F000251??\r")
            return self.mixsock.recv(4096)
        else:
            self.statusbar.showMessage('Disconnected')

    def take(self): #set
        if self.connected:
            self.mixsock.sendall("F041041024F00020F??\r")
            return self.mixsock.recv(4096)
        else:
            self.statusbar.showMessage('Disconnected')

    def up(self): #set
        if self.connected:
            self.mixsock.sendall("F041041024F00024C??\r")
            return self.mixsock.recv(4096)
        else:
            self.statusbar.showMessage('Disconnected')

    def down(self): #set
        if self.connected:
            self.mixsock.sendall("F041041024F00024B??\r")
            return self.mixsock.recv(4096)
        else:
            self.statusbar.showMessage('Disconnected')

    def left(self): #set
        if self.connected:
            self.mixsock.sendall("F041041024F000129??\r")
            return self.mixsock.recv(4096)
        else:
            self.statusbar.showMessage('Disconnected')

    def right(self): #set
        if self.connected:
            self.mixsock.sendall("F041041024F00012A??\r")
            return self.mixsock.recv(4096)
        else:
            self.statusbar.showMessage('Disconnected')

    def freeze(self): #set
        if self.connected:
            self.mixsock.sendall("F041041024F000211??\r")
            return self.mixsock.recv(4096)
        else:
            self.statusbar.showMessage('Disconnected')

    def pip(self): #set
        if self.connected:
            self.mixsock.sendall("F041041024F000257??\r")
            return self.mixsock.recv(4096)
        else:
            self.statusbar.showMessage('Disconnected')

    def input(self):
        if self.connected:
            self.mixsock.sendall("F041041024F00024E??\r")
            return self.mixsock.recv(4096)
        else:
            self.statusbar.showMessage('Disconnected')






if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

