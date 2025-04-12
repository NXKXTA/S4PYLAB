from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget
import sys
from Window_1 import Window1
from Window_2 import Window2
from Window_3 import Window3

class MainWindow(QTabWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Создаем вкладки
        self.addTab(Window1(), "Расписание")
        self.addTab(Window2(), "Аккаунт")
        self.addTab(Window3(), "Перетаскивание")

        # Настройки окна
        self.setWindowTitle("Практика 4")
        self.setGeometry(100, 100, 600, 400)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())