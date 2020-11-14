# -*- coding: utf-8 -*-
"""
First steps in GUI application using PyQt5.

Created on Sat Nov 14 09:59:59 2020

@author: mikeqin

References:
    [1] V. Lakshminarayanan, H. Ghalila, A. Ammar, and L. S. Varadharajan, 
        Understanding optics with Python. CRC Press, 2017.
"""

# ============================================================================
#%% Imports
# ============================================================================
from PyQt5.QtWidgets import QApplication, QWidget
import sys


# ============================================================================
#%% Create a Window
# ============================================================================
# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) is fine.
app = QApplication(sys.argv)

window = QWidget()
window.setGeometry(400, 100, 300, 200)
window.setWindowTitle('My first app')
window.show() # IMPORTANT!!!!! Windows are hidden by default.
app.exec_() # Start the event loop.


