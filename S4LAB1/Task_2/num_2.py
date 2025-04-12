import sys  # Только для доступа к аргументам командной строки
from PyQt5.QtWidgets import QApplication
from App import BookApp


app = QApplication(sys.argv)  # Передаём sys.argv, чтобы разрешить аргументы командной строки для приложения.
window = BookApp()
window.show()
sys.exit(app.exec())