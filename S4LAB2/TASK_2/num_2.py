from PyQt5.QtWidgets import QApplication
from Window_2 import Window
import sys

app = QApplication(sys.argv)  # Создаем приложение
window = Window()  # Создаем окно
window.show()  # Показываем окно
sys.exit(app.exec_())  # Запускаем главный цикл приложения\
