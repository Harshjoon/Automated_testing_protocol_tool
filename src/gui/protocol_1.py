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
    QDialogButtonBox,
    QMessageBox,
    QComboBox
)


class Protocol_1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.protocol_data_file = "../../protocols/protocols_1/protocols.json"

        self.window_height      = 800
        self.window_width       = 700
        
        self.initUI()

    def initUI(self):
        
        self.setFixedSize(QSize(self.window_height, self.window_width))
        
        y1 = 20
        self.main_heading_label = QLabel("Main heading", self)
        self.main_heading_label.setStyleSheet("QLabel{font-size: 14pt;font-weight: bold}")
        x,y = 50,y1
        self.main_heading_label.move(x,y)
        self.main_heading_label.adjustSize()
        y1 += 30
        self.sub_heading_label  = QLabel("Sub heading", self)
        self.sub_heading_label.setStyleSheet("QLabel{font-size: 12pt;font-weight: bold}")
        x,y = 50,y1
        self.sub_heading_label.move(x,y)
        self.sub_heading_label.adjustSize()
        y1 += 30
        self.requirement_id_label = QLabel("Requirement id here", self)
        self.requirement_id_label.setStyleSheet("QLabel{font-size: 12pt}")
        x,y = 50,y1
        self.requirement_id_label.move(x,y)
        self.requirement_id_label.adjustSize()
        y1 += 20
        self.pre_requisites_label = QLabel("Pre requisites label", self)
        self.pre_requisites_label.setStyleSheet("QLabel{font-size: 12pt}")
        x,y = 50,y1
        self.pre_requisites_label.move(x,y)
        self.pre_requisites_label.adjustSize()
        y1 += 20
        self.test_objective_label = QLabel("Test objective label", self)
        self.test_objective_label.setStyleSheet("QLabel{font-size: 12pt}")
        x,y = 50,y1
        self.test_objective_label.move(x,y)
        self.test_objective_label.adjustSize()
        y1 += 20
        self.test_number_label  = QLabel("Test Number: ", self)
        self.test_number_label.setStyleSheet("QLabel{font-size: 12pt}")
        x,y = 50,y1
        self.test_number_label.move(x,y)
        self.test_number_label.adjustSize()
        y1 += 40
        self.test_case_methodology_label = QLabel("Test case methodology: ", self)
        self.test_case_methodology_label.setStyleSheet("QLabel{font-size: 12pt}")
        x,y = 50,y1
        self.test_case_methodology_label.move(x,y)
        self.test_case_methodology_label.adjustSize()
        y1 += 60
        self.expected_results_label      = QLabel("Expected results: ", self)
        self.expected_results_label.setStyleSheet("QLabel{font-size: 12pt}")
        x,y = 50,y1
        self.expected_results_label.move(x,y)
        self.expected_results_label.adjustSize()

        self.temp_actual_results_list = [
            "As expected",
            "Actual_results_1",
            "Actual_results_2",
            "Others"
        ]
        self.temp_results_list        = [
            "Pass",
            "Fail",
            "N/A",
            "Others"
        ]

        #y1 += 60
        self.actual_results_list    = self.temp_actual_results_list
        self.results_list           = self.temp_results_list

        self.actual_results_combobox = QComboBox(self)
        for i in self.actual_results_list:
            self.actual_results_combobox.addItem(i)
        x,y = 300,y1
        self.actual_results_combobox.move(x,y)

        y1 += 60
        self.results_label      = QLabel("Results: ", self)
        self.results_label.setStyleSheet("QLabel{font-size: 12pt}")
        x,y = 50,y1
        self.results_label.move(x,y)
        self.results_label.adjustSize()

        #y1 += 60
        self.results_combobox        = QComboBox(self)
        for i in self.results_list:
            self.results_combobox.addItem(i)
        x,y = 300,y1
        self.results_combobox.move(x,y)

        return None



