from PySide6.QtGui import QPainter, QPen, QBrush, QColor
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PySide6.QtCore import (QPropertyAnimation, QPoint,
                           QParallelAnimationGroup, QEasingCurve)

class AnimatedShapesWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):
        self.setWindowTitle("Параллельная анимация фигур")
        self.setGeometry(100, 100, 600, 600)
        self.show()

        # Создаем центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Создаем анимируемые виджеты
        self.square = AnimatedSquare(QColor("#ff8b0f"), central_widget)
        self.circle = AnimatedCircle(QColor("#2E8B57"), central_widget)

        # Устанавливаем начальные позиции
        self.square.move(50, 50)  # Переместить на (x, y)
        self.circle.move(500, 50)  # Переместить на (x, y)

        # Создаем анимации
        self.create_animations()

        self.show()

    def create_animations(self):
        # Анимация для квадрата (ломаная линия)
        square_anim = QPropertyAnimation(self.square, b"pos")
        square_anim.setDuration(4000)
        square_anim.setEasingCurve(QEasingCurve.InOutQuad)

        # Задаем ключевые точки для ломаной линии
        square_anim.setKeyValueAt(0.0, QPoint(50, 50))
        square_anim.setKeyValueAt(0.3, QPoint(200, 200))
        square_anim.setKeyValueAt(0.5, QPoint(350, 100))
        square_anim.setKeyValueAt(0.7, QPoint(200, 300))
        square_anim.setKeyValueAt(1.0, QPoint(50, 400))

        # Анимация для круга (прямая линия)
        circle_anim = QPropertyAnimation(self.circle, b"pos")
        circle_anim.setDuration(4000)
        circle_anim.setEasingCurve(QEasingCurve.InOutQuad)
        circle_anim.setStartValue(QPoint(500, 50))
        circle_anim.setEndValue(QPoint(100, 400))

        # Группа параллельных анимаций
        self.anim_group = QParallelAnimationGroup()
        self.anim_group.addAnimation(square_anim)
        self.anim_group.addAnimation(circle_anim)

        # Запускаем анимацию
        self.anim_group.start()


class AnimatedSquare(QWidget):
    def __init__(self, color, parent=None):
        super().__init__(parent)
        self.color = color
        self.setFixedSize(50, 50)


    def paintEvent(self, event):
        painter = QPainter(self)  # Создать художника
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)  # Добавить сглаживание границ
        painter.setBrush(QBrush(self.color))  #  Дать заливку
        painter.setPen(QPen(QColor(0, 0, 0), 2))  # Дать чёрную ручку
        painter.drawRect(0, 0, 50, 50)  # Рисовать квадрат


class AnimatedCircle(QWidget):
    def __init__(self, color, parent=None):
        super().__init__(parent)
        self.color = color
        self.setMaximumSize(60, 60)
        self.setMinimumSize(50, 50)


    def paintEvent(self, event):
        painter = QPainter(self)  # Создать художника
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)  # Добавить сглаживание границ
        painter.setBrush(QBrush(self.color))  # Дать заливку
        painter.setPen(QPen(QColor(0, 0, 0), 2))  # Дать чёрную ручку
        painter.drawEllipse(0, 0, 50, 50)  # Рисовать эллипс



