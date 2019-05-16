# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(291, 201)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setContentsMargins(5, 0, 5, 5)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.closeBtn = QtWidgets.QPushButton(Form)
        self.closeBtn.setMinimumSize(QtCore.QSize(23, 23))
        self.closeBtn.setMaximumSize(QtCore.QSize(23, 23))
        self.closeBtn.setStyleSheet("background-color: rgb(255, 133, 135);")
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout_2.addWidget(self.closeBtn, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.minBtn = QtWidgets.QPushButton(Form)
        self.minBtn.setMinimumSize(QtCore.QSize(23, 23))
        self.minBtn.setMaximumSize(QtCore.QSize(23, 23))
        self.minBtn.setObjectName("minBtn")
        self.horizontalLayout_2.addWidget(self.minBtn, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.newGroupBtn = QtWidgets.QPushButton(Form)
        self.newGroupBtn.setMinimumSize(QtCore.QSize(75, 23))
        self.newGroupBtn.setMaximumSize(QtCore.QSize(75, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        self.newGroupBtn.setFont(font)
        self.newGroupBtn.setStyleSheet("background-color: rgb(226, 255, 225);")
        self.newGroupBtn.setObjectName("newGroupBtn")
        self.horizontalLayout_2.addWidget(self.newGroupBtn, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.horizontalLayout_2.setStretch(1, 2000)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setMinimumSize(QtCore.QSize(281, 171))
        self.groupBox.setMaximumSize(QtCore.QSize(281, 171))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.groupsTable = QtWidgets.QTableWidget(self.groupBox)
        self.groupsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.groupsTable.setObjectName("groupsTable")
        self.groupsTable.setColumnCount(2)
        self.groupsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.groupsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.groupsTable.setHorizontalHeaderItem(1, item)
        self.groupsTable.horizontalHeader().setDefaultSectionSize(126)
        self.gridLayout.addWidget(self.groupsTable, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Expenses Splitter - Группы"))
        self.closeBtn.setText(_translate("Form", "✕"))
        self.minBtn.setText(_translate("Form", "_"))
        self.newGroupBtn.setText(_translate("Form", "Создать"))
        self.groupBox.setTitle(_translate("Form", "Группы"))
        item = self.groupsTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Название"))
        item = self.groupsTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Дата"))

