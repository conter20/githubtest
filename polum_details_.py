import sys
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import QApplication, QGridLayout, QInputDialog, QLineEdit, QPushButton, QVBoxLayout, QWidget, QLabel, QTextEdit, QScrollArea,QSpinBox, QRadioButton, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import re
# from polum_ui_ import scontent,stitle

def run_indetails():
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())

class App(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.clock=QLabel('p',self)
        self.clock.setFont(QtGui.QFont("Arial Black",40))
        self.clock.setStyleSheet(
            "color: white;")
        self.clock.setAlignment(Qt.AlignCenter)
        self.clock.setGeometry(10,10,300,90)

        self.start=QPushButton('Activation',self)
        self.start.setFont(QtGui.QFont("Arial Black",11,QtGui.QFont.Bold))
        self.start.setStyleSheet("QPushButton"
                             "{"
                             "color: rgb(210,213,210);"
                             "background-color : rgb(30,170,30);"
                             "border-style: solid;"
                            #  "border-width: 5px;"
                            #  "border-color: rgb(70,73,70);"
                             "border-radius: 8px"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "color: rgb(220,223,220);"
                             "background-color : rgb(20,130,20);"
                             "border-style: solid;"
                            #  "border-width: 5px;"
                            #  "border-color: rgb(90,93,90);"
                             "border-radius: 8px"
                             "}"
                             )
        self.start.setGeometry(150,100,300,75)
        
        
