#!/usr/bin/python

import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QRegularExpressionValidator, QPixmap
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

        self.window_height      = 700
        self.window_width       = 800
        
        self.initUI()

    def initUI(self):
        
        self.setFixedSize(QSize(self.window_width, self.window_height))
        
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
        #x,y = 50,y1
        x,y = 50,90
        self.requirement_id_label.move(x,y)
        self.requirement_id_label.adjustSize()
        y1 += 20
        self.pre_requisites_label = QLabel("Pre requisites label", self)
        self.pre_requisites_label.setStyleSheet("QLabel{font-size: 12pt}")
        #x,y = 50,y1
        x,y = 50,120
        self.pre_requisites_label.move(x,y)
        self.pre_requisites_label.adjustSize()
        y1 += 20
        self.test_objective_label = QLabel("Test objective label", self)
        self.test_objective_label.setStyleSheet("QLabel{font-size: 12pt}")
        #x,y = 50,y1
        x,y = 50,150
        self.test_objective_label.move(x,y)
        self.test_objective_label.adjustSize()
        y1 += 20
        self.test_number_label  = QLabel("Test Number: ", self)
        self.test_number_label.setStyleSheet("QLabel{font-size: 12pt}")
        #x,y = 50,y1
        x,y = 50,220
        self.test_number_label.move(x,y)
        self.test_number_label.adjustSize()
        y1 += 40
        self.test_case_methodology_label = QLabel("Test case methodology: ", self)
        self.test_case_methodology_label.setStyleSheet("QLabel{font-size: 12pt}")
        #x,y = 50,y1
        x,y = 50,250
        self.test_case_methodology_label.move(x,y)
        self.test_case_methodology_label.adjustSize()

        # temp image path
        self.temp_image_path = "../../protocols/protocols_1/images/1.png"
        self.pixmap          = QPixmap(self.temp_image_path)
        self.image_label     = QLabel(self)
        w,h = 200,100
        self.image_label.setFixedSize(QSize(w,h))
        self.image_label.setPixmap(self.pixmap.scaled(w, h, Qt.AspectRatioMode.KeepAspectRatio))
        #x,y = 500,y1
        x,y = 500,250
        self.image_label.move(x,y)
        #self.image_label.setScaledContents(True)
        self.image_label.adjustSize()

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

        y1 += 60
        self.expected_results_label      = QLabel("Expected results: ", self)
        self.expected_results_label.setStyleSheet("QLabel{font-size: 12pt}")
        #x,y = 50,y1
        x,y = 50, self.window_height - 160
        self.expected_results_label.move(x,y)
        self.expected_results_label.adjustSize()

        #y1 += 60
        self.actual_results_list    = self.temp_actual_results_list
        self.results_list           = self.temp_results_list

        self.actual_results_combobox = QComboBox(self)
        for i in self.actual_results_list:
            self.actual_results_combobox.addItem(i)
        #x,y = 300,y1
        x,y = 300, self.window_height - 160
        self.actual_results_combobox.move(x,y)

        y1 += 60
        self.results_label      = QLabel("Results: ", self)
        self.results_label.setStyleSheet("QLabel{font-size: 12pt}")
        #x,y = 50,y1
        x,y = 50, self.window_height - 120
        self.results_label.move(x,y)
        self.results_label.adjustSize()

        #y1 += 60
        self.results_combobox        = QComboBox(self)
        for i in self.results_list:
            self.results_combobox.addItem(i)
        #x,y = 300,y1
        x,y = 300, self.window_height - 120
        self.results_combobox.move(x,y)


        self.remarks_label           = QLabel("Remarks", self)
        self.remarks_label.setStyleSheet("QLabel{font-size: 12pt}")
        x,y = 450, self.window_height - 160
        self.remarks_label.move(x,y)
        self.remarks_label.adjustSize()

        self.remarks_box             = QLineEdit(self)
        w,h = 200,80
        self.remarks_box.setFixedSize(QSize(w,h))
        x,y = 550, self.window_height - 160
        self.remarks_box.move(x,y)
        self.remarks_box.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.remarks_box.adjustSize()

        self.previous_button    = QPushButton("Previous", self)
        x,y = 150, self.window_height - 60
        self.previous_button.move(x,y)

        self.next_button        = QPushButton("Next", self)
        x,y = 350, self.window_height - 60
        self.next_button.move(x,y)

        self.finish_button    = QPushButton("Finish", self)
        x,y = 550, self.window_height - 60
        self.finish_button.move(x,y)

        self.finish_button.clicked.connect(self.on_finish_clicked)

        return None
    
    def on_finish_clicked(self):
        
        self.close()
        
        return None
    

def main():
    print("This is the main function.")
    app = QApplication(sys.argv)
    # set app stylesheet
    # app.setStyleSheet()
    loginWindow = Protocol_1()
    loginWindow.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window ...')

if __name__ == '__main__':
    main()
