from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from ui_design_python import Ui_Form
from Score_Prediction_Plus import predict_score
from Score_Prediction_Plus import teams
from Score_Prediction_Plus import cities
from PyQt5.QtGui import QGuiApplication
from PySide6.QtGui import QIntValidator
import sys

from separate import plese



app = QGuiApplication(sys.argv)



class Widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.count=1
        int_validator = QIntValidator()
        self.lineEdit.setValidator(int_validator)
        self.lineEdit_2.setValidator(int_validator)
        self.lineEdit_3.setValidator(int_validator)
        self.lineEdit_4.setValidator(int_validator)
        self.comboBox.addItems(teams)
        self.comboBox_2.addItems(teams)
        self.comboBox_3.addItems(cities)
        self.pushButton.clicked.connect(self.read_input)
        self.comboBox.currentTextChanged.connect(self.batting_team)

        
        
       
        
        
    
    def batting_team(self,data):
        self.comboBox_2.clear()
        self.comboBox_2.addItems(teams)
        self.comboBox_2.insertItem(0,"Select Bowling Team")
        self.comboBox_2.setCurrentIndex(0)

        if data !='Select Batting Team':
            self.comboBox_2.clear()
            for i in teams:
                 if i !=data:
                      self.comboBox_2.addItem(i)
                      
            
            self.comboBox_2.insertItem(0,"Select Bowling Team")
            self.comboBox_2.setCurrentIndex(0)
       



          
    def read_input(self):
       

        line1 = int(self.lineEdit.text())
        line2 = int(self.lineEdit_2.text())
        line3 = int(self.lineEdit_3.text())
        line4 = int(self.lineEdit_4.text())

        cmb1 = self.comboBox.currentText()
        cmb2 = self.comboBox_2.currentText()
        cmb3 = self.comboBox_3.currentText()

        

       
        
        
        
        predicted_score=predict_score(line1,line2,line3,line4, cmb1,cmb2,cmb3)
        if predicted_score <=line1:
            predicted_score += 20

            

        flags = ['Afghanistan.png','Australia.png','Bangladesh.png','England.png','India.png','New Zealand.png','Pakistan.png','South Africa.png','Sri Lanka.png','West Indies.png']
        
        for flag in flags:
            if cmb1.lower() in flag.lower():
                cou1 = flag
                

            if cmb2.lower() in flag.lower():
                cou2 = flag
                

            

        if self.count==1:

                plese.qmap(self,cou1,cou2)
                self.label_8.setText(str(predicted_score))
                self.count+=1

        elif self.count==2:

                plese.qmap2(self,cou1,cou2)
                self.label_9.setText(str(predicted_score))
                self.count+=1

        elif self.count==3:

                plese.qmap3(self,cou1,cou2)
                self.label_10.setText(str(predicted_score))
                self.count+=1
            
        else:
                plese.qmap(self,cou1,cou2)
                self.label_8.setText(str(predicted_score))
                self.count=2

        


        



      

        


