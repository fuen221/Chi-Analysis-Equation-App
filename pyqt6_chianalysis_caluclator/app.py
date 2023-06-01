import sys
import random

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import ( QWidget, QGridLayout, QApplication, QLabel,
                             QMainWindow, QPushButton, QVBoxLayout, QSpinBox, QDoubleSpinBox, QLineEdit)
import design
import controller
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My App")
        self.resize(300,500)

     # Gridlayout with colorsw
        layout = QGridLayout()

        layout.addWidget(design.Color('light grey'), 0, 0, 1, 6)
        layout.addWidget(design.Color('light grey'), 1, 0, 1, 1)
        layout.addWidget(design.Color('light grey'), 1, 1, 1, 1)
        layout.addWidget(design.Color('light grey'), 1, 2, 1, 4)
        layout.addWidget(design.Color('light grey'), 2, 0, 1, 6)
        layout.addWidget(design.Color('light grey'), 3, 0, 1, 6)

        ##### QLabels #####
        # QLabel for title
        title_label = QLabel("Chi  Square ")
        title_label_two = QLabel("   Analysis  Calculator")
        title_label.setBaseSize(100, 200)
        title_label_two.setBaseSize(100, 200)

        #QLabel for observed 
        observed_label = QLabel("Observed")

        #QLabel for expected
        expected_label = QLabel("Expected")

        #QLabel for Chi analysis table number
        chi_analysis_table_number_label = QLabel("Chi Analysis Table Number")

        #QLabel for description
        description_label = QLabel("Calculates whether data is biased or not.")

        ### End of QLabels###

        ###Placment of QLabels 
        
        #Placement of title
        layout.addWidget(title_label, 0, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter.AlignTop)
        layout.addWidget(title_label_two, 0, 1, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter.AlignTop)

        #Placement of observed label
        layout.addWidget(observed_label, 0, 0, alignment=Qt.AlignmentFlag.AlignCenter.AlignBottom)

        #Placment of expected label
        layout.addWidget(expected_label, 0, 1, alignment=Qt.AlignmentFlag.AlignCenter.AlignBottom)

        #Placment of chi analysis table number label
        layout.addWidget(chi_analysis_table_number_label, 0, 2, alignment=Qt.AlignmentFlag.AlignLeft.AlignBottom)

        #Placment of description
        layout.addWidget(description_label, 3, 0, 1, 6)

        ### End of placement of QLabels ###

        # Observed spinboxes
        self.observed_spinbox = QDoubleSpinBox()
        self.observed_spinbox_two = QDoubleSpinBox()
        self.observed_spinbox_three = QDoubleSpinBox()
        self.observed_spinbox_four = QDoubleSpinBox()

        # Placement of oberved spinboxes (left column)
        layout.addWidget(self.observed_spinbox, 1, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignBaseline)
        layout.addWidget(self.observed_spinbox_two, 1, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignBottom)
        layout.addWidget(self.observed_spinbox_three, 1, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.observed_spinbox_four, 2, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignTop)
        
        # Expected Spinboxes
        self.expected_spinbox = QDoubleSpinBox()
        self.expected_spinbox_two = QDoubleSpinBox()
        self.expected_spinbox_three = QDoubleSpinBox()
        self.expected_spinbox_four = QDoubleSpinBox()

        #Observed Spinboxe one altercations
        self.observed_spinbox.setMaximum(900.00)
        self.observed_spinbox.setMaximumWidth(50)
        self.observed_spinbox.setMaximumHeight(50)
        self.observed_spinbox.setValue(1.00)

        #observed spinbox two altercations
        self.observed_spinbox_two.setMaximum(900.00)
        self.observed_spinbox_two.setMaximumWidth(50)
        self.observed_spinbox_two.setMaximumHeight(50)
        self.observed_spinbox_two.setValue(1.0)

        #observed spinbox altercations
        self.observed_spinbox_three.setMaximum(900.00)
        self.observed_spinbox_three.setMaximumWidth(50)
        self.observed_spinbox_three.setMaximumHeight(50)
        self.observed_spinbox_three.setValue(1.0)

        #observed spinbox four altercations
        self.observed_spinbox_four.setMaximum(900.00)
        self.observed_spinbox_four.setMaximumWidth(50)
        self.observed_spinbox_four.setMaximumHeight(50)
        self.observed_spinbox_four.setValue(1.0)

        # Expected Spinboxes altercations
        self.expected_spinbox.setMaximum(900.00)
        self.expected_spinbox.setMaximumWidth(50)
        self.expected_spinbox.setMaximumHeight(50)
        self.expected_spinbox.setValue(1.0)
        
        # Expected spinbox two altercations
        self.expected_spinbox_two.setMaximum(900.00)
        self.expected_spinbox_two.setMaximumWidth(50)
        self.expected_spinbox_two.setMaximumHeight(50)
        self.expected_spinbox_two.setValue(1.0)

        #Expected spinbox three altercations
        self.expected_spinbox_three.setMaximum(900.00)
        self.expected_spinbox_three.setMaximumWidth(50)
        self.expected_spinbox_three.setMaximumHeight(50)
        self.expected_spinbox_three.setValue(1.0)

        #Expected spinbox four altercations
        self.expected_spinbox_four.setMaximum(900.00)
        self.expected_spinbox_four.setMaximumWidth(50)
        self.expected_spinbox_four.setMaximumHeight(50)
        self.expected_spinbox_four.setValue(1.0)

        # Placement of expected spinboxes (middle column)
        layout.addWidget(self.expected_spinbox, 1, 1, alignment=Qt.AlignmentFlag.AlignBaseline)
        layout.addWidget(self.expected_spinbox_two, 1, 1, 1, 2, alignment=Qt.AlignmentFlag.AlignBottom)
        layout.addWidget(self.expected_spinbox_three, 1, 1, 1, 2, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.expected_spinbox_four, 2, 1, 1, 2, alignment=Qt.AlignmentFlag.AlignTop)

        # Chi Table Number Spinbox
        self.chi_table_number_spinbox = QDoubleSpinBox()

        #Chi Table Number Spinbox altercations
        self.chi_table_number_spinbox.setMaximumWidth(50)
        self.chi_table_number_spinbox.setMaximumHeight(50)
        self.chi_table_number_spinbox.setValue(1.0)

        #Placement of Chi Table Number spinbox
        layout.addWidget(self.chi_table_number_spinbox, 1, 2, 1, 2, alignment=Qt.AlignmentFlag.AlignTop)

        #QPushButton for Total
        self.total_button = QPushButton("Total")
        self.total_button.setBaseSize(50,50)

        # Placement of Total QPushButton
        layout.addWidget(self.total_button, 1, 2, 1, 2, alignment=Qt.AlignmentFlag.AlignBaseline)

        #QButton for Results
        self.results_button = QPushButton("Results")

        #Placement of results button
        layout.addWidget(self.results_button, 2, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignBottom)

        # QLineEdit for results window
        self.results_window = QLineEdit()
        self.results_window.setMaximumWidth(100)
        self.results_window.setMaximumHeight(50)

        #Alignment of results_window
        layout.addWidget(self.results_window, 2, 2, 1, 2, alignment=Qt.AlignmentFlag.AlignBottom)

        # QLineEdit for total window
        self.total_window = QLineEdit()
        self.total_window.setMaximumWidth(200)
        self.total_window.setMaximumHeight(50)

        #Alignment of total_window
        layout.addWidget(self.total_window, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter.AlignBottom)
        
        #add a calculate function
        self.results_button.clicked.connect(self.calculate_results)
        self.total_button.clicked.connect(self.calculate_total)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def calculate_results(self):
        """Caculate Chi Analysis Results"""
        #get expected
        expected_one = self.expected_spinbox.value()
        expected_two = self.expected_spinbox_two.value()
        expected_three = self.expected_spinbox_three.value()
        expected_four = self.expected_spinbox_four.value()

        #get observed
        observed_one = self.observed_spinbox.value()
        observed_two = self.observed_spinbox_two.value()
        observed_three = self.observed_spinbox_three.value()
        observed_four = self.observed_spinbox_four.value()

        #get analysis chi table number
        number = self.chi_table_number_spinbox.value()
        #get resutls
        results = controller.get_results(expected_one,expected_two,expected_three, expected_four,
                                         observed_one,observed_two,observed_three,observed_four,number)

        #Display results
        self.results_window.setText(results)

    def calculate_total(self):
        #get expected
        expected_one = self.expected_spinbox.value()
        expected_two = self.expected_spinbox_two.value()
        expected_three = self.expected_spinbox_three.value()
        expected_four = self.expected_spinbox_four.value()

        #get observed
        observed_one = self.observed_spinbox.value()
        observed_two = self.observed_spinbox_two.value()
        observed_three = self.observed_spinbox_three.value()
        observed_four = self.observed_spinbox_four.value()

        #get total
        total = controller.get_total(expected_one, expected_two, expected_three, expected_four, observed_one, 
                                     observed_two, observed_three, observed_four)
        
        #display total
        self.total_window.setText(str(total))
    

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()
