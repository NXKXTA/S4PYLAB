from Book import Book
from PyQt5.QtWidgets import (QMainWindow, QLabel, QScrollArea, QVBoxLayout, QFrame, QWidget,
                             QHBoxLayout)  # Импортируем виджеты PyQt5
from PyQt5.QtGui import QPixmap  # Импортируем QPixmap для работы с картинками
from PyQt5.QtCore import Qt  # Импортируем Qt для использования флагов (например, выравнивание)

books = [
    Book("Гарри Поттер и проклятый код", "Дж.К. Роулинг", 404, "../covers/tupa_ya.jpg"),
    Book("Как выжить в Брагино", "Чак Норис", 9999, "../covers/brzd.jpg")
]


# Создаем класс BookApp, который наследуется от QWidget (базовый виджет PyQt5)
class BookApp(QWidget):
    def __init__(self):
        super().__init__()  # Вызываем конструктор родительского класса (QWidget)
        self.initUI()  # Вызываем метод для настройки интерфейса

    def initUI(self):
        # Настройки окна
        self.setWindowTitle('Книжный чертог PyQt')  # Устанавливаем заголовок окна
        self.setGeometry(300, 300, 600, 400)  # Устанавливаем размер и положение окна (x, y, width, height)

        # Создаем прокручиваемую область (QScrollArea)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)  # Разрешаем изменение размера содержимого

        # Контейнер для всех книг (QWidget)
        container = QWidget()
        self.vbox = QVBoxLayout(container)  # Создаем вертикальный лейаут для контейнера

        # Для каждой книги создаем свой виджет
        for book in books:
            self.add_book_widget(book)

        # Настраиваем прокрутку
        scroll.setWidget(container)  # Помещаем контейнер в прокручиваемую область

        # Главный лейаут (QVBoxLayout)
        main_layout = QVBoxLayout(self)  # Создаем вертикальный лейаут для главного окна
        main_layout.addWidget(scroll)  # Добавляем прокручиваемую область в главный лейаут

    def add_book_widget(self, book):
        # Создаем фрейм для книги (QFrame)
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)  # Устанавливаем стиль рамки (StyledPanel — красивая рамка)
        frame.setFixedHeight(200)  # Фиксируем высоту фрейма (200 пикселей)

        # Создаем горизонтальный лейаут для фрейма (QHBoxLayout)
        layout = QHBoxLayout(frame)

        # Загрузка обложки книги
        try:
            pixmap = QPixmap(book.cover_path)  # Загружаем картинку по указанному пути
            if not pixmap.isNull():  # Проверяем, что картинка загрузилась
                pixmap = pixmap.scaled(150, 200,
                                       Qt.KeepAspectRatio)  # Масштабируем картинку (150x200, сохраняя пропорции)
                cover_label = QLabel()  # Создаем QLabel для отображения картинки
                cover_label.setPixmap(pixmap)  # Устанавливаем картинку в QLabel
                layout.addWidget(cover_label)  # Добавляем QLabel в лейаут
            else:
                raise FileNotFoundError  # Если картинка не загрузилась, выбрасываем ошибку
        except:
            error_label = QLabel("😡 Обложка сгорела в аду!")  # Создаем QLabel с сообщением об ошибке
            layout.addWidget(error_label)  # Добавляем QLabel в лейаут

        # Создаем QLabel для текста с информацией о книге
        info_label = QLabel(book.get_info())  # Используем метод get_info() для получения текста
        info_label.setAlignment(Qt.AlignTop)  # Выравниваем текст по верхнему краю
        info_label.setStyleSheet("font-size: 14px;")  # Устанавливаем стиль текста (размер шрифта 14px)
        layout.addWidget(info_label)  # Добавляем QLabel в лейаут

        # Добавляем фрейм в общий вертикальный лейаут
        self.vbox.addWidget(frame)

