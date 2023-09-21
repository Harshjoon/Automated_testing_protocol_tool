#!/usr/bin/python


'''
TODO
 - add warning message for incorrect password               = Pending
 - setup icon                                               = Pending
 - code cleanup                                             = Pending
 - code documentation                                       = Pending

 - show protocols from json data                            = Pending
 - find a way to automate class generation or a single
   class for all the protocols                              = Pending
 - Add image in protocol test case methodology              = Pending
 - 
'''

import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import Qt, QSize, QRegularExpression
from PyQt6.QtWidgets import (
    QCheckBox,
    QPushButton,
    QFileDialog,
    QLineEdit,
    QTableWidget,
    QFormLayout,
    QTabWidget,
    QVBoxLayout,
    QMainWindow,
    QDialog,
    QGridLayout,
    QDialogButtonBox,
    QMessageBox,
    QSizePolicy
)

import sqlite3
from sqlite3 import Error

from main_window import Main_Window

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        # set window icon
        # self.setWindowIcon(QIcon(''))
        self.database_filepath = "../../test.db"

        self.window_width, self.window_height = 600,200
        self.setFixedSize( self.window_width, self.window_height )

        layout = QGridLayout()
        self.setLayout(layout)

        labels = {}
        self.lineEdits = {}

        labels['Username'] = QLabel('Username')
        labels['Password'] = QLabel('Password')
        labels['Username'].setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)
        labels['Password'].setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)

        self.lineEdits['Username']     = QLineEdit()
        self.lineEdits['Password']     = QLineEdit()
        self.lineEdits['Password'].setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(labels['Username'],            0,0,1,1)
        layout.addWidget(self.lineEdits['Username'],    0,1,1,3)
        layout.addWidget(labels['Password'],            1,0,1,1)
        layout.addWidget(self.lineEdits['Password'],    1,1,1,3)

        login_button = QPushButton('&Log In', clicked=self.checkCredential)
        layout.addWidget(login_button,                  2,3,1,1)

        self.status = QLabel('')
        self.status.setStyleSheet('font-size: 25px; color: red;')
        layout.addWidget(self.status,                   3,0,1,3)

        

        # connect to database
        # self.conntectToDB()

    def checkCredential(self):

        username = self.lineEdits['Username'].text()
        password = self.lineEdits['Password'].text()

        db      = sqlite3.connect(self.database_filepath)
        cursor  = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?",[username])
        cursor_output = cursor.fetchall()
        if len(cursor_output)==0:
            print("Username not present.")
        else:
            target_username, target_password = cursor_output[0]
            if password == target_password:
                print("password is correct.")
                meta_data = {}
                self.main_window = Main_Window(meta_data)
                self.main_window.show()
                self.close()
            else:
                print("incorrect password")
        return None


def main():
    print("This is the main function.")
    app = QApplication(sys.argv)
    loginWindow = LoginWindow()
    loginWindow.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window ...')

if __name__ == '__main__':
    main()