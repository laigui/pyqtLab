# -*- coding: utf-8 -*-
"""
Matplotlib widget class using PyQt5.

Created on Sat Nov 14 17:22:26 2020

@author: mikeqin

References:
    [1] S. Tosi, Matplotlib for Python Developers. Birmingham, UK: Packt Publishing, 2009.
"""

# ============================================================================
#%% Imports
# ============================================================================
from PyQt5.QtWidgets import QSizePolicy, QWidget, QVBoxLayout
# import the Qt5Agg FigureCanvas object, that binds Figure to
# Qt5Agg backend. It also inherits from QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# Matplotlib Toolbar
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
# Matplotlib Figure object
from matplotlib.figure import Figure
from matplotlib import rcParams
rcParams['font.size'] = 9


# ============================================================================
#%% Matplotlib Canvas Class
# ============================================================================
class MplCanvas(FigureCanvas):
    """Class to represent the FigureCanvas widget"""

    def __init__(self):
        # setup Matplotlib Figure and Axis
        self.fig = Figure()
        self.ax1 = self.fig.add_subplot(211)
        self.ax2 = self.fig.add_subplot(212)
        # initialization of the canvas
        FigureCanvas.__init__(self, self.fig)
        # we define the widget as expandable
        FigureCanvas.setSizePolicy(
            self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        # notify the system of updated policy
        FigureCanvas.updateGeometry(self)


# ============================================================================
#%% Matplotlib Widget Class
# ============================================================================
class MPL_WIDGET(QWidget):
    """Widget defined in Qt Designer"""

    def __init__(self, parent=None):
        # initialization of Qt MainWindow widget
        QWidget.__init__(self, parent)
        # set the canvas to the Matplotlib canvas
        self.canvas = MplCanvas()
        # create a navigation toolbar for our plot canvas
        self.navi_toolbar = NavigationToolbar(self.canvas, self)
        # create a vertical box layout
        self.vbl = QVBoxLayout()
        # add mpl widget to vertical box
        self.vbl.addWidget(self.canvas)
        # add the navigation toolbar to vertical box
        self.vbl.addWidget(self.navi_toolbar)
        # set the layout to vertical box
        self.setLayout(self.vbl)
