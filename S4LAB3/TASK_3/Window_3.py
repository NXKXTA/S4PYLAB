from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QDateEdit, QTextEdit, QPushButton
)
from PyQt6.QtCore import QDate
from datetime import datetime

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Кнопка и текст")
        self.setGeometry(100, 100, 300, 300)
        # Основной layout
        layout = QVBoxLayout()

        # Метка для инструкции
        self.label = QLabel("Введите дату рождения:")
        layout.addWidget(self.label)

        # Виджет для ввода даты
        self.date_edit = QDateEdit()
        self.date_edit.setDisplayFormat("dd.MM.yyyy")  # Формат даты
        self.date_edit.setDate(QDate.currentDate())  # Устанавливаем текущую дату по умолчанию
        self.date_edit.setCalendarPopup(True)  # Всплывающий календарь
        layout.addWidget(self.date_edit)

        # Кнопка для расчета
        self.calculate_button = QPushButton("Рассчитать")
        self.calculate_button.clicked.connect(self.calculate_age)
        layout.addWidget(self.calculate_button)

        # Текстовое поле для вывода результатов
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)  # Запрещаем редактирование
        layout.addWidget(self.result_text)

        # Устанавливаем layout для окна
        self.setLayout(layout)

    def calculate_age(self):
        # Получаем введенную дату рождения
        birth_date = self.date_edit.date()

        # Преобразуем QDate в datetime
        birth_datetime = datetime(birth_date.year(), birth_date.month(), birth_date.day())

        # Текущая дата и время
        current_datetime = datetime.now()

        # Вычисляем разницу между текущим временем и временем рождения
        delta = current_datetime - birth_datetime

        # Если разница отрицательная, значит, дата рождения в будущем
        if delta.total_seconds() < 0:
            result = "<h2>Ошибка:</h2><p>Дата рождения не может быть в будущем.</p>"
        else:
            # Рассчитываем общее количество секунд
            total_seconds = int(delta.total_seconds())

            # Количество лет
            years = total_seconds // (365 * 24 * 3600)
            # years = current_datetime.year - birth_datetime.year

            # Количество часов
            hours = total_seconds // 3600

            # Количество секунд
            seconds = total_seconds


            # Форматируем результат
            result = (
                f"<h2>Результаты расчета:</h2>"
                f"<p><b>Лет:</b> {years}</p>"
                f"<p><b>Часов:</b> {hours}</p>"
                f"<p><b>Секунд:</b> {seconds}</p>"
            )

        # Выводим результат в QTextEdit
        self.result_text.setHtml(result)