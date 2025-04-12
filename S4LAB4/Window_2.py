from PyQt5.QtWidgets import (
    QWidget, QFormLayout, QLineEdit, QCheckBox, QPushButton, QMessageBox, QVBoxLayout
)

class Window2(QWidget):
    def __init__(self):
        super().__init__()  # Инициализация родительского класса QWidget
        self.initUI()  # Вызов метода для настройки интерфейса

    def initUI(self):
        # Основной layout (вертикальный)
        layout = QVBoxLayout()

        # Форма для ввода данных (QFormLayout для удобного размещения меток и полей)
        form_layout = QFormLayout()

        # Поля для ФИО
        self.first_name = QLineEdit()  # Поле для ввода имени
        self.last_name = QLineEdit()  # Поле для ввода фамилии
        self.middle_name = QLineEdit()  # Поле для ввода отчества
        form_layout.addRow("Имя:", self.first_name)  # Добавляем поле имени в форму
        form_layout.addRow("Фамилия:", self.last_name)  # Добавляем поле фамилии в форму
        form_layout.addRow("Отчество:", self.middle_name)  # Добавляем поле отчества в форму

        # Поле для почты
        self.email = QLineEdit()  # Поле для ввода почты
        form_layout.addRow("Почта:", self.email)  # Добавляем поле почты в форму

        # Поле для телефона
        self.phone = QLineEdit()  # Поле для ввода телефона
        form_layout.addRow("Телефон:", self.phone)  # Добавляем поле телефона в форму

        # Чекбоксы для тем
        self.topics = {
            "Программирование": QCheckBox("Программирование"),  # Чекбокс для темы "Программирование"
            "Математика": QCheckBox("Математика"),  # Чекбокс для темы "Математика"
            "Физика": QCheckBox("Физика"),  # Чекбокс для темы "Физика"
        }
        for topic, checkbox in self.topics.items():
            form_layout.addRow(topic, checkbox)  # Добавляем чекбоксы в форму

        # Чекбоксы для согласий
        self.agree_personal_data = QCheckBox("Согласие на обработку персональных данных")  # Чекбокс для согласия на обработку данных
        self.agree_mailing = QCheckBox("Согласие на рассылку")  # Чекбокс для согласия на рассылку
        form_layout.addRow(self.agree_personal_data)  # Добавляем чекбокс согласия на обработку данных в форму
        form_layout.addRow(self.agree_mailing)  # Добавляем чекбокс согласия на рассылку в форму

        # Кнопка для проверки ввода
        self.submit_button = QPushButton("Проверить")  # Кнопка для проверки введенных данных
        self.submit_button.clicked.connect(self.validate_input)  # Подключаем метод validate_input к событию нажатия на кнопку
        form_layout.addRow(self.submit_button)  # Добавляем кнопку в форму

        # Добавляем форму в основной layout
        layout.addLayout(form_layout)  # Добавляем форму в вертикальный layout
        self.setLayout(layout)  # Устанавливаем layout для окна

    def validate_input(self):
        # Проверка полей
        errors = []  # Список для хранения ошибок
        if not self.first_name.text():  # Проверяем, заполнено ли поле имени
            errors.append("Имя не заполнено.")
        if not self.last_name.text():  # Проверяем, заполнено ли поле фамилии
            errors.append("Фамилия не заполнена.")
        if not self.email.text():  # Проверяем, заполнено ли поле почты
            errors.append("Почта не заполнена.")
        if not self.phone.text():  # Проверяем, заполнено ли поле телефона
            errors.append("Телефон не заполнен.")
        if not self.agree_personal_data.isChecked():  # Проверяем, поставлен ли чекбокс согласия на обработку данных
            errors.append("Необходимо согласие на обработку персональных данных.")

        # Вывод ошибок или успеха
        if errors:  # Если есть ошибки
            QMessageBox.critical(self, "Ошибка", "\n".join(errors))  # Показываем сообщение об ошибке
        else:  # Если ошибок нет
            QMessageBox.information(self, "Успех", "Данные введены корректно.")  # Показываем сообщение об успехе