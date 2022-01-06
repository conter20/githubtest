import sys
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import QApplication, QBoxLayout, QGridLayout, QInputDialog, QLineEdit, QPushButton, QVBoxLayout, QWidget, QLabel, QTextEdit, QScrollArea,QSpinBox, QRadioButton, QMessageBox
from PyQt5.QtCore import Qt
import re
from PyQt5 import QtGui
from datetime import datetime
import threading


# from polum_details_ import run_indetails



schedule_content=''
schedule_count=0
stitle=''
scontent=''
hours=[]
minutes=[]
TaskA=False
t=0

    
class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #input box
        self.TaskA()
        self.lbl1 = QLabel('Write your schedule content')
        self.lbl1.setFont(QtGui.QFont("Arial Black",10))
        self.lbln1=QLineEdit(self)
        self.te = QTextEdit()
        self.te.setAcceptRichText(False)
        self.te.setFontPointSize(20)
        self.te.setTextColor(QColor(10,15,10))
        self.te.setCurrentFont(QFont("Noto Sans",20))
        self.te.textChanged.connect(self.text_changed)
        
        #add new schedule
        self.addbutton=QPushButton('Add new schedule')
        self.addbutton.clicked.connect(self.clicked_addbutton)

        #set alarm hour
        self.lbl2 = QLabel('Hour')
        self.lbl2.setFont(QtGui.QFont("Arial Black",10))
        self.set_htime = QSpinBox()
        self.set_htime.setFont(QtGui.QFont("Arial Black",8))
        self.set_htime.setMinimum(1)
        self.set_htime.setMaximum(24)

        #set alarm minute
        self.lbl3 = QLabel('Minute')
        self.lbl3.setFont(QtGui.QFont("Arial Black",10))
        self.set_mtime = QSpinBox()
        self.set_mtime.setFont(QtGui.QFont("Arial Black",8))
        self.set_mtime.setMinimum(0)
        self.set_mtime.setMaximum(59)
        
        #background feedback on-off
        self.feedback = QRadioButton('Background Feedback', self)
        self.feedback.setFont(QtGui.QFont("Arial Black",10))
        self.feedback.setChecked(False)
        
        #show schedule list
        self.lbl4 = QLabel('Your Schedule list')
        self.lbl4.setFont(QtGui.QFont("Arial Black",10))
        self.scr = QScrollArea() 
        self.scr.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scr.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scr.setWidgetResizable(True)
        
        #schedule title
        self.lblt=QLabel('None')
        self.lblt.setFont(QtGui.QFont("Arial Black",10))
        
        #edit schedule
        self.editbutton=QPushButton('None')
        self.editbutton.clicked.connect(self.edit_schedule)
        self.editbutton.setDisabled(True)
        
        #schedule content
        self.lbln2=QTextEdit(self)
        self.lbln2.setAcceptRichText(False)
        self.lbln2.setFontPointSize(20)
        self.lbln2.setTextColor(QColor(10,15,10))
        self.lbln2.setCurrentFont(QFont("Noto Sans",15))
        self.lbln2.textChanged.connect(self.text_changed2)
        
        
        #include scroll widget contents
        self.scrlayout = QGridLayout()
        self.lbl5=QWidget()
        #get file data
        with open('polum_schedulefile_.txt','r') as f:
            global schedule_content
            global schedule_count
            schedule_content=f.readlines()
            schedule_count=len(schedule_content)/5
            schedule_count=float(schedule_count)
            
        #show schedule contents
        for i in range(1,int(schedule_count+1)):
            self.object = QLabel(schedule_content[5*i-2])#default label
            self.object.setFont(QtGui.QFont("Arial Black",9))
            self.checkbutton = QPushButton("[{}]Details".format(i),self)#checkbox
            self.checkbutton.clicked.connect(self.check_schedule)
            self.scrlayout.addWidget(self.object,i,0)#gridbox replace
            self.scrlayout.addWidget(self.checkbutton,i,1)#gridpox replace
        self.lbl5.setLayout(self.scrlayout)
        self.scr.setWidget(self.lbl5)
        

        #setting grid box
        layout = QGridLayout()
        layout.addWidget(self.addbutton,3,1)#able to change
        layout.addWidget(self.lbl4,1,1)
        layout.addWidget(self.lbl1,1,2)
        layout.addWidget(self.lblt,1,0)
        layout.addWidget(self.lbln2,2,0)
        layout.addWidget(self.editbutton,3,0)
        layout.addWidget(self.lbln1,3,2)
        layout.addWidget(self.te,2,2)
        layout.addWidget(self.scr,2,1)#scr infor able to change
        layout.addWidget(self.lbl2,2,3)
        layout.addWidget(self.set_htime,2,4)
        layout.addWidget(self.lbl3,2,5)
        layout.addWidget(self.set_mtime,2,6)
        layout.addWidget(self.feedback,2,7)
        self.setLayout(layout)
        
        #window setting
        self.setWindowTitle('schedule_assistant')
        self.setGeometry(800, 450, 1300, 550)
        self.show()

    #label text change
    def text_changed(self):
        self.te.setFontPointSize(20)
        self.te.setTextColor(QColor(10,15,10))
        self.te.setCurrentFont(QFont("Noto Sans",20))
        
    def text_changed2(self):
        self.lbln2.setFontPointSize(20)
        self.lbln2.setTextColor(QColor(10,15,10))
        self.lbln2.setCurrentFont(QFont("Noto Sans",15))

    #add newschedules
    def clicked_addbutton(self):
        global hours
        global minutes
        global schedule_content
        #save values
        hvalue=self.set_htime.value()
        mvalue=self.set_mtime.value()
        background=self.feedback.isChecked()
        title=self.lbln1.text()
        content=self.te.toPlainText()

        if len(title)<=30 and len(content)<=300:
            global schedule_content
            global schedule_count
            schedule_count=schedule_count+1
            #reset
            self.set_htime.setValue(1)
            self.set_mtime.setValue(0)
            self.feedback.setChecked(False)
            self.lbln1.setText('')
            self.te.setText('')
            
            #write in file
            with open('polum_schedulefile_.txt','a') as f:
                f.write(str(hvalue)+'\n')
                f.write(str(mvalue)+'\n')
                f.write(str(background)+'\n')
                f.write(title+'\n')
                f.write(content+'\n')
            #import datas
            with open('polum_schedulefile_.txt','r') as f:
                global schedule_content
                global hours
                global minutes
                schedule_content=f.readlines()
                schedule_count=len(schedule_content)/5
                schedule_count=float(schedule_count)

                a=1
                count=len(schedule_content)/5
                while a<=count:
                    hours.append(schedule_content[5*a-5])
                    minutes.append(schedule_content[5*a-4])
                    if a==count:
                        print('True!')
                    a=a+1

            #update widget
            self.object = QLabel("{}".format(title))
            self.object.setFont(QtGui.QFont("Arial Black",9))
            self.checkbutton = QPushButton("[{}]Details".format(int(schedule_count)),self)
            self.checkbutton.clicked.connect(self.check_schedule)
            self.scrlayout.addWidget(self.object,int(schedule_count),0)
            self.scrlayout.addWidget(self.checkbutton,int(schedule_count),1)
            self.lbl5.setLayout(self.scrlayout)
            self.scr.setWidget(self.lbl5)
            self.lbl5.repaint()
            self.scr.repaint()
            
            a=1
            count=len(schedule_content)/5
            while a<=count:
                hours.append(schedule_content[5*a-5])
                minutes.append(schedule_content[5*a-4])
                a=a+1
            
            
                

        #if title over text content doesn't over text
        elif len(title)>=30 and len(content)<=300:
            buttonReply = QMessageBox.question(
            self, 'Alert', "    title limit excess 30   ",
            QMessageBox.Yes
            )


        #if title doesn't over text content over text
        elif len(title)<=30 and len(content)>=300:
            buttonReply = QMessageBox.question(
            self, 'Alert', "    content limit excess 300    ",
            QMessageBox.Yes
            )
 
                
        #if title over text content over text
        elif len(title)>=30 and len(content)>=300:
            buttonReply = QMessageBox.question(
            self, 'Alert', "title limit excess 30,content limit excess 300",
            QMessageBox.Yes
            )
    
    def check_schedule(self):
        global stitle
        global scontent
        #update contents
        with open('polum_schedulefile_.txt','r') as f:
            schedule_content=f.readlines()
            schedule_count=len(schedule_content)/5
            schedule_count=float(schedule_count)
        #import text datas
        btn = self.sender()
        #import text content
        btn=btn.text()
        #save number
        num=int(''.join(list(filter(str.isdigit, btn))))
        #import titles
        stitle=schedule_content[5*num-2]
        stitle=stitle[:-1]
        #import content
        scontent=schedule_content[5*num-1]
        scontent=scontent[:-1]
        
        self.lblt.setText('[{}]'.format(num)+stitle)
        self.lbln2.setText(scontent)
        self.editbutton.setText('edit text [{}]'.format(num))
        self.editbutton.setEnabled(True)
        
    def edit_schedule(self):
        global t
        btn=self.sender()
        btn=btn.text()
        t.cancel()
        num=int(''.join(list(filter(str.isdigit,btn))))
        text=self.lbln2.toPlainText()
        if len(text)<=300:
            with open('polum_schedulefile_.txt','r') as f:
                lines=f.readlines()
                lines[5*num-1]=text+'\n'
            with open('polum_schedulefile_.txt','w') as w:
                w.writelines(lines)
                
        elif  len(text)>=300:
            buttonReply = QMessageBox.question(
            self, 'Alert', "    content limit excess 300   ",
            QMessageBox.Yes
            )
            
    def TaskA(self):
        global hours
        global minutes
        global TaskA
        global schedule_content
        global t
        t=threading.Timer(4,self.TaskA)
        t.start()
        time=datetime.now()
        hour=time.hour
        minute=time.minute
        print('#########')
        print('[hour]'+str(hour))
        print('[minute]'+str(minute))
        if TaskA==False:
            with open('polum_schedulefile_.txt','r') as f:
                a=1
                count=len(schedule_content)/5
                while a<=count:
                    hours.append(schedule_content[5*a-5])
                    minutes.append(schedule_content[5*a-4])
                    if a==count:
                        TaskA=True
                        print('True!')
                    a=a+1
                        
        a=1
        count=len(schedule_content)/5
        
        if TaskA==True:
            while a<=count:
                if (hours[a-1])[:-1]==str(hour) and (minutes[a-1])[:-1]==str(minute):
                    print('match')
                else:
                    pass
                a=a+1

            
        


        
        

        

        
        
        

        
        