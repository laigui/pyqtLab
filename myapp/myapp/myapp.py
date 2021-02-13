# ===========================================================================
# Imports
# ===========================================================================
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QAction, QApplication, QDesktopWidget, QDialog, QFileDialog,
                             QHBoxLayout, QLabel, QMainWindow, QToolBar, QVBoxLayout, QWidget)

try:
    # Assume we're a sub-module in a package.
    from .gui.mainwindow import *
except ImportError:
    # Apparently no higher-level package has been imported, fall back to a local import.
    from gui.mainwindow import *


# ===========================================================================
# Application GUI
# ===========================================================================
class MainWindow(QMainWindow):
    """Create the main window that stores all of the widgets necessary for the application."""

    def __init__(self):
        """Initialize the components of the main window."""
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resize(1024, 768)
        self.setWindowTitle('myapp')
        self.ui.actionOpen.triggered.connect(self.openFileDialog)

    def openFileDialog(self):
        """Open a QFileDialog to allow the user to open a file into the application."""
        filename, accepted = QFileDialog.getOpenFileName(self, 'Open File')

        if accepted:
            with open(filename) as file:
                file.read()



# ===========================================================================
# Application entry
# ===========================================================================
def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    desktop = QDesktopWidget().availableGeometry()
    width = (desktop.width() - win.width()) / 2
    height = (desktop.height() - win.height()) / 2
    win.show()
    win.move(width, height)
    sys.exit(app.exec_())


# ===========================================================================
if __name__ == "__main__":
    sys.exit(main())