from PySide6.QtGui import QPainter, QPen, QBrush, QColor, QLinearGradient
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QPoint


class ShapesWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):
        self.setWindowTitle("Геометрические фигуры")
        self.setGeometry(100, 100, 600, 600)
        self.show()


    def paintEvent(self, event):
        painter = QPainter(self)
        self.draw_shapes(painter)
        painter.end()


    def draw_shapes(self, painter):
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Берём чёрный карандаш
        black_pen = QPen(QColor(0, 0, 0), 2)
        painter.setPen(black_pen)

        # Градиент для треугольника
        gradient = QLinearGradient(180, 50, 280, 150)  # x1, y1, x2, y2
        gradient.setColorAt(0.0, QColor("#00FFFF"))
        gradient.setColorAt(0.5, QColor("#0000FF"))
        gradient.setColorAt(1.0, QColor("#FFFFFF"))

        # Рисуем треугольник
        painter.setBrush(QBrush(gradient))
        triangle = [
            QPoint(290, 50),
            QPoint(240, 150),
            QPoint(190, 50)
        ]
        painter.drawPolygon(triangle)

        # Рисуем квадрат
        painter.setBrush(QBrush(QColor("#9370DB"))) # Даём фиолетовую заливку
        painter.drawRect(150, 170, 180, 180)  # Рисуем квадрат (x, y, width, heigh)

        # Рисуем эллипс
        painter.setBrush(QBrush(QColor(100, 255, 100)))  # Даём зелёную заливку
        painter.drawEllipse(30, 210, 100, 100)  # Рисуем эллипс (x, y, width, heigh)