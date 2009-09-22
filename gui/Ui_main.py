# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Tue Sep 22 17:17:00 2009
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(574, 601)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtGui.QSplitter(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.tabWidget = QtGui.QTabWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.text = CodeEditor(self.tab)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        self.text.setFont(font)
        self.text.setObjectName("text")
        self.horizontalLayout.addWidget(self.text)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.style = CodeEditor(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        self.style.setFont(font)
        self.style.setObjectName("style")
        self.horizontalLayout_2.addWidget(self.style)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 574, 28))
        self.menuBar.setObjectName("menuBar")
        self.menuText = QtGui.QMenu(self.menuBar)
        self.menuText.setObjectName("menuText")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.pdfbar = QtGui.QToolBar(MainWindow)
        self.pdfbar.setObjectName("pdfbar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.pdfbar)
        self.actionLoad_Text = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/fileopen.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoad_Text.setIcon(icon)
        self.actionLoad_Text.setObjectName("actionLoad_Text")
        self.actionLoad_Style = QtGui.QAction(MainWindow)
        self.actionLoad_Style.setIcon(icon)
        self.actionLoad_Style.setObjectName("actionLoad_Style")
        self.actionRender = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/pdf.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRender.setIcon(icon1)
        self.actionRender.setObjectName("actionRender")
        self.actionSave_Text = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/filesave.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_Text.setIcon(icon2)
        self.actionSave_Text.setObjectName("actionSave_Text")
        self.actionSave_Style = QtGui.QAction(MainWindow)
        self.actionSave_Style.setIcon(icon2)
        self.actionSave_Style.setObjectName("actionSave_Style")
        self.actionSave_PDF = QtGui.QAction(MainWindow)
        self.actionSave_PDF.setIcon(icon1)
        self.actionSave_PDF.setObjectName("actionSave_PDF")
        self.menuText.addAction(self.actionLoad_Text)
        self.menuText.addAction(self.actionLoad_Style)
        self.menuText.addSeparator()
        self.menuText.addAction(self.actionSave_Text)
        self.menuText.addAction(self.actionSave_Style)
        self.menuText.addAction(self.actionSave_PDF)
        self.menuBar.addAction(self.menuText.menuAction())
        self.toolBar.addAction(self.actionLoad_Text)
        self.toolBar.addAction(self.actionRender)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.text, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.style)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Text", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "StyleSheet", None, QtGui.QApplication.UnicodeUTF8))
        self.menuText.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.pdfbar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar_2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_Text.setText(QtGui.QApplication.translate("MainWindow", "Open Text", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_Text.setToolTip(QtGui.QApplication.translate("MainWindow", "Open Text", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_Style.setText(QtGui.QApplication.translate("MainWindow", "Open Style", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_Style.setToolTip(QtGui.QApplication.translate("MainWindow", "Open Style", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRender.setText(QtGui.QApplication.translate("MainWindow", "Render", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Text.setText(QtGui.QApplication.translate("MainWindow", "Save Text", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Text.setToolTip(QtGui.QApplication.translate("MainWindow", "Save Text", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Style.setText(QtGui.QApplication.translate("MainWindow", "Save Style", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Style.setToolTip(QtGui.QApplication.translate("MainWindow", "Save Style", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_PDF.setText(QtGui.QApplication.translate("MainWindow", "Save PDF", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_PDF.setToolTip(QtGui.QApplication.translate("MainWindow", "Save PDF", None, QtGui.QApplication.UnicodeUTF8))

from codeeditor import CodeEditor
import icons_rc
