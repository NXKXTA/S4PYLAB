from PySide6.QtCore import QPropertyAnimation, QPoint, QEasingCurve
from PySide6.QtWidgets import QApplication, QWidget, QPushButton


# Создаем класс окна, наследуясь от QWidget
class Window(QWidget):
    def __init__(self):
        super().__init__()  # Вызываем конструктор родительского класса (QWidget)
        self.setMinimumWidth(1000)  # Устанавливаем минимальную ширину окна в 1000 пикселей
        self.setMinimumHeight(500)   # Устанавливаем минимальную высоту окна в 500 пикселей
        self.setWindowTitle("Анимация виджетов") # Задаем заголовок окна

        # Создаем кнопку с текстом "Я еду по экспоненте"
        # Второй параметр (self) указывает, что кнопка будет внутри этого окна
        button = QPushButton('Я еду по экспоненте', self)

        # Создаем анимацию для свойства "pos" (позиция) кнопки
        # b"pos" - преобразуем строку в байты (требуется для QPropertyAnimation)
        # self - указывает, что анимация принадлежит этому окну
        anim = QPropertyAnimation(button, b"pos", self)

        # Устанавливаем продолжительность анимации в 5000 миллисекунд (5 секунд)
        anim.setDuration(5000)

        # Устанавливаем начальную позицию анимации - точка (0, 0) в окне
        anim.setStartValue(QPoint(0, 0))

        # Устанавливаем конечную позицию анимации - точка (100, 250) в окне
        anim.setEndValue(QPoint(100, 250))

        # Задаем функцию плавности анимации - экспоненциальное ускорение
        anim.setEasingCurve(QEasingCurve.InExpo)

        # Запускаем анимацию
        anim.start()


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
