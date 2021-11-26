# -*- coding: UTF-8 -*-
import sys
import json
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

reload(sys)
sys.setdefaultencoding('utf8')


class App(QWidget):

    def __init__(self,row,col,str):
        super(App,self).__init__()
        self.title = '系统资源监控'
        self.left = 0
        self.top = 0
        self.width = 1300
        self.height = 600
        self.initUI(row,col,str)
        
    def initUI(self,row,col,str):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createTable(row,col,str)

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 

        # Show widget
        self.show()

    def createTable(self,row,col,str):
       # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(col)
        list1 = ["pid","进程名","CPU","内存占用率","GPU","硬盘占用率","网络","I/O"]
        for nameid in range(0,len(list1)):
            self.tableWidget.setItem(0,nameid, QTableWidgetItem(list1[nameid]))
        strlist = str.split("key")
        for i in range(1,len(strlist)):
            print(strlist[i])
            print(type(strlist[i]))
            user_dict = json.loads(strlist[i])
            for key,values in user_dict.items():
                print(key,values,list1.index(key))
                self.tableWidget.setItem(i,list1.index(key), QTableWidgetItem("%s"%values))
        self.tableWidget.move(0,0)

        # table selection change
        # self.tableWidget.doubleClicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
 
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())  