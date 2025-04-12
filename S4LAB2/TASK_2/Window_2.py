from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.counter = 0  # Начальное значение счётчика
        self.initUI()

    def initUI(self):
        # Настройки окна
        self.setWindowTitle("Счётчик")
        self.setGeometry(100, 100, 300, 200)

        # Создаем вертикальный лейаут
        layout = QVBoxLayout()

        # Создаем поле для отображения значения счётчика
        self.label = QLabel("Счётчик: 0", self)
        self.label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #333;
            margin-bottom: 20px;
        """)

        # Создаем кнопку "Увеличить"
        self.increment_button = QPushButton("Увеличить", self)
        self.increment_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
        """)
        self.increment_button.clicked.connect(self.increment_counter)

        # Создаем кнопку "Сбросить"
        self.reset_button = QPushButton("Сбросить", self)
        self.reset_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                font-size: 16px;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #e53935;
            }
            QPushButton:pressed {
                background-color: #d32f2f;
            }
        """)
        self.reset_button.clicked.connect(self.reset_counter)

        # Добавляем элементы в лейаут
        layout.addWidget(self.label)
        layout.addWidget(self.increment_button)
        layout.addWidget(self.reset_button)

        # Устанавливаем лейаут в окно
        self.setLayout(layout)

    def increment_counter(self):
        # Увеличиваем счётчик на 1
        self.counter += 1
        self.label.setText(f"Счётчик: {self.counter}")

    def reset_counter(self):
        # Сбрасываем счётчик
        self.counter = 0
        self.label.setText(f"Счётчик: {self.counter}")