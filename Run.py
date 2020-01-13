from Windows import *
import sys
from PyQt5 import QtWidgets

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Window = MWindow()
    Window.show()
    sys.exit(app.exec_())
