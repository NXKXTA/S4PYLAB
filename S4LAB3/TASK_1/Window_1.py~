from PyQt5.QtWidgets import QWidget, QVBoxLayout, QRadioButton, QLabel

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Времена года")
        self.setGeometry(100, 100, 500, 150)
        # Создаем вертикальный layout
        layout = QVBoxLayout()

        # Создаем радиокнопки для времен года
        self.winter_radio = QRadioButton("Зима", self)
        self.spring_radio = QRadioButton("Весна", self)
        self.summer_radio = QRadioButton("Лето", self)
        self.autumn_radio = QRadioButton("Осень", self)

        # Создаем метку для вывода информации
        self.info_label = QLabel("", self)

        # Добавляем радиокнопки и метку в layout
        layout.addWidget(self.winter_radio)
        layout.addWidget(self.spring_radio)
        layout.addWidget(self.summer_radio)
        layout.addWidget(self.autumn_radio)
        layout.addWidget(self.info_label)

        # Устанавливаем layout для окна
        self.setLayout(layout)

        # Подключаем обработчики событий для радиокнопок
        self.winter_radio.toggled.connect(self.update_info)
        self.spring_radio.toggled.connect(self.update_info)
        self.summer_radio.toggled.connect(self.update_info)
        self.autumn_radio.toggled.connect(self.update_info)

        # Устанавливаем радиокнопку "Зима" по умолчанию
        self.winter_radio.setChecked(True)
        self.update_info()

    def update_info(self):
        # Обновляем информацию в метке в зависимости от выбранной радиокнопки
        if self.winter_radio.isChecked():
            self.info_label.setText("Зима - холодное время года с снегом и морозами.")
        elif self.spring_radio.isChecked():
            self.info_label.setText("Весна - время года, когда природа пробуждается после зимы.")
        elif self.summer_radio.isChecked():
            self.info_label.setText("Лето - теплое время года с длинными днями и короткими ночами.")
        elif self.autumn_radio.isChecked():
            self.info_label.setText("Осень - время года, когда листья на деревьях желтеют и опадают.")