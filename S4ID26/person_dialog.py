from PyQt6.QtWidgets import QDialog, QVBoxLayout, QComboBox, QLineEdit, QLabel, QDialogButtonBox, QMessageBox
from PyQt6.QtGui import QDoubleValidator

class PersonDialog(QDialog):
    def __init__(self, initial_data=None):
        super().__init__()
        self.setWindowTitle("Редактировать данные" if initial_data else "Добавить человека")

        layout = QVBoxLayout()

        # Поле для выбора пола
        self.gender_combo = QComboBox()
        self.gender_combo.addItems(["Male", "Female"])
        layout.addWidget(QLabel("Пол:"))
        layout.addWidget(self.gender_combo)

        # Поле для ввода веса
        self.weight_edit = QLineEdit()
        layout.addWidget(QLabel("Вес (кг):"))
        layout.addWidget(self.weight_edit)

        # Поле для ввода роста
        self.height_edit = QLineEdit()
        layout.addWidget(QLabel("Рост (см):"))
        layout.addWidget(self.height_edit)

        # Заполняем поля если есть начальные данные
        if initial_data:
            self.gender_combo.setCurrentText(initial_data["gender"])
            self.weight_edit.setText(initial_data["weight"])
            self.height_edit.setText(initial_data["height"])

        # Кнопки
        self.buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        self.buttons.accepted.connect(self.validate)
        self.buttons.rejected.connect(self.reject)
        layout.addWidget(self.buttons)

        self.setLayout(layout)

    def validate(self):
            try:
                # Проверка введенных данных
                weight = float(self.weight_edit.text())
                height = float(self.height_edit.text())
                if weight <= 0 or height <= 0:
                    raise ValueError
                self.accept()
            except:
                QMessageBox.critical(self, "Ошибка", "Некорректные данные!")
                self.weight_edit.clear()
                self.height_edit.clear()

    def get_data(self):
        return {
            "gender": self.gender_combo.currentText(),
            "weight": self.weight_edit.text(),
            "height": self.height_edit.text()
        }