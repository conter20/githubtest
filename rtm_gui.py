import sys
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import QApplication, QBoxLayout, QGridLayout, QInputDialog, QLineEdit, QPushButton, QVBoxLayout, QWidget, QLabel, QTextEdit, QScrollArea,QSpinBox, QRadioButton, QMessageBox,QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from datetime import datetime
from rtm_webscrap import*
import math
# from polum_details_ import run_indetails


en_sentense=""
kr_sentense=""
percent=""
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #defualt setup  
        self.setWindowTitle('Random Test machine')
        self.setGeometry(300, 300, 800, 500)
        self.setStyleSheet("background-color: rgb(10,10,10);")
        self.show()
        
        
        #Part1 Select layout
        self.C_math=QPushButton("English")
        self.C_math.setFont(QFont('Segoe UI',13,QtGui.QFont.Bold))
        self.C_math.setStyleSheet (
            "color: rgb(235,235,235);"
            "background-color: rgb(60,60,60);"
        )
        self.C_math.setFixedHeight(30)
       
        self.C_object=QGridLayout()
        self.C_object.addWidget(self.C_math,0,0)
        self.C_plate=QWidget()
        self.C_plate.setLayout(self.C_object)
        self.C_scr=QScrollArea()
        self.C_scr.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.C_scr.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.C_scr.setWidgetResizable(True)
        self.C_scr.setWidget(self.C_plate)
        self.C_scr.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Expanding)
        self.C_scr.setStyleSheet("QScrollBar"
            "{"
            "background : rgb(50,50,50);"
            "}"
            "QScrollBar::handle"
            "{"
            "background : rgb(10,10,10);"
            "}"
            "QScrollBar::handle::pressed"
            "{"
            "background-color : red;"
            "}"
                             )
        
        
        
        #part 2 about Math
        self.MA_text=QLabel('the title')
        self.MA_text.setFont(QFont('Segoe UI',13,QtGui.QFont.Bold))
        self.MA_text.setStyleSheet(
            "color: rgb(180,180,200);"
            "border-radius: 4px;"
            "border-width: 10px;"
            "background-color:rgb(70,70,70);"                       
        )
        self.MA_answer=QLabel('')
        self.MA_answer.setFont(QFont('Segoe UI',12,QtGui.QFont.Bold))
        self.MA_answer.setStyleSheet(
            "color: rgb(150,200,150);"
            "border-radius: 4px;"
            "border-width: 10px;"
            "background-color:rgb(70,70,70);"                       
        )
        self.MA_s_object=QGridLayout()
        self.MA_s_object.addWidget(self.MA_text,0,0)
        self.MA_s_object.addWidget(self.MA_answer,1,0)
        self.MA_s_plate=QWidget()
        self.MA_s_plate.setLayout(self.MA_s_object)
        self.MA_scr=QScrollArea()
        self.MA_scr.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.MA_scr.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.MA_scr.setWidgetResizable(True)
        self.MA_scr.setWidget(self.MA_s_plate)
        self.MA_scr.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.MA_scr.setStyleSheet("QScrollBar"
            "{"
            "background : rgb(50,50,50);"
            "}"
            "QScrollBar::handle"
            "{"
            "background : rgb(10,10,10);"
            "}"
            "QScrollBar::handle::pressed"
            "{"
            "background-color : red;"
            "}"
                             )
        self.MA_input=QTextEdit()
        self.MA_input.setAcceptRichText(False)
        self.MA_input.setFontPointSize(25)
        self.MA_input.setTextColor(QColor(210,215,210))
        self.MA_input.setCurrentFont(QFont('Segoe UI',11,QtGui.QFont.Bold))
        self.MA_input.textChanged.connect(self.MA_input_textchange)
        self.MA_object=QGridLayout()
        self.MA_object.addWidget(self.MA_scr,0,0)
        self.MA_object.addWidget(self.MA_input,1,0)
        self.MA_object.setRowStretch(0,1)
        self.MA_object.setRowStretch(1,2)
        self.MA_plate=QWidget()
        self.MA_plate.setLayout(self.MA_object)
        
        
        
        #part 3 about Information
        self.IN_object=QGridLayout()
        
        self.IN_percent=QLabel('Bool')
        self.IN_percent.setAlignment(Qt.AlignCenter)
        self.IN_percent.setFont(QFont('Segoe UI',11,QtGui.QFont.Bold))
        self.IN_percent.setStyleSheet(
            "color: rgb(240,240,240);"
            "background-color:rgb(60,60,60)"
        )
        self.IN_num=QLabel('number\n0')
        self.IN_num.setAlignment(Qt.AlignCenter)
        self.IN_num.setFont(QFont('Segoe UI',11,QtGui.QFont.Bold))
        self.IN_num.setStyleSheet(
            "color: rgb(240,240,240);"
            "background-color:rgb(60,60,60)"
        )
        self.IN_cpercent=QLabel('percent\n0.0')
        self.IN_cpercent.setAlignment(Qt.AlignCenter)
        self.IN_cpercent.setFont(QFont('Segoe UI',11,QtGui.QFont.Bold))
        self.IN_cpercent.setStyleSheet(
            "color: rgb(240,240,240);"
            "background-color:rgb(60,60,60)"
        )
        #scrap data
        self.IN_next=QPushButton('Next')
        self.IN_next.setFont(QFont('Segoe UI',12,QtGui.QFont.Bold))
        self.IN_next.setStyleSheet(
            "color:rgb(215,215,215);"
            "background-color:rgb(60,60,60)"
        )
        self.IN_next.clicked.connect(self.IN_textchange)
        
        self.IN_check=QPushButton('Check')
        self.IN_check.setFont(QFont('Segoe UI',12,QtGui.QFont.Bold))
        self.IN_check.setStyleSheet(
            "color:rgb(215,215,215);"
            "background-color:rgb(60,60,60)"
        )
        self.IN_check.clicked.connect(self.IN_encheck)
        
        self.IN_object.addWidget(self.IN_percent,0,0)
        self.IN_object.addWidget(self.IN_num,1,0)
        self.IN_object.addWidget(self.IN_cpercent,2,0)
        self.IN_object.addWidget(self.IN_next,3,0)
        self.IN_object.addWidget(self.IN_check,4,0)
        self.IN_object.setRowStretch(0,1)
        self.IN_object.setRowStretch(1,2)
        self.IN_object.setRowStretch(2,3)
        self.IN_object.setRowStretch(3,4)
        self.IN_object.setRowStretch(4,5)
        self.IN_plate=QWidget()
        self.IN_plate.setLayout(self.IN_object)
        
        
        
        #display all parts
        layout=QGridLayout()
        layout.addWidget(self.C_scr,0,0)
        layout.addWidget(self.MA_plate,0,1)
        layout.addWidget(self.IN_plate,0,2)
        self.setLayout(layout)
        
    #connect to part2 Ma_input-Qtextedit
    def MA_input_textchange(self):
        self.MA_input.setFontPointSize(25)
        self.MA_input.setTextColor(QColor(210,215,210))
        self.MA_input.setCurrentFont(QFont('Segoe UI',11,QtGui.QFont.Bold))
        
    #kr_sentense,en_sentense
    def IN_textchange(self):
        global en_sentense,kr_sentense
        en_sentense,kr_sentense=en_scrap(en_sentense,kr_sentense)
        en_sentense2=en_sentense
        
        i2=math.floor(len(en_sentense)/60)
        for i in range(1,i2+1):
            if len(en_sentense) >=60*i:
                a=en_sentense2[:61*i]
                b=en_sentense2[61*i:]
                en_sentense2=a+"\n"+b
            else:
                break
        self.MA_text.setText(en_sentense2)
        self.MA_answer.setText('')
        self.MA_input.setText('')
        
        
        
    def IN_encheck(self):
        global kr_sentense,percent
        in_text = self.MA_input.toPlainText()
        percent=en_check(in_text,kr_sentense)
        self.IN_cpercent.setText("percent\n"+percent)
        if float(percent)>=90:
            self.IN_percent.setText("Correct")
        else:
            self.IN_percent.setText("Incorrect")
        
        kr_sentense2=kr_sentense
        i2=math.floor(len(kr_sentense)/30)
        for i in range(1,i2+1):
            if len(en_sentense) >=30*i:
                a=kr_sentense2[:31*i]
                b=kr_sentense2[31*i:]
                kr_sentense2=a+"\n"+b
            else:
                break
        self.MA_answer.setText(kr_sentense2)
            
        