import sys
from PyQt5.QtGui import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from pendaftaran import*

class MainForm (QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 100)
        self.move(300, 300)
        self.setWindowTitle('Kuis Pemograman GUI')
        self.us = QLabel('Username')
        self.ps = QLabel('Password')
        self.NameEdit = QLineEdit()
        self.PsEdit = QLineEdit()
        self.PsEdit.setEchoMode(QLineEdit.Password)
        self.Login=QPushButton('Login')
        self.Clear=QPushButton('Clear')
        btx =QGridLayout()
        btx.addWidget(self.us)
        btx.addWidget(self.NameEdit, 0,1,1,2)
        btx.addWidget(self.ps)
        btx.addWidget(self.PsEdit, 1,1,1,2)
        btx.addWidget(self.Login, 2,1)
        btx.addWidget(self.Clear, 2,2)
        self.setLayout(btx)

        self.Login.clicked.connect(self.buttonClick)
        self.Clear.clicked.connect(self.buttonClick1)

    def buttonClick(self):
        user = self.NameEdit.text()
        pw = self.PsEdit.text()

        if not user or not pw :
            QMessageBox.information(self,'Perhatian','Username atau password tidak boleh kosong')
        else:
            if user == '17104013' and pw =='123456789':
                self.form = pendaftaran()
                self.form.show()
                self.close()
            else:
                QMessageBox.information(self,'Perhatian','Username atau password Salah')

    def buttonClick1 (self):
            self.NameEdit.clear()
            self.PsEdit.clear()
			
if __name__ =='__main__':
        a =QApplication(sys.argv)
        form = MainForm()
        form.show()

        a.exec_()
