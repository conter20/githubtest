from typing_extensions import runtime
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from playsound import playsound
from PyQt5.QtCore import Qt
from datetime import datetime
import threading
import sched
from datetime import datetime
import keyboard
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)
# from Lucdar__Tine__ import Tine_conver

run=True
now=datetime.now()
start_setup=False
conver_setup=False
clocks=''
t=0
text=''
conver_liter_count=0
conver_text=''
talk_acess=True
class ScrollLabel(QScrollArea):
    # constructor
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)
 
        # making widget resizable
        self.setWidgetResizable(True)
 
        # making qwidget object
        content = QWidget(self)
        self.setWidget(content)
 
        # vertical box layout
        lay = QVBoxLayout(content)
 
        # creating label
        self.label = QLabel(content)
 
        # setting alignment to the text
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
 
        # making label multi-line
        self.label.setWordWrap(True)
 
        # adding label to the layout
        lay.addWidget(self.label)

    def setText(self, text):
        # setting text to the label
        self.label.setText(text)

class MyApp(QWidget):
    global run
    global start_setup
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("TINE")
        self.setStyleSheet('background-color: rgb(0,0,0)')

    def TaskA(self):
        global clocks
        global t
        global now
        global run
        global start_setup
        global conver_setup
        global text
        global conver_liter_count
        t=threading.Timer(0.1,self.TaskA)
        t.start()
        #update time
        now=datetime.now()
        hour=now.hour
        minute=now.minute
        if hour>12:
            hour=hour-12
        if minute<10:
            minute='0'+str(minute)
        clocks=str(hour)+':'+str(minute)
        #change clock 
        if start_setup==False:
            self.clock.setText(str(clocks))
        if start_setup==True:
            self.clock.setText('00:00')
        text=self.input.text()
        self.tine()


    def initUI(self):
        global start_setup
        global text
        self.center()
        self.resize(700, 500)

        self.show_conver=ScrollLabel(self)
        self.show_conver.setText('')
        self.show_conver.setFont(QtGui.QFont("Arial Black",20,QtGui.QFont.Bold))
        self.show_conver.setStyleSheet("color: rgb(115,115,115);"
                                "font: 16 10pt Arial Black;")
        self.show_conver.setGeometry(460,20,220,410)

        self.input=QLineEdit(self)
        self.input.move(190,435)
        self.input.setStyleSheet(
        'color:rgb(190,190,190);font-size:20px;')
        self.input.returnPressed.connect(self.continue_conver)

        self.start=QPushButton('Activation',self)
        self.start.clicked.connect(self.setup_button)
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

        self.clock=QLabel('',self)
        self.clock.setFont(QtGui.QFont("Arial Black",40))
        self.clock.setStyleSheet(
            "color: white;"
            "border-style: solid;"
            "border-width:5px;"
            "border-radius: 10px;"
            'border-color: rgb(30,170,30);')
        self.clock.setAlignment(Qt.AlignCenter)
        self.clock.setGeometry(150,20,300,90)
        self.TaskA()

        self.Tine_label=QLabel('',self)
        self.Tine_label.setFont(QtGui.QFont("Arial Black",15))
        self.Tine_label.setStyleSheet(
            "color: white;"
            "border-style: solid;"
            "border-width:3px;"
            "border-radius: 9px;"
            "background-color: rgb(25,25,25);"
            'border-color: rgb(120,120,120);')
        self.Tine_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.Tine_label.setGeometry(150,180,300,250)
        

#Functions
    def setup_button(self):
        global start_setup
        global conver_setup
        global text
        global conver_liter_count
        global conver_text
        work=False
        if start_setup==True and work==False:
            self.start.setText('Activation')
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
            self.clock.setStyleSheet(
                "color: white;"
                "border-style: solid;"
                "border-width:5px;"
                "border-radius: 10px;"
                'border-color: rgb(30,170,30);')
            self.clock.setText(clocks)
            self.input.setText('')
            self.Tine_label.setText('')
            with open('comment_data.txt','w') as f:
                f.write('')
            start_setup=False
            conver_setup=False
            work=True
            
        if start_setup==False and work==False:
            self.start.setText('Disable')
            self.start.setStyleSheet("QPushButton"
                             "{"
                             "color: rgb(210,213,210);"
                             "background-color : rgb(170,30,30);"
                             "border-style: solid;"
                             "border-radius: 8px"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "color: rgb(220,223,220);"
                             "background-color : rgb(130,20,20);"
                             "border-style: solid;"
                             "border-radius: 8px"
                             "}"
                             )
            self.clock.setStyleSheet(
                "color: white;"
                "border-style: solid;"
                "border-width:5px;"
                "border-radius: 10px;"
                'border-color: rgb(170,30,30);')
            self.clock.setText('00:00')
            self.input.setText('')
            self.Tine_label.setText('')
            self.show_conver.setText('')
            with open('comment_data.txt','w') as f:
                f.write('')
            start_setup=True
            conver_setup=False
            work=True
            text=''
            conver_liter_count=0
            conver_text=''

    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def tine(self):
        global text
        global conver_setup
        global start_setup
        global now
        global conver_liter_count
        global conver_text
        if text.lower()=='hey' and start_setup==False and conver_setup==False:
            conver_setup=True
            self.Tine_label.setText('Yep')

            with open('total_comment_data.txt','a') as f:
                f.write('{}-{}-{}-{}[System]:'.format(
            now.year,now.month,now.day,now.hour)+'Yep'+'(conversation start)'+str(conver_liter_count)+"\n")
            conver_text+='[User]'+'Hey'+'\n'+'[Tine]:'+'Yep'+'\n'

            with open('comment_data.txt','a') as f:
                f.write('['+str(conver_liter_count)+']'+'Yep'+"\n")

            self.show_conver.setText(conver_text)
            self.input.setText('')
            print('Yep')
            conver_liter_count+=1

        if conver_setup==True and start_setup==False:
            if ' ' in text:
                pass
                # print(text.split(' '))
            else:
                pass

    def continue_conver(self):
        global now
        global text
        global start_setup
        global conver_setup
        global conver_liter_count
        global conver_text
        global talk_acess
        if start_setup==False and conver_setup==True and talk_acess==True:
            if text.replace(' ','')!='':
                conver_text+='[User]:'+text+'\n'
                self.show_conver.setText(conver_text)

                with open('total_comment_data.txt','a') as f:
                    f.write(
                '{}-{}-{}-{}[User]:'.format(now.year,now.month,now.day,now.hour)+text+'['+str(conver_liter_count)+']'+"\n")
                self.input.setText('')

                with open('comment_data.txt','a') as f:
                    f.write(
                '['+str(conver_liter_count)+']'+text+"\n")
                self.input.setText('')
                conver_liter_count+=1


    def closeEvent(self,event):
        t.cancel()
        event.accept()
        with open('comment_data.txt','w') as f:
            f.write('')






    


