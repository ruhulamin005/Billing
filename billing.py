


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3

#Creating database & connecting it

conn = sqlite3.connect('smart_billing.db')

c= conn.cursor()

#Creating Tables

c.execute("""CREATE TABLE if not exists 
    bill_info(bill_id INTEGER,cust_name text,cust_phone text,service text,additional text,amount real,notes text)

    """)
c.execute("""CREATE TABLE if not exists 
    combo_items(items text)

    """)




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 615)
        MainWindow.setStyleSheet("#list{\n"
"background-color:#FFFFFF;\n"
"border-radius:20px;\n"
"\n"
"}\n"
"#admin{\n"
"\n"
"background:#9DC98A;\n"
"\n"
"}\n"
"\n"
"\n"
"#centralwidget{\n"
"\n"
"background-color:#FFFFFF;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"#frame{\n"
"\n"
"background:#9DC98A;\n"
"\n"
"border-radius:20px;\n"
"}\n"
"\n"
"#frame_2{\n"
"\n"
"background:#9DC98A;\n"
"\n"
"border-radius:20px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background:#FFFFFF;\n"
"border-radius:15px;\n"
"}\n"
"QLabel{\n"
"\n"
"font-family:century gothic;\n"
"font-size:24px;\n"
"border-radius:15px;    \n"
"}\n"
"QComboBox{\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"color:black;\n"
"border-radius:15px;\n"
"background:pink;\n"
"}\n"
"QPushButton{\n"
"\n"
"background-color:#CCF2FF;\n"
"font-size:24px;\n"
"border-radius:15px;\n"
"color:black;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 0, 241, 31))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(1)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 50, 361, 511))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        combo = self.combo = QtWidgets.QComboBox(self.frame)
        self.combo.setGeometry(QtCore.QRect(10, 130, 341, 31))
        self.combo.setObjectName("combo")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(140, 100, 91, 21))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(1)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.add = QtWidgets.QPushButton(self.frame , clicked = lambda:self.add_it())
        self.add.setGeometry(QtCore.QRect(10, 310, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.remove = QtWidgets.QPushButton(self.frame, clicked = lambda:self.remove_it())
        self.remove.setGeometry(QtCore.QRect(10, 360, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.remove.setFont(font)
        self.remove.setObjectName("remove")
        self.save = QtWidgets.QPushButton(self.frame, clicked = lambda:self.save_it())
        self.save.setGeometry(QtCore.QRect(10, 410, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.save.setFont(font)
        self.save.setObjectName("save")
        self.print = QtWidgets.QPushButton(self.frame, clicked = lambda:self.print_it())
        self.print.setGeometry(QtCore.QRect(10, 460, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.print.setFont(font)
        self.print.setObjectName("print")
        self.name = QtWidgets.QLineEdit(self.frame)
        self.name.setGeometry(QtCore.QRect(10, 20, 341, 31))
        self.name.setObjectName("name")
        self.phone = QtWidgets.QLineEdit(self.frame)
        self.phone.setGeometry(QtCore.QRect(10, 60, 341, 31))
        self.phone.setObjectName("phone")
        self.additional = QtWidgets.QLineEdit(self.frame)
        self.additional.setGeometry(QtCore.QRect(10, 170, 341, 31))
        self.additional.setObjectName("additional")
        self.amount = QtWidgets.QLineEdit(self.frame)
        self.amount.setGeometry(QtCore.QRect(10, 210, 341, 31))
        self.amount.setObjectName("amount")
        self.notes = QtWidgets.QLineEdit(self.frame)
        self.notes.setGeometry(QtCore.QRect(10, 250, 341, 51))
        self.notes.setObjectName("notes")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(390, 50, 391, 511))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame2label = QtWidgets.QLabel(self.frame_2)
        self.frame2label.setGeometry(QtCore.QRect(100, 0, 181, 31))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(1)
        self.frame2label.setFont(font)
        self.frame2label.setObjectName("frame2label")
        self.list = QtWidgets.QListWidget(self.frame_2)
        self.list.setGeometry(QtCore.QRect(15, 41, 361, 461))
        self.list.setObjectName("list")
        self.admin = QtWidgets.QPushButton(self.centralwidget)
        self.admin.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.admin.setFont(font)
        self.admin.setObjectName("admin")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #adding item to combo
        #"1. New Tires "
         #               ,"2. Oil services","3. Oil filter change","4. Diesel filter change ",
          #                  "5. Grease ",
          #              "6. Air filter cleane",
           #             "7. Engine clean With Diesel",
            #                "8. Air check ",
             #           "9. Bolt",
              #          "10. Bolt  change ",
               #         "11. Pancher",
              #          "12. Pancher and patch fitting",
              #          "13. New tube",
               #         "14. New tube fitting",
               #         "15. Ring ",
               #         "16. Ring.  Balp change",
               #         "17. Tire chang"

        combo.addItem("1. New Tires")
        combo.addItem("2. Oil services ")
        combo.addItem("3. Oil filter change ")
        combo.addItem("4. Diesel filter change")
        combo.addItem("5. Grease")
        combo.addItem("6. Air filter clean")
        combo.addItem("7. Engine clean With Diesel ")
        combo.addItem("8. Air check")
        combo.addItem("9. Bolt")
        combo.addItem("10. Bolt  change ")
        combo.addItem("11. Pancher ")
        combo.addItem("12. Pancher and patch fitting")
        combo.addItem("13. New tube ")
        combo.addItem("14. New tube fitting ")
        combo.addItem("15. Ring ")
        combo.addItem("16. Ring.  Balp change")
        combo.addItem("17. Tire chang ")

        self.combo.activated[str].connect(self.onSelected)
        



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def onSelected(self, combo_text):
        #print(combo_text)
        pass


    def add_it(self):
        name = self.name.text()

        if not name:
            pass
        else:
            self.list.addItem(name)
            self.name.setText("")


        phone = self.phone.text()

        if not phone:
            pass
        else:
            self.list.addItem(phone)
            self.phone.setText("")

        amount = self.amount.text()
        self.list.addItem(amount)

        additional = self.additional.text()
        self.list.addItem(additional)

        notes = self.notes.text()
        self.list.addItem(notes)

        

        choosen = self.combo.currentText()
        self.list.addItem(choosen)

        bill = name + "\n" +phone + "\n"+choosen+"\n"+amount+"\n"+additional+"\n"+notes
        self.list.addItem(bill)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Smart Billing System"))
        self.combo.setPlaceholderText(_translate("MainWindow", "Service or Product"))
        self.label_2.setText(_translate("MainWindow", "Service"))
        self.add.setText(_translate("MainWindow", "ADD"))
        self.remove.setText(_translate("MainWindow", "DELETE"))
        self.save.setText(_translate("MainWindow", "SAVE"))
        self.print.setText(_translate("MainWindow", "PRINT"))
        self.name.setPlaceholderText(_translate("MainWindow", "Name"))
        self.phone.setPlaceholderText(_translate("MainWindow", "Phone"))
        self.additional.setPlaceholderText(_translate("MainWindow", "Additional Info"))
        self.amount.setPlaceholderText(_translate("MainWindow", "Amount"))
        self.notes.setPlaceholderText(_translate("MainWindow", "Notes"))
        self.frame2label.setText(_translate("MainWindow", "Service Details"))
        self.admin.setText(_translate("MainWindow", "ADMIN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
