# -*- coding: utf-8 -*-
"""
First steps in GUI application using PyQt5 classes.

Created on Sat Nov 14 10:18:05 2020

@author: mikeqin

References:
    [1] V. Lakshminarayanan, H. Ghalila, A. Ammar, and L. S. Varadharajan, 
        Understanding optics with Python. CRC Press, 2017.
"""

# ============================================================================
#%% Imports
# ============================================================================
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


# ============================================================================
#%% Create a MainWindow class
# ============================================================================
class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        # GUI proprieties
        self.setGeometry(400, 100, 300, 200)
        self.setWindowTitle('My first app')


# ============================================================================
#%% Main function
# ============================================================================
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()