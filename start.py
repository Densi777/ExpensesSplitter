import os
import sys
import postgresql
from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import window_move
import start_form

class ES(QtWidgets.QWidget, start_form.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.newGroupBtn.clicked.connect(self.new_group_win) 
        self.minBtn.clicked.connect(self.showMinimized)
        self.closeBtn.clicked.connect(self.exit_program)

    def new_group_win(self):
        pass

    def exit_program(self):
        QApplication.quit()

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = ES()
    window_move.setMoveWindow(window)
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()