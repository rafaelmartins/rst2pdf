# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'style.ui'
#
# Created: Mon Sep 28 16:31:48 2009
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(365, 446)
        self.formLayout = QtGui.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.fontComboBox = QtGui.QFontComboBox(Form)
        self.fontComboBox.setObjectName("fontComboBox")
        self.gridLayout.addWidget(self.fontComboBox, 1, 0, 1, 2)
        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 2, 0, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(Form)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 2, 1, 1, 1)
        self.checkBox_3 = QtGui.QCheckBox(Form)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 0, 0, 1, 1)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.gridLayout)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.spinBox = QtGui.QSpinBox(Form)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.comboBox_2 = QtGui.QComboBox(Form)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.checkBox_4 = QtGui.QCheckBox(Form)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_2.addWidget(self.checkBox_4)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_11 = QtGui.QCheckBox(Form)
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout_2.addWidget(self.checkBox_11, 0, 0, 1, 1)
        self.comboBox_9 = QtGui.QComboBox(Form)
        self.comboBox_9.setObjectName("comboBox_9")
        self.gridLayout_2.addWidget(self.comboBox_9, 0, 1, 1, 1)
        self.spinBox_2 = QtGui.QSpinBox(Form)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_2.addWidget(self.spinBox_2, 1, 0, 1, 1)
        self.comboBox_3 = QtGui.QComboBox(Form)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_2.addWidget(self.comboBox_3, 1, 1, 1, 1)
        self.formLayout.setLayout(4, QtGui.QFormLayout.FieldRole, self.gridLayout_2)
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.toolButton = QtGui.QToolButton(Form)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_3.addWidget(self.toolButton)
        self.toolButton_2 = QtGui.QToolButton(Form)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout_3.addWidget(self.toolButton_2)
        self.toolButton_3 = QtGui.QToolButton(Form)
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout_3.addWidget(self.toolButton_3)
        self.toolButton_4 = QtGui.QToolButton(Form)
        self.toolButton_4.setObjectName("toolButton_4")
        self.horizontalLayout_3.addWidget(self.toolButton_4)
        self.checkBox_10 = QtGui.QCheckBox(Form)
        self.checkBox_10.setObjectName("checkBox_10")
        self.horizontalLayout_3.addWidget(self.checkBox_10)
        self.formLayout.setLayout(5, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_7)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.spinBox_3 = QtGui.QSpinBox(Form)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout_4.addWidget(self.spinBox_3)
        self.comboBox_4 = QtGui.QComboBox(Form)
        self.comboBox_4.setObjectName("comboBox_4")
        self.horizontalLayout_4.addWidget(self.comboBox_4)
        self.checkBox_9 = QtGui.QCheckBox(Form)
        self.checkBox_9.setObjectName("checkBox_9")
        self.horizontalLayout_4.addWidget(self.checkBox_9)
        self.formLayout.setLayout(6, QtGui.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_8)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.spinBox_4 = QtGui.QSpinBox(Form)
        self.spinBox_4.setObjectName("spinBox_4")
        self.horizontalLayout_5.addWidget(self.spinBox_4)
        self.comboBox_5 = QtGui.QComboBox(Form)
        self.comboBox_5.setObjectName("comboBox_5")
        self.horizontalLayout_5.addWidget(self.comboBox_5)
        self.checkBox_8 = QtGui.QCheckBox(Form)
        self.checkBox_8.setObjectName("checkBox_8")
        self.horizontalLayout_5.addWidget(self.checkBox_8)
        self.formLayout.setLayout(7, QtGui.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_9)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.spinBox_5 = QtGui.QSpinBox(Form)
        self.spinBox_5.setObjectName("spinBox_5")
        self.horizontalLayout_6.addWidget(self.spinBox_5)
        self.comboBox_6 = QtGui.QComboBox(Form)
        self.comboBox_6.setObjectName("comboBox_6")
        self.horizontalLayout_6.addWidget(self.comboBox_6)
        self.checkBox_7 = QtGui.QCheckBox(Form)
        self.checkBox_7.setObjectName("checkBox_7")
        self.horizontalLayout_6.addWidget(self.checkBox_7)
        self.formLayout.setLayout(8, QtGui.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.label_10 = QtGui.QLabel(Form)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_10)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.spinBox_6 = QtGui.QSpinBox(Form)
        self.spinBox_6.setObjectName("spinBox_6")
        self.horizontalLayout_7.addWidget(self.spinBox_6)
        self.comboBox_7 = QtGui.QComboBox(Form)
        self.comboBox_7.setObjectName("comboBox_7")
        self.horizontalLayout_7.addWidget(self.comboBox_7)
        self.checkBox_6 = QtGui.QCheckBox(Form)
        self.checkBox_6.setObjectName("checkBox_6")
        self.horizontalLayout_7.addWidget(self.checkBox_6)
        self.formLayout.setLayout(9, QtGui.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.label_11 = QtGui.QLabel(Form)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(10, QtGui.QFormLayout.LabelRole, self.label_11)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.spinBox_7 = QtGui.QSpinBox(Form)
        self.spinBox_7.setObjectName("spinBox_7")
        self.horizontalLayout_8.addWidget(self.spinBox_7)
        self.comboBox_8 = QtGui.QComboBox(Form)
        self.comboBox_8.setObjectName("comboBox_8")
        self.horizontalLayout_8.addWidget(self.comboBox_8)
        self.checkBox_5 = QtGui.QCheckBox(Form)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout_8.addWidget(self.checkBox_5)
        self.formLayout.setLayout(10, QtGui.QFormLayout.FieldRole, self.horizontalLayout_8)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Parent:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Font:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Form", "Bold", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("Form", "Italic", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_3.setText(QtGui.QApplication.translate("Form", "Inherited", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Font Size:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_4.setText(QtGui.QApplication.translate("Form", "Inherited", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Leading:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_11.setText(QtGui.QApplication.translate("Form", "Inherited", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Alignment:", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_2.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_3.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_4.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_10.setText(QtGui.QApplication.translate("Form", "Inherited", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "Left Indent:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_9.setText(QtGui.QApplication.translate("Form", "Inherited", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "Right Indent:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_8.setText(QtGui.QApplication.translate("Form", "Inherited", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "First Line Indent:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_7.setText(QtGui.QApplication.translate("Form", "Inherited", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Form", "Space Before:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_6.setText(QtGui.QApplication.translate("Form", "Inherited", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Form", "Space After:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_5.setText(QtGui.QApplication.translate("Form", "Inherited", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

