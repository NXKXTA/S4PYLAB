import sys  # Только для доступа к аргументам командной строки
from PyQt5.QtWidgets import QApplication
from Window import Window


app = QApplication(sys.argv)  # Передаём sys.argv, чтобы разрешить аргументы командной строки для приложения.
window = Window()
window.show()
sys.exit(app.exec())