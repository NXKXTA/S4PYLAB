from PyQt6.QtWidgets import QApplication
from Window_1 import Window
import sys

app = QApplication(sys.argv)  # Создаем приложение
window = Window()  # Создаем окно
window.show()  # Показываем окно
sys.exit(app.exec_())  # Запускаем главный цикл приложения