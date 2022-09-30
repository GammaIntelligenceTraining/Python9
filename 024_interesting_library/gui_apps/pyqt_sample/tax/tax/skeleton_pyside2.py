import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

loader = QUiLoader()
file = QtCore.QFile("mainwindow.ui")
file.open(QtCore.QFile.ReadOnly)
file.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = loader.load(file, None)
    window.show()
    sys.exit(app.exec_())