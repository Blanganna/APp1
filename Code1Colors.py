# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 17:51:36 2022

@author: ablan
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import QCoreApplication
class Color(QWidget):
  def _init_(self, color):
    super()._init_()
    self.setAutoFillBackground(True) 
    self.myPalette = self.palette() 
    self.myPalette.setColor(QPalette.Window, QColor(color))
    self.setPalette(self.myPalette) 

class Window(QMainWindow):
  def _init_(self):
    super()._init_()
    self.setWindowTitle("Horizontal Box Layouts")
    self.layout = QHBoxLayout()
    self.layout.addWidget(Color('blue'))
    self.layout.addWidget(Color('white'))
    self.layout.addWidget(Color('red'))
    self.widget = QWidget()
    self.widget.setLayout(self.layout)
    self.setCentralWidget(self.widget)

app = QCoreApplication.instance()
if app is None:
  app = QApplication(sys.argv)
window = Window()
window.show()
app.exec_()
