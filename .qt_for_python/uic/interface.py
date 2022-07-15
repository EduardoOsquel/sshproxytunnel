# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/eduardo/Git/sshproxytunnel/gui/interface.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 400)
        MainWindow.setMinimumSize(QtCore.QSize(800, 400))
        MainWindow.setMaximumSize(QtCore.QSize(800, 400))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        MainWindow.setBaseSize(QtCore.QSize(800, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/eduardo/Git/sshproxytunnel/gui/../icons/console.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolTipDuration(1)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.userEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.userEdit.setGeometry(QtCore.QRect(10, 30, 200, 28))
        self.userEdit.setObjectName("userEdit")
        self.userLabel = QtWidgets.QLabel(self.centralwidget)
        self.userLabel.setGeometry(QtCore.QRect(10, 10, 58, 21))
        self.userLabel.setObjectName("userLabel")
        self.serverEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.serverEdit.setGeometry(QtCore.QRect(10, 80, 200, 28))
        self.serverEdit.setObjectName("serverEdit")
        self.serverLabel = QtWidgets.QLabel(self.centralwidget)
        self.serverLabel.setGeometry(QtCore.QRect(10, 60, 58, 21))
        self.serverLabel.setObjectName("serverLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAdd_Server = QtWidgets.QAction(MainWindow)
        self.actionAdd_Server.setObjectName("actionAdd_Server")
        self.menuFile.addAction(self.actionAdd_Server)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SSH Tunneling"))
        self.userLabel.setText(_translate("MainWindow", "User:"))
        self.serverLabel.setText(_translate("MainWindow", "Server:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionAdd_Server.setText(_translate("MainWindow", "Add Server"))
        self.actionAdd_Server.setShortcut(_translate("MainWindow", "Ctrl+A"))
