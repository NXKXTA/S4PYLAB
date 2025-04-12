import sys
from window_2 import AnimatedShapesWindow
from PySide6.QtWidgets import QApplication


app = QApplication(sys.argv)
window = AnimatedShapesWindow()
sys.exit(app.exec())