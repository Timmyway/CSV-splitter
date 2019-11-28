# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1132, 303)
        MainWindow.setStyleSheet("QMainWindow {\n"
"background-color: #202126;\n"
"color: #ffffff;\n"
"padding: 5px;\n"
"font-family: verdana;\n"
"}\n"
"\n"
"QTextEdit {\n"
"background: qlineargradient( x1:0 y0:1, x2:1 y2:0, stop:0 #0D4242, stop:1 #082222);\n"
"color: #ffffff;\n"
"border-radius: 18px;\n"
"padding: 5px;\n"
"border: 1px solid #CBC9D2;\n"
"}\n"
"\n"
"QPushButton {\n"
"border-radius: 8px;\n"
"width: 60px;\n"
"color: #ffffff;\n"
"border-width: 1px;\n"
"border-color: #ffffff;\n"
"border-style: solid;\n"
"padding: 3px;\n"
"font-size: 16px;\n"
"background-color: #514ea7;\n"
"margin-bottom: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: grey;\n"
"}\n"
"\n"
"QLineEdit {\n"
"border-radius: 8px;\n"
"border-style: solid;\n"
"border-color: #333333;\n"
"background-color: #454545;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QTabWidget::tab_Calendar {\n"
"background-color: #501F95;\n"
"}\n"
"\n"
"QSpinBox {\n"
"font-size: 16px;\n"
"}\n"
"QLabel {\n"
"color: #333333;\n"
"font-family: verdana;\n"
"font-size: 16px;\n"
"}\n"
"\n"
"QCheckBox {\n"
"font-family: courier;\n"
"}\n"
"\n"
"QProgressBar {\n"
"color: #ffffff;\n"
"font-size: 14px;\n"
"}\n"
"\n"
"QComboBox {\n"
"font-family: courier;\n"
"font-size: 17px;\n"
"background-color: #134B4B;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QStatusBar {\n"
"color: #ffffff;\n"
"font-family: verdana;\n"
"font-size: 16px;\n"
"padding: 3px;\n"
"}\n"
"\n"
"QTabWidget {\n"
"font-family: verdana;\n"
"}\n"
"\n"
"/* Particular style */\n"
"\n"
"\n"
"QPushButton#btnOpenLocation {\n"
"    width: 150px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setContentsMargins(0, 0, -1, -1)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_2 = QtWidgets.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setFamily("verdana")
        font.setPointSize(-1)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.spinBoxNbMorceau = QtWidgets.QSpinBox(self.tab_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxNbMorceau.sizePolicy().hasHeightForWidth())
        self.spinBoxNbMorceau.setSizePolicy(sizePolicy)
        self.spinBoxNbMorceau.setObjectName("spinBoxNbMorceau")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBoxNbMorceau)
        self.label = QtWidgets.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setFamily("verdana")
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditAdress = QtWidgets.QLineEdit(self.tab_5)
        self.lineEditAdress.setClearButtonEnabled(True)
        self.lineEditAdress.setObjectName("lineEditAdress")
        self.horizontalLayout.addWidget(self.lineEditAdress)
        self.btnBrowse = QtWidgets.QPushButton(self.tab_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBrowse.sizePolicy().hasHeightForWidth())
        self.btnBrowse.setSizePolicy(sizePolicy)
        self.btnBrowse.setObjectName("btnBrowse")
        self.horizontalLayout.addWidget(self.btnBrowse)
        self.labSize = QtWidgets.QLabel(self.tab_5)
        self.labSize.setObjectName("labSize")
        self.horizontalLayout.addWidget(self.labSize)
        self.formLayout_3.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setFamily("verdana")
        font.setPointSize(-1)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEditOutputName = QtWidgets.QLineEdit(self.tab_5)
        self.lineEditOutputName.setClearButtonEnabled(True)
        self.lineEditOutputName.setObjectName("lineEditOutputName")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditOutputName)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnProcess = QtWidgets.QPushButton(self.tab_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnProcess.sizePolicy().hasHeightForWidth())
        self.btnProcess.setSizePolicy(sizePolicy)
        self.btnProcess.setObjectName("btnProcess")
        self.horizontalLayout_4.addWidget(self.btnProcess, 0, QtCore.Qt.AlignLeft)
        self.btnQuit = QtWidgets.QPushButton(self.tab_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnQuit.sizePolicy().hasHeightForWidth())
        self.btnQuit.setSizePolicy(sizePolicy)
        self.btnQuit.setObjectName("btnQuit")
        self.horizontalLayout_4.addWidget(self.btnQuit)
        self.formLayout_3.setLayout(3, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_4)
        self.gridLayout_4.addLayout(self.formLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.labOriginal = QtWidgets.QLabel(self.tab_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labOriginal.sizePolicy().hasHeightForWidth())
        self.labOriginal.setSizePolicy(sizePolicy)
        self.labOriginal.setObjectName("labOriginal")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labOriginal)
        self.labDedup = QtWidgets.QLabel(self.tab_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labDedup.sizePolicy().hasHeightForWidth())
        self.labDedup.setSizePolicy(sizePolicy)
        self.labDedup.setObjectName("labDedup")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labDedup)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.formOriginalPath = QtWidgets.QLineEdit(self.tab_6)
        self.formOriginalPath.setObjectName("formOriginalPath")
        self.horizontalLayout_5.addWidget(self.formOriginalPath)
        self.btnBrowseOriginal = QtWidgets.QPushButton(self.tab_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBrowseOriginal.sizePolicy().hasHeightForWidth())
        self.btnBrowseOriginal.setSizePolicy(sizePolicy)
        self.btnBrowseOriginal.setObjectName("btnBrowseOriginal")
        self.horizontalLayout_5.addWidget(self.btnBrowseOriginal)
        self.labSizeOriginal = QtWidgets.QLabel(self.tab_6)
        self.labSizeOriginal.setObjectName("labSizeOriginal")
        self.horizontalLayout_5.addWidget(self.labSizeOriginal)
        self.formLayout_4.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.formDedupPath = QtWidgets.QLineEdit(self.tab_6)
        self.formDedupPath.setObjectName("formDedupPath")
        self.horizontalLayout_6.addWidget(self.formDedupPath)
        self.btnBrowseDedup = QtWidgets.QPushButton(self.tab_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBrowseDedup.sizePolicy().hasHeightForWidth())
        self.btnBrowseDedup.setSizePolicy(sizePolicy)
        self.btnBrowseDedup.setObjectName("btnBrowseDedup")
        self.horizontalLayout_6.addWidget(self.btnBrowseDedup)
        self.labSizeDedup = QtWidgets.QLabel(self.tab_6)
        self.labSizeDedup.setObjectName("labSizeDedup")
        self.horizontalLayout_6.addWidget(self.labSizeDedup)
        self.formLayout_4.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.btnCalculate = QtWidgets.QPushButton(self.tab_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCalculate.sizePolicy().hasHeightForWidth())
        self.btnCalculate.setSizePolicy(sizePolicy)
        self.btnCalculate.setObjectName("btnCalculate")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.btnCalculate)
        self.gridLayout_5.addLayout(self.formLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_6, "")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.tabWidget)
        self.btnOpenLocation = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOpenLocation.sizePolicy().hasHeightForWidth())
        self.btnOpenLocation.setSizePolicy(sizePolicy)
        self.btnOpenLocation.setObjectName("btnOpenLocation")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.btnOpenLocation)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1132, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuEdition = QtWidgets.QMenu(self.menubar)
        self.menuEdition.setObjectName("menuEdition")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_as_file = QtWidgets.QAction(MainWindow)
        self.actionSave_as_file.setObjectName("actionSave_as_file")
        self.menuMenu.addAction(self.actionOpen)
        self.menuMenu.addAction(self.actionSave_as_file)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuEdition.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Part number"))
        self.label.setText(_translate("MainWindow", "File path"))
        self.btnBrowse.setText(_translate("MainWindow", "Browse"))
        self.labSize.setText(_translate("MainWindow", "0 KB"))
        self.label_3.setText(_translate("MainWindow", "Export name"))
        self.btnProcess.setText(_translate("MainWindow", "Process"))
        self.btnQuit.setText(_translate("MainWindow", "Quit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Dedup"))
        self.labOriginal.setText(_translate("MainWindow", "Original"))
        self.labDedup.setText(_translate("MainWindow", "Dedup"))
        self.btnBrowseOriginal.setText(_translate("MainWindow", "Browse"))
        self.labSizeOriginal.setText(_translate("MainWindow", "0 Ko"))
        self.btnBrowseDedup.setText(_translate("MainWindow", "Browse"))
        self.labSizeDedup.setText(_translate("MainWindow", "0 Ko"))
        self.btnCalculate.setText(_translate("MainWindow", "Calculate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Dedup difference"))
        self.btnOpenLocation.setText(_translate("MainWindow", "Open Local Folder"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuEdition.setTitle(_translate("MainWindow", "Edition"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave_as_file.setText(_translate("MainWindow", "Save as file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

