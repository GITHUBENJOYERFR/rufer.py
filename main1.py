from instr import *
from second_win import *
from PyQt5.QtCore import Qt, QTimer,QTime,QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator,QFont
from PyQt5.QtWidgets import QApplication,QVBoxLayout,QWidget,QHBoxLayout,QGridLayout,QGroupBox,QRadioButton,QPushButton,QLabel,QListWidget,QLineEdit

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('health test')
question1 = QLabel(txt_name)
main_win.show()
app.exec_()