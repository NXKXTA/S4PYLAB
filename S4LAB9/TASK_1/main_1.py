import sys
from window_1 import ShapesWindow
from PySide6.QtWidgets import QApplication


app = QApplication(sys.argv)
window = ShapesWindow()
sys.exit(app.exec())