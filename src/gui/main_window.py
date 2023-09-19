#!/usr/bin/python

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
    QSizePolicy,
    QComboBox
)

# similarly import all protocols
from protocol_1 import Protocol_1

class Main_Window(QMainWindow):
    def __init__(self, meta_data):
        super().__init__()

        self.meta_data = meta_data
        self.setWindowTitle('Main Window')
        # set icon
        #self.setWindowIcon(QIcon(''))
        self.window_width, self.window_height = 800,700
        self.setFixedSize(self.window_width, self.window_height)

        self.initUI()

    def initUI(self):

        y1 = 20
        # show information
        self.information_label = QLabel("General Information", self)
        self.information_label.setStyleSheet("QLabel{font-size: 12pt;font-weight: bold}")
        x,y = 20,y1
        self.information_label.move(x,y)
        self.information_label.adjustSize()
        y1 += 40
        self.tester_name_label = QLabel("Tester_name", self)
        x,y = 20,y1
        self.tester_name_label.move(x,y)
        self.tester_name_label.adjustSize()

        y1 += 50
        self.protocols_heading_label = QLabel("Select Protocols", self)
        self.protocols_heading_label.setStyleSheet("QLabel{font-size: 12pt;font-weight: bold}")
        x,y = 20,y1
        self.protocols_heading_label.move(x,y)
        self.protocols_heading_label.adjustSize()

        self.protocols = {
            "Protocol_1" : Protocol_1(),
            "Protocol_2" : None,
            "Protocol_3" : None,
            "Protocol_4" : None,
        }
        y1 += 40
        self.protocols_combobox = QComboBox(self)
        for key in self.protocols.keys():
            self.protocols_combobox.addItem(key)
        x,y = 20,y1
        self.protocols_combobox.move(x,y)

        y1 += 100
        self.start_protocols_button = QPushButton("Start Protocols", self)
        x,y = 100,y1
        self.start_protocols_button.move(x,y)


        # connect signals and slots
        self.start_protocols_button.clicked.connect(self.start_protocols)

        return None
    
    def start_protocols(self):

        # read selected protocol
        self.selected_protocol          = self.protocols_combobox.currentText()
        self.selected_protocol_index    = self.protocols_combobox.currentIndex()

        print("selected protocol", self.selected_protocol)
        print("selected protocol index", self.selected_protocol_index) 

        # open the selected protocol class
        self.protocols[self.selected_protocol].show()
        #self.hide()

        return None


