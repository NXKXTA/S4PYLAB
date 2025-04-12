from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Настройки окна
        self.setWindowTitle("Кнопка и текст")
        self.setGeometry(100, 100, 300, 150)

        # Создаем вертикальный лейаут
        layout = QVBoxLayout()

        # Создаем кнопку
        self.button = QPushButton("Нажми меня", self)
        self.button.setCheckable(True)  # Делаем кнопку "нажимаемой"
        self.button.clicked.connect(self.on_button_click)  # Подключаем обработчик нажатия

        # Устанавливаем начальный стиль кнопки
        self.button.setStyleSheet("""
            background-color: #5c5c5c;
            color: white;
            font-size: 16px;
            border-radius: 10px;
            padding: 10px;
        """)

        # Создаем поле с текстом
        self.label = QLabel("Кнопка отпущена", self)
        self.label.setStyleSheet("font-size: 16px;")  # Устанавливаем размер шрифта

        # Добавляем кнопку и текстовое поле в лейаут
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        # Устанавливаем лейаут в окно
        self.setLayout(layout)

    def on_button_click(self):
        # Обработчик нажатия кнопки
        if self.button.isChecked():
            self.label.setText("Кнопка нажата")
            self.button.setStyleSheet("""
                background-color: #05c702;
                color: white;
                font-size: 16px;
                border-radius: 10px;
                padding: 10px;
            """)
        else:
            self.label.setText("Кнопка отпущена")
            self.button.setStyleSheet("""
                background-color: #5c5c5c;
                color: white;
                font-size: 16px;
                border-radius: 10px;
                padding: 10px;
            """)