import sys

from PySide6 import QtWidgets
from merge_plus import Widget
from PySide6.QtCore import Qt


app = QtWidgets.QApplication(sys.argv)

window = Widget()
window.setWindowFlags(Qt.FramelessWindowHint)

window.show()

app.exec()