from PyQt5.QtWidgets import QLabel, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap

# Класс окна
class Window(QMainWindow):
    def __init__(self):  # Конструктор, с названием будущего окна
        super().__init__()  # Вызов конструктора родительского класса

        # Делаем квадратное окно
        self.setWindowTitle("Окно обыкновенное")  # Название окна
        self.setGeometry(100, 100, 660, 660)  # Размеры окна: x, y, ширина, высота
        # x, y - координаты левого верхнего угла создаваемого окна на мониторе

        # Создание первой метки
        label1 = QLabel(self)  # Я делаю плакат, а QLabel — это наклейка, на которую можно написать текст или приклеить картинку.
        label1.setText("Это очень длинный текст, который нужно перенести на следующую строку. Надеюсь, он не вылезет за края.")
        label1.setAlignment(Qt.AlignCenter)  # Выравнивание текста по центру
        label1.setWordWrap(True)  # Перенос текста на следующую строку
        label1.setFont(QFont("Arial", 14, QFont.StyleItalic))  # Шрифт и размер
        label1.setGeometry(20, 20, 200, 200)  # Размеры метки
        label1.setStyleSheet("padding: 10px; background-color: lightblue; margin-top: 20px;")

        # Создание второй метки
        label2 = QLabel(self)
        label2.setText("Я - текст второй метки!")
        label2.setAlignment(Qt.AlignCenter | Qt.AlignBottom)  # Выровняем по центру и снизу
        label2.setWordWrap(True)  # Перенос текста на следующую строку
        label2.setFont(QFont("Arial", 28))
        label2.setGeometry(20, 20, 200, 200)  # Отступы вокруг метки
        label2.setStyleSheet("padding: 10px; background-color: lightgreen; margin-top: 20px;")
        label2.move(20, 220)

        # Создание третей метки
        label3 = QLabel(self)
        picture_1 = QPixmap("../covers/pic_1.jpg")
        label3.setPixmap(picture_1)
        label3.setGeometry(240, 20, 400, 400)
        label3.setStyleSheet("margin-top: 20px;")
        label3.setScaledContents(True)  # Масштабируем картинку, а не обрезаем


        self.show()
