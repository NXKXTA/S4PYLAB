from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QMimeData, QPoint
from PyQt5.QtGui import QDrag


class DraggableLabel(QLabel):
    def __init__(self, text, parent):
        super().__init__(text, parent)  # Инициализация QLabel с текстом и родительским виджетом
        self.setStyleSheet("""
            background-color: lightblue; 
            padding: 10px; 
            border: 1px solid black;
            border-radius: 5px;
        """)  # Устанавливаем стиль виджета (цвет, отступы, границы и скругление углов)
        self.setAlignment(Qt.AlignCenter)  # Выравниваем текст по центру
        self.mousePos = QPoint()  # Инициализируем переменную для хранения позиции клика
        self.adjustSize()  # Автоматически подгоняем размер виджета под текст

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:  # Проверяем, что нажата левая кнопка мыши
            self.mousePos = event.pos()  # Сохраняем позицию клика относительно виджета
            self.raise_()  # Поднимаем виджет на передний план

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):  # Проверяем, что левая кнопка мыши зажата
            return

        # Создаем объект перетаскивания
        drag = QDrag(self)  # Инициализируем объект QDrag для перетаскивания
        mime = QMimeData()  # Создаем объект MimeData для хранения данных перетаскивания
        mime.setText("custom/draggable-widget")  # Устанавливаем уникальный MIME-тип

        drag.setMimeData(mime)  # Привязываем MimeData к объекту перетаскивания
        drag.setPixmap(self.grab())  # Устанавливаем изображение виджета при перетаскивании
        drag.setHotSpot(self.mousePos)  # Устанавливаем точку "захвата" виджета

        # Начинаем перетаскивание
        drag.exec_(Qt.MoveAction)  # Запускаем перетаскивание с действием "перемещение"


class Window3(QWidget):
    def __init__(self):
        super().__init__()  # Инициализация родительского класса QWidget
        self.initUI()  # Вызов метода для настройки интерфейса
        self.setAcceptDrops(True)  # Разрешаем принимать события перетаскивания

    def initUI(self):
        layout = QVBoxLayout()  # Создаем вертикальный layout
        self.label = QLabel("Кликайте в верхней половине окна, чтобы создать виджет.")
        layout.addWidget(self.label)  # Добавляем метку в layout
        self.setLayout(layout)  # Устанавливаем layout для окна

    def mousePressEvent(self, event):
        # Создаем виджет только в верхней половине
        if event.y() < self.height() // 2:  # Проверяем, что клик был в верхней половине окна
            widget = DraggableLabel("Перетащи меня вниз", self)  # Создаем новый виджет
            widget.move(event.pos())  # Устанавливаем позицию виджета в точке клика
            widget.show()  # Показываем виджет

    def dragEnterEvent(self, event):
        # Разрешаем перетаскивание только наших виджетов
        if event.mimeData().hasText() and event.mimeData().text() == "custom/draggable-widget":
            event.acceptProposedAction()  # Принимаем событие перетаскивания

    def dropEvent(self, event):
        # Получаем виджет из события перетаскивания
        widget = event.source()  # Получаем виджет, который перетаскивается

        # Проверяем, что отпустили в нижней половине
        if event.pos().y() > self.height() // 2:  # Проверяем, что позиция отпускания в нижней половине
            new_pos = event.pos() - widget.mousePos  # Рассчитываем новую позицию виджета
            widget.move(new_pos)  # Перемещаем виджет
            event.accept()  # Принимаем событие
        else:
            event.ignore()  # Игнорируем событие, если отпустили в верхней половине