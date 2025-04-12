from PyQt6.QtWidgets import QApplication
from Window_1 import MainWindow
import sys

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())