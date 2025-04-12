from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Настройки окна
        self.setWindowTitle("Калькулятор")
        self.setGeometry(100, 100, 400, 300)

        # Создаем вертикальный лейаут
        layout = QVBoxLayout()

        # Поле для ввода первого числа
        self.input_1 = QLineEdit(self)
        self.input_1.setPlaceholderText("Введите первое число")
        self.input_1.setStyleSheet("font-size: 16px; padding: 5px;")
        layout.addWidget(self.input_1)

        # Поле для ввода второго числа
        self.input_2 = QLineEdit(self)
        self.input_2.setPlaceholderText("Введите второе число")
        self.input_2.setStyleSheet("font-size: 16px; padding: 5px;")
        layout.addWidget(self.input_2)

        # Горизонтальный лейаут для кнопок
        buttons_layout = QHBoxLayout()

        # Кнопка сложения
        self.plus_button = QPushButton("+", self)
        self.plus_button.setStyleSheet("font-size: 16px; padding: 10px;")
        self.plus_button.clicked.connect(lambda: self.calculate("+"))
        buttons_layout.addWidget(self.plus_button)

        # Кнопка вычитания
        self.subtract_button = QPushButton("-", self)
        self.subtract_button.setStyleSheet("font-size: 16px; padding: 10px;")
        self.subtract_button.clicked.connect(lambda: self.calculate("-"))
        buttons_layout.addWidget(self.subtract_button)

        # Кнопка умножения
        self.multiply_button = QPushButton("*", self)
        self.multiply_button.setStyleSheet("font-size: 16px; padding: 10px;")
        self.multiply_button.clicked.connect(lambda: self.calculate("*"))
        buttons_layout.addWidget(self.multiply_button)

        # Кнопка деления
        self.divide_button = QPushButton("/", self)
        self.divide_button.setStyleSheet("font-size: 16px; padding: 10px;")
        self.divide_button.clicked.connect(lambda: self.calculate("/"))
        buttons_layout.addWidget(self.divide_button)

        # Кнопка возведения в степень
        self.power_button = QPushButton("x^y", self)
        self.power_button.setStyleSheet("font-size: 16px; padding: 10px;")
        self.power_button.clicked.connect(lambda: self.calculate("^"))
        buttons_layout.addWidget(self.power_button)

        # Добавляем горизонтальный лейаут с кнопками в основной лейаут
        layout.addLayout(buttons_layout)

        # Поле для вывода результата
        self.result_label = QLabel("Результат будет здесь", self)
        self.result_label.setStyleSheet("font-size: 18px; font-weight: bold; margin-top: 20px;")
        self.result_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.result_label)

        # Устанавливаем лейаут в окно
        self.setLayout(layout)

    def calculate(self, operation):
        try:
            # Получаем числа из полей ввода
            num1 = int(self.input_1.text())
            num2 = int(self.input_2.text())

            # Выполняем операцию
            if operation == "+":
                result = num1 + num2
                self.result_label.setText(f"{num1} + {num2} = {result}")
            elif operation == "-":
                result = num1 - num2
                self.result_label.setText(f"{num1} - {num2} = {result}")
            elif operation == "*":
                result = num1 * num2
                self.result_label.setText(f"{num1} * {num2} = {result}")
            elif operation == "/":
                if num2 == 0:
                    self.result_label.setText("Ошибка: деление на ноль")
                    return
                result = num1 / num2
                self.result_label.setText(f"{num1} / {num2} = {result}")
            elif operation == "^":
                result = num1 ** num2
                self.result_label.setText(f"{num1}<sup>{num2}</sup> = {result}")
        except ValueError:
            self.result_label.setText("Ошибка: введите целые числа")